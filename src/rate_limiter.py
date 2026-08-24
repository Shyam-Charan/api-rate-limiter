"""Unified rate limiter facade."""
from .token_bucket import TokenBucket
from .sliding_window import SlidingWindow


class RateLimiter:
    def __init__(self, algorithm="token_bucket", **kwargs):
        if algorithm == "token_bucket":
            self.limiter = TokenBucket(**kwargs)
        elif algorithm == "sliding_window":
            self.limiter = SlidingWindow(**kwargs)
        else:
            raise ValueError("algorithm must be token_bucket or sliding_window")

    def allow(self, tokens=1):
        if isinstance(self.limiter, TokenBucket):
            return self.limiter.allow(tokens)
        return self.limiter.allow()
