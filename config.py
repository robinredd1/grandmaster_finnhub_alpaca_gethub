
# ====== config.py (GitHub-ready; secrets from environment) ======
import os

FINNHUB_API_KEY   = os.getenv("FINNHUB_API_KEY", "")
ALPACA_API_KEY    = os.getenv("ALPACA_API_KEY", "")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET", "")

UNIVERSE_MODE = "AUTO"                 # AUTO pulls symbols from Finnhub; FILE uses UNIVERSE_FILE
UNIVERSE_FILE = "symbols_all.txt"      # only used if UNIVERSE_MODE == "FILE"

SCAN_BATCH_SIZE = 500
CONCURRENCY = 50
BASE_SCAN_DELAY = 2.0
TAKE_PER_SCAN = 5
FORCE_BUY_ON_FIRST_PASS = True

MIN_1MOMENTUM_PCT = -10.0
MIN_DAY_PCT = -10.0

DOLLARS_PER_TRADE = 75
MAX_OPEN_POSITIONS = 15

USE_EXTENDED_HOURS = True
LIMIT_SLIPPAGE_BPS = 15
TRAIL_PERCENT = 3.0
TIME_EXIT_MINUTES = 7

ALPACA_BROKER_BASE = "https://paper-api.alpaca.markets"
