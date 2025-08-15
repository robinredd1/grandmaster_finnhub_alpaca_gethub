
# Grandmaster Sweep — Finnhub (Data) + Alpaca Paper (Orders) — GitHub Edition

**No secrets in code.** Add your keys as environment variables.

## Files
- `bot.py` — Finnhub scanning (async) + Alpaca Paper orders
- `config.py` — reads `FINNHUB_API_KEY`, `ALPACA_API_KEY`, `ALPACA_API_SECRET` from environment
- `.replit` — auto-installs deps then runs the bot
- `requirements.txt` — minimal deps
- `.gitignore` — keeps `.env` and caches out of repo
- `sample.env` — template to copy if running locally

## Upload to GitHub → Run on Replit
1. Create a **new GitHub repo** (empty). Upload these files.
2. In **Replit** → Create Repl → **Import from GitHub** (select your repo).
3. In Replit, set **Secrets** (lock icon in left sidebar):
   - `FINNHUB_API_KEY` = your Finnhub key
   - `ALPACA_API_KEY` = your Alpaca Paper key
   - `ALPACA_API_SECRET` = your Alpaca Paper secret
4. Click **Run**.

## Local dev (optional)
Create a private `.env` (do **not** commit):
```
FINNHUB_API_KEY=your_finnhub_key
ALPACA_API_KEY=your_alpaca_key
ALPACA_API_SECRET=your_alpaca_secret
```
Export then run:
```
export $(cat .env | xargs) && python bot.py
```

## Tuning (edit `config.py`)
- `SCAN_BATCH_SIZE`, `CONCURRENCY` — control scan size & speed
- `MAX_OPEN_POSITIONS`, `DOLLARS_PER_TRADE` — risk sizing
- `TRAIL_PERCENT`, `TIME_EXIT_MINUTES` — exits
- `FORCE_BUY_ON_FIRST_PASS=True` — immediate entries on first loop
