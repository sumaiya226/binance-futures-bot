import math
from ..config import settings
from ..utils import setup_logger, validate_side, validate_positive_float, sleep_seconds
from ..binance_client import build_um_futures_client

def place_twap(symbol: str, side: str, qty: float, slices: int, interval: int):
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    qty = validate_positive_float("qty", qty)
    slices = int(validate_positive_float("slices", slices))
    interval = int(validate_positive_float("interval", interval))
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)

    slice_qty = round(qty / slices, 8)
    logger.info(f"TWAP: {slices} slices of {slice_qty} every {interval}s for {symbol} {side} total {qty}")
    results = []
    for i in range(slices):
        logger.info(f"TWAP slice {i+1}/{slices}")
        try:
            resp = client.new_order(symbol=symbol, side=side, type="MARKET", quantity=slice_qty)
            logger.info(f"API Response: {resp}")
            results.append(resp)
        except Exception:
            logger.exception("TWAP slice failed")
            raise
        if i < slices - 1:
            sleep_seconds(interval, logger)
    return results
