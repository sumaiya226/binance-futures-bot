from ..config import settings
from ..utils import setup_logger, validate_side, validate_positive_float
from ..binance_client import build_um_futures_client

def place_grid(symbol: str, side: str, lower: float, upper: float, grids: int, qty: float, tif: str = "GTC"):
    logger = setup_logger(settings.log_level)
    side = validate_side(side)
    lower = validate_positive_float("lower", lower)
    upper = validate_positive_float("upper", upper)
    grids = int(validate_positive_float("grids", grids))
    qty = validate_positive_float("qty", qty)
    if lower >= upper:
        raise ValueError("lower must be < upper")
    client = build_um_futures_client(settings.api_key, settings.api_secret, settings.use_testnet)

    step = (upper - lower) / (grids - 1)
    prices = [round(lower + i * step, 2) for i in range(grids)]  # round for readability
    logger.info(f"GRID {symbol} {side}: {grids} levels from {lower}..{upper}: {prices}")

    orders = []
    for i, p in enumerate(prices):
        try:
            resp = client.new_order(symbol=symbol, side=side, type="LIMIT",
                                    quantity=qty, price=p, timeInForce=tif)
            logger.info(f"Grid order {i+1}/{grids} @ {p}: {resp}")
            orders.append(resp)
        except Exception:
            logger.exception(f"Grid order at {p} failed")
            raise
    return orders
