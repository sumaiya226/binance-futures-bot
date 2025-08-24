from .config import settings
from .utils import setup_logger, validate_side, validate_positive_float
from .binance_client import build_um_futures_client

def place_market_order(symbol: str, side: str, qty: float):
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    qty = validate_positive_float("qty", qty)
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)
    logger.info(f"Placing MARKET order: {symbol} {side} {qty}")
    try:
        resp = client.new_order(symbol=symbol, side=side, type="MARKET", quantity=qty)
        logger.info(f"API Response: {resp}")
        return resp
    except Exception as e:
        logger.exception("Market order failed")
        raise
