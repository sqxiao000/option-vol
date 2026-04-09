import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def volatility_surface(ticker, expiration_date):
    asset = yf.Ticker(ticker)
    options = asset.option_chain(expiration_date.strftime('%Y-%m-%d'))
    calls = options.calls
    puts = options.puts
    
    data = []
    ticker_name = asset.info.get('shortName', ticker)  # Use ticker as fallback
    
    for _, row in calls.iterrows():
        data.append({'Strike': row['strike'], 'Expiration': expiration_date.strftime('%Y-%m-%d'), 'Implied Volatility': row['impliedVolatility']})
    
    for _, row in puts.iterrows():
        data.append({'Strike': row['strike'], 'Expiration': expiration_date.strftime('%Y-%m-%d'), 'Implied Volatility': row['impliedVolatility']})
    
    vol_surface = pd.DataFrame(data)
    return vol_surface, ticker_name


def plot_volatility_surface(vol_surface, ticker_name):
    # Sort by strike for a connected plot
    vol_surface = vol_surface.sort_values('Strike')
    
    strikes = vol_surface['Strike']
    implied_vols = vol_surface['Implied Volatility']
    
    plt.figure(figsize=(10, 6))
    plt.plot(strikes, implied_vols, marker='o', linestyle='-', color='blue')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility')
    plt.title(f'Implied Volatility vs Strike for {ticker_name} (Expiration: {vol_surface["Expiration"].iloc[0]})')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    ticker = input("Please enter ticker: ")
    expiration_date = input("Please enter expiration date (YYYY-MM-DD). Press Enter to use default (last business day): ")
    if expiration_date == "" or not expiration_date:
        expiration_date = yf.Ticker(ticker).options[-1]  # Use the last available expiration date
    expiration_date = pd.to_datetime(expiration_date)

    vol_surface, ticker_name = volatility_surface(ticker, expiration_date)
    plot_volatility_surface(vol_surface, ticker_name)