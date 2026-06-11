# Architecture

## Components

### Request Handler
Receives incoming API requests.

### Rate Limiter Core
Applies rate limiting rules per client.

### Token Bucket Module
Controls request rate using token refill logic.

### Sliding Window Module
Tracks request count over a rolling time window.

## Data Flow

Incoming Request → Rate Limiter → Allow / Deny → Response
