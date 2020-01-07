import datetime
import pandas_datareader.data as web
import pandas_datareader.wb

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("YESBANK", 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())
