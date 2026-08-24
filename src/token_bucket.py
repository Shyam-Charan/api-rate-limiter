"""Thread-safe token bucket rate limiter."""
import threading
import time


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float, clock=time.monotonic):
        if capacity <= 0 or refill_rate <= 0:
            raise ValueError("capacity and refill_rate must be positive")
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.refill_rate = float(refill_rate)
        self.clock = clock
        self.last_refill = clock()
        self.lock = threading.Lock()

    def allow(self, tokens: int = 1) -> bool:
        if tokens <= 0 or tokens > self.capacity:
            raise ValueError("tokens must be between 1 and capacity")
        with self.lock:
            now = self.clock()
            elapsed = max(0.0, now - self.last_refill)
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
