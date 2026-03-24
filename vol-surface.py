import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt

expiration_date = dt.today()
ticker = 'WCP.TO'

asset = yf.Ticker(ticker)
option_expirations = asset.options
