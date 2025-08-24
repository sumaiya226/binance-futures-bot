from .config import settings
from .utils import setup_logger, validate_side, validate_positive_float
from .binance_client import build_um_futures_client

def place_limit_order(symbol: str, side: str, qty: float, price: float, tif: str = "GTC"):
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    qty = validate_positive_float("qty", qty)
    price = validate_positive_float("price", price)
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)
    logger.info(f"Placing LIMIT order: {symbol} {side} {qty} @ {price} ({tif})")
    try:
        resp = client.new_order(symbol=symbol, side=side, type="LIMIT",
                                quantity=qty, price=price, timeInForce=tif)
        logger.info(f"API Response: {resp}")
        return resp
    except Exception as e:
        logger.exception("Limit order failed")
        raise
