# API Rate Limiter

A thread-safe Python rate-limiting library implementing two common admission-control algorithms:

- **Token Bucket** — supports bursts up to a configured capacity and refills at a configurable rate.
- **Sliding Window** — limits the number of requests observed in a rolling time window.

## Structure

```text
src/
  rate_limiter.py      # unified facade
  token_bucket.py      # token bucket implementation
  sliding_window.py   # sliding-window implementation
  main.py              # runnable demonstration
tests/
  test_rate_limiter.py
```

## Run

```bash
python -m src.main
```

## Example

```python
from src.rate_limiter import RateLimiter

limiter = RateLimiter("token_bucket", capacity=10, refill_rate=2)

if limiter.allow():
    print("request accepted")
else:
    print("request rejected")
```

Both implementations use locks so that request admission and state updates remain atomic when called from multiple threads.

## Design notes

Token Bucket is useful when short bursts are acceptable while maintaining a long-term rate. Sliding Window provides a direct rolling-window request-count limit. The facade makes the algorithms interchangeable without changing application code.
