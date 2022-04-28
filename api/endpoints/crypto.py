from typing import Optional

import requests
from fastapi import APIRouter

router = APIRouter()


@router.get("/prices/{crypto}")
async def get_real_time_prices(crypto: str, currency: Optional[str] = "USD"):
    """Get real-time price for the selected cryptocurrency in the currency of your choice"""

    r = requests.get(
        f"https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms={currency}"
    )
    data = r.json()
    return data


@router.get("/trading/{crypto}")
async def get_trading_signals(crypto: str):
    """Get market sentiment:
    * if bullish, prices are expected to rise - optimistic
    * if bearish, prices are expected to fall - pessimistic"""

    r = requests.get(
        f"https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym={crypto}"
    )
    data = r.json()
    trading_signals = data["Data"]
    return trading_signals
