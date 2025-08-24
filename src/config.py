from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    api_key: str = os.getenv("BINANCE_API_KEY", "")
    api_secret: str = os.getenv("BINANCE_API_SECRET", "")
    use_testnet: bool = os.getenv("USE_TESTNET", "true").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    default_symbol: str = os.getenv("DEFAULT_SYMBOL", "BTCUSDT")

settings = Settings()
