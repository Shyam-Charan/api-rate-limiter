"""Simple demonstration CLI."""
try:
    from .rate_limiter import RateLimiter
except ImportError:
    from rate_limiter import RateLimiter


def main():
    limiter = RateLimiter("token_bucket", capacity=5, refill_rate=1)
    results = [limiter.allow() for _ in range(7)]
    print("Requests:", results)


if __name__ == "__main__":
    main()
