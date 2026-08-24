import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rate_limiter import RateLimiter
from src.token_bucket import TokenBucket
from src.sliding_window import SlidingWindow


def test_token_bucket_burst_and_rejection():
    limiter = TokenBucket(capacity=2, refill_rate=1, clock=lambda: 0.0)
    assert limiter.allow()
    assert limiter.allow()
    assert not limiter.allow()


def test_sliding_window_limit():
    clock = [0.0]
    limiter = SlidingWindow(limit=2, window_seconds=10, clock=lambda: clock[0])
    assert limiter.allow()
    assert limiter.allow()
    assert not limiter.allow()
    clock[0] = 10.1
    assert limiter.allow()


def test_facade_selects_algorithm():
    assert RateLimiter("token_bucket", capacity=1, refill_rate=1).allow()
    assert RateLimiter("sliding_window", limit=1, window_seconds=10).allow()
