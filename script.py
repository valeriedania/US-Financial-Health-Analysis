import seaborn as sns
import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb 
from datetime import datetime

#Import commodity prices
gold_prices = pd.read_csv('gold_prices.csv')

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')

#Create datetimes
start = datetime(1999, 1,1)
end = datetime(2019, 1,1)

#Use web.DataReader to get historical prices
nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)

#Get S&P data
sap_data = web.DataReader(“SP500”, “fred”, start, end)

#Import GDP data from World Bank API
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country['US'], start=start, end=end)
