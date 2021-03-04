import seaborn as sns
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

#Import commodity prices
gold_prices = pd.read_csv('gold_prices.csv')

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')

#Create datetimes
start = datetime(1999, 1,1)
end = datetime(2019, 1,1)
