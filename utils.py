from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd


def yf_download(symbols):

    interval = "1h"
    start = datetime.now() - timedelta(days = 729)
    end = datetime.now()

    data = {}
    for symbol in symbols:
        print(f"Downloading: {symbol}")
        data[symbol] = yf.download(
            symbol,
            start=start,
            end=end,
            interval=interval
        )

    dfs = []
    for symbol, df in data.items():
        symbol = symbol.replace("^", "")
        df.columns = [f"{symbol}_{col}" for col in df.columns]
        dfs.append(df)
    return pd.concat(dfs, axis=1)
