# Deploy to Google Cloud Run

This bot ships with a `Dockerfile`, so it deploys to Cloud Run with no extra
build configuration.

## 1. Set your project

```sh
gcloud config set project YOUR_PROJECT_ID
```

## 2. Build and deploy

```sh
gcloud run deploy masterexpro \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars \
BOT_TOKEN=your_bot_token,\
API_ID=your_api_id,\
API_HASH=your_api_hash,\
DB_URL=your_mongodb_connection_string
```

Cloud Run will print a service URL when this finishes. This bot doesn't need
that URL for core functionality (it's polling-based, not webhook-based) —
it's only there to satisfy the platform's health-check requirement.

## 3. Verify

```sh
gcloud run services describe masterexpro --region us-central1
```

Visit the printed service URL — it should return a basic health-check response.

See `config.py` in the repo root for what each variable means. Only
`BOT_TOKEN`, `API_ID`, `API_HASH`, and `DB_URL` are required for the bot to
start; everything else (channel/log IDs) is optional and only affects
individual features.
