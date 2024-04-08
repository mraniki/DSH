"""
DXSP Example
"""

import asyncio

from dxsp import DexSwap


async def main():
    dex = DexSwap()
    # symbol = "LINK"
    symbol = "0x514910771af9ca656af840dff83e8264ecf986ca"

    quote = await dex.get_quotes(symbol)
    print("quote ", quote)
    # quote  🦄 29761.19589 USDT

    # # BUY 10 USDC to SWAP with BITCOIN
    # tx = await dex.execute_order('USDT','BTC',10)
    # print("tx ", tx)


if __name__ == "__main__":
    asyncio.run(main())
