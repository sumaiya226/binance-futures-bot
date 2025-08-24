import logging
from binance.um_futures import UMFutures

TESTNET_URL = "https://testnet.binancefuture.com"

def build_um_futures_client(api_key: str, api_secret: str, use_testnet: bool) -> UMFutures:
    if use_testnet:
        return UMFutures(key=api_key, secret=api_secret, base_url=TESTNET_URL)
    return UMFutures(key=api_key, secret=api_secret)
