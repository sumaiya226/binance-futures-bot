from ..config import settings
from ..utils import setup_logger, validate_side, validate_positive_float
from ..binance_client import build_um_futures_client

def place_oco(symbol: str, side: str, qty: float, take_profit: float, stop: float, stop_limit: float, tif: str = "GTC"):
    """
    Simulated OCO for Futures using two conditional orders:
      - Take-profit limit
      - Stop order (with stop-limit price)
    The first to trigger *should* cancel the other. This implementation places both and
    logs orderIds so you can manage cancels (simple approach).
    """
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    qty = validate_positive_float("qty", qty)
    take_profit = validate_positive_float("take_profit", take_profit)
    stop = validate_positive_float("stop", stop)
    stop_limit = validate_positive_float("stop_limit", stop_limit)
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)

    # Place TP
    logger.info(f"Placing TAKE-PROFIT LIMIT: {symbol} {side} {qty} @ {take_profit}")
    tp = client.new_order(symbol=symbol, side=side, type="TAKE_PROFIT",
                          quantity=qty, price=take_profit, stopPrice=take_profit, timeInForce=tif)

    # Place SL
    logger.info(f"Placing STOP LIMIT: {symbol} {side} {qty} stop={stop} limit={stop_limit}")
    sl = client.new_order(symbol=symbol, side=side, type="STOP",
                          quantity=qty, price=stop_limit, stopPrice=stop, timeInForce=tif)

    logger.info(f"OCO pair placed: take_profit_orderId={tp.get('orderId')} stop_orderId={sl.get('orderId')}")
    return {"take_profit": tp, "stop": sl}
