# Binance USDT-M Futures Order Bot (CLI)

A CLI-based trading bot for **Binance USDT-M Futures** supporting market and limit orders (core) plus stop-limit, OCO, TWAP, and Grid strategies (advanced).  
Built for macOS + VS Code users with step-by-step instructions.

> ⚠️ **Risk Disclaimer**: Crypto derivatives are risky. Use the **testnet** first. You are responsible for your API keys and trades.

---

## Features
- **Core Orders**: Market, Limit
- **Advanced**: Stop-Limit, OCO, TWAP, Grid
- **Validation** of symbol, side, quantity, price thresholds
- **Structured logging** to `bot.log` with timestamps + error traces
- **.env-based config** (no hardcoding secrets)
- **Testnet toggle** for safe dry runs
- **Reproducible CLI**: documented commands

---

## Prerequisites (macOS + VS Code)

1. Install Python 3.10+ (check with `python3 --version`).
2. Open **VS Code** → `File > Open` → select this project folder.
3. Open a **VS Code Terminal**: `Terminal > New Terminal`.

### Create & activate a virtual environment
```bash
# Inside VS Code terminal (recommended), or macOS Terminal
python3 -m venv .venv
source .venv/bin/activate  # (macOS/Linux)
# If it shows (venv) in your prompt, you're good.
```

### Install dependencies
```bash
pip install --upgrade pip
pip install binance-futures-connector python-dotenv pydantic rich reportlab
```

> If you prefer the official `binance-connector`, the UMFutures class is similar. This project uses `binance-futures-connector` explicitly.

---

## Set up API Keys
1. Copy `.env.example` to `.env` and fill in your keys.
2. Start with **testnet** enabled.

```
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
USE_TESTNET=true
LOG_LEVEL=INFO
DEFAULT_SYMBOL=BTCUSDT
```

**Get testnet futures keys** from Binance Futures Testnet.

---

## How to Run

All commands are run **from the project root** (where `src/` lives). Make sure your virtualenv is **activated**.

### 1) Market order
```bash
python3 src/cli.py market BTCUSDT BUY --qty 0.001
```

### 2) Limit order
```bash
python3 src/cli.py limit BTCUSDT SELL --qty 0.001 --price 75000
```

### 3) Stop-Limit (advanced)
```bash
python3 src/cli.py stop-limit BTCUSDT SELL --qty 0.001 --stop 74000 --limit 73950
```

### 4) OCO (advanced)
```bash
python3 src/cli.py oco BTCUSDT SELL --qty 0.001 --take-profit 78000 --stop 74000 --stop-limit 73950
```

### 5) TWAP (advanced)
Split a large order into slices over time:
```bash
python3 src/cli.py twap BTCUSDT BUY --qty 0.01 --slices 5 --interval 10
```
This places 5 market orders of equal size every 10 seconds.

### 6) Grid (advanced)
Automated buy-low/sell-high within a range:
```bash
python3 src/cli.py grid BTCUSDT BUY --lower 72000 --upper 78000 --grids 6 --qty 0.001
```
This places alternating limit orders across 6 grid levels.

---

## Project Structure
```
[project_root]/
├── src/
│   ├── cli.py
│   ├── binance_client.py
│   ├── config.py
│   ├── utils.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   └── advanced/
│       ├── stop_limit.py
│       ├── oco.py
│       ├── twap.py
│       └── grid.py
├── .env.example
├── bot.log
├── report.pdf
└── README.md
```

---

## Notes
- **Paper/Test Mode**: With `USE_TESTNET=true`, orders go to Binance **UM Futures Testnet**.
- Logging is in `bot.log`; errors + API responses are captured.
- If an order fails validation, it’s rejected before reaching the exchange.
- For screenshots + explanation, see `report.pdf`.

---

## Troubleshooting
- `ModuleNotFoundError`: Activate venv, reinstall packages.
- `-2019 / -1021` errors: API key/secret or timestamp issue; ensure correct Testnet keys and system time is synced.
- SYMBOL precision errors: The exchange enforces lot/price filters. Adjust qty/price to valid increments.

---

## Example Development Flow in VS Code
1. Open folder; create `.env`.
2. Create & activate venv.
3. Install deps.
4. Test with **market** command on testnet.
5. Inspect `bot.log`.
6. Move on to **limit**, then **advanced** orders.
7. Commit and push to a **private GitHub repo** named `yourname-binance-bot` and add your reviewer.

---

## License
MIT (for the sample code in this assignment).
