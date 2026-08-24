"""Thread-safe sliding-window rate limiter."""
from collections import deque
import threading
import time


class SlidingWindow:
    def __init__(self, limit: int, window_seconds: float, clock=time.monotonic):
        if limit <= 0 or window_seconds <= 0:
            raise ValueError("limit and window_seconds must be positive")
        self.limit = limit
        self.window_seconds = float(window_seconds)
        self.clock = clock
        self.events = deque()
        self.lock = threading.Lock()

    def allow(self) -> bool:
        with self.lock:
            now = self.clock()
            cutoff = now - self.window_seconds
            while self.events and self.events[0] <= cutoff:
                self.events.popleft()
            if len(self.events) >= self.limit:
                return False
            self.events.append(now)
            return True
