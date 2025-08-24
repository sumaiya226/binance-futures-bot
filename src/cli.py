import argparse
from rich import print
from .market_orders import place_market_order
from .limit_orders import place_limit_order
from .advanced.stop_limit import place_stop_limit
from .advanced.oco import place_oco
from .advanced.twap import place_twap
from .advanced.grid import place_grid

def main():
    parser = argparse.ArgumentParser(description="Binance USDT-M Futures Bot (CLI)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_m = sub.add_parser("market", help="Place a market order")
    p_m.add_argument("symbol")
    p_m.add_argument("side", choices=["BUY", "SELL"])
    p_m.add_argument("--qty", required=True, type=float)

    p_l = sub.add_parser("limit", help="Place a limit order")
    p_l.add_argument("symbol")
    p_l.add_argument("side", choices=["BUY", "SELL"])
    p_l.add_argument("--qty", required=True, type=float)
    p_l.add_argument("--price", required=True, type=float)
    p_l.add_argument("--tif", default="GTC")

    p_sl = sub.add_parser("stop-limit", help="Place a stop-limit order")
    p_sl.add_argument("symbol")
    p_sl.add_argument("side", choices=["BUY", "SELL"])
    p_sl.add_argument("--qty", required=True, type=float)
    p_sl.add_argument("--stop", required=True, type=float)
    p_sl.add_argument("--limit", required=True, type=float)
    p_sl.add_argument("--tif", default="GTC")

    p_oco = sub.add_parser("oco", help="Place a simulated OCO (TP + SL)")
    p_oco.add_argument("symbol")
    p_oco.add_argument("side", choices=["BUY", "SELL"])
    p_oco.add_argument("--qty", required=True, type=float)
    p_oco.add_argument("--take-profit", required=True, type=float)
    p_oco.add_argument("--stop", required=True, type=float)
    p_oco.add_argument("--stop-limit", required=True, type=float)
    p_oco.add_argument("--tif", default="GTC")

    p_twap = sub.add_parser("twap", help="Split a big order into smaller slices over time (market)")
    p_twap.add_argument("symbol")
    p_twap.add_argument("side", choices=["BUY", "SELL"])
    p_twap.add_argument("--qty", required=True, type=float)
    p_twap.add_argument("--slices", required=True, type=int)
    p_twap.add_argument("--interval", required=True, type=int, help="Seconds between slices")

    p_grid = sub.add_parser("grid", help="Place multiple limit orders within a price range")
    p_grid.add_argument("symbol")
    p_grid.add_argument("side", choices=["BUY", "SELL"])
    p_grid.add_argument("--lower", required=True, type=float)
    p_grid.add_argument("--upper", required=True, type=float)
    p_grid.add_argument("--grids", required=True, type=int)
    p_grid.add_argument("--qty", required=True, type=float)
    p_grid.add_argument("--tif", default="GTC")

    args = parser.parse_args()

    if args.cmd == "market":
        print(place_market_order(args.symbol, args.side, args.qty))
    elif args.cmd == "limit":
        print(place_limit_order(args.symbol, args.side, args.qty, args.price, args.tif))
    elif args.cmd == "stop-limit":
        print(place_stop_limit(args.symbol, args.side, args.qty, args.stop, args.limit, args.tif))
    elif args.cmd == "oco":
        print(place_oco(args.symbol, args.side, args.qty, args.take_profit, args.stop, args.stop_limit, args.tif))
    elif args.cmd == "twap":
        print(place_twap(args.symbol, args.side, args.qty, args.slices, args.interval))
    elif args.cmd == "grid":
        print(place_grid(args.symbol, args.side, args.lower, args.upper, args.grids, args.qty, args.tif))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
