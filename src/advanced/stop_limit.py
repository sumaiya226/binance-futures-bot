from ..config import settings
from ..utils import setup_logger, validate_side, validate_positive_float
from ..binance_client import build_um_futures_client

def place_stop_limit(symbol: str, side: str, qty: float, stop: float, limit_price: float, tif: str = "GTC"):
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    qty = validate_positive_float("qty", qty)
    stop = validate_positive_float("stop", stop)
    limit_price = validate_positive_float("limit", limit_price)
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)
    logger.info(f"Placing STOP-LIMIT: {symbol} {side} {qty} stop={stop} limit={limit_price}")
    try:
        resp = client.new_order(symbol=symbol, side=side, type="STOP",
                                quantity=qty, price=limit_price, stopPrice=stop, timeInForce=tif)
        logger.info(f"API Response: {resp}")
        return resp
    except Exception as e:
        logger.exception("Stop-limit failed")
        raise
