import logging, sys, time
from logging.handlers import RotatingFileHandler
from typing import Optional

def setup_logger(level: str = "INFO", log_file: str = "bot.log") -> logging.Logger:
    logger = logging.getLogger("binance_bot")
    if logger.handlers:
        return logger
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    fh = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    fh.setFormatter(fmt)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def validate_side(side: str) -> str:
    s = side.upper()
    if s not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")
    return s

def validate_positive_float(name: str, v: float) -> float:
    try:
        v = float(v)
    except Exception:
        raise ValueError(f"{name} must be a number")
    if v <= 0:
        raise ValueError(f"{name} must be > 0")
    return v

def sleep_seconds(seconds: int, logger: Optional[logging.Logger] = None):
    if logger:
        logger.info(f"Sleeping {seconds}s...")
    time.sleep(seconds)
