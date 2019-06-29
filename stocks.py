


#from pandas.io.data import DataReader
#print(ibm['Adj Close'])

#pip install pandas-datareader

import pandas as pd
import pandas_datareader as pdr
from datetime import datetime , date, time, timedelta
import matplotlib.pyplot as plt

stock1 = input("Please enter stock: ")
#stock2 = input("Please enter stock: ")

end_date = datetime.today()
beg_date = end_date - timedelta(50)


#jpm = pdr.get_data_yahoo(symbols=stock1, start=datetime(2019, 4, 10), end=datetime(2019, 6, 24))
jpm = pdr.get_data_yahoo(symbols=stock1, start=beg_date , end=end_date)
#Index(['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], dtype='object')
jpm = jpm[[ 'Open','Adj Close']]
#jpm = jpm.rename(columns={ 'Open' : 'JPM-Open'  , 'Adj Close':'JPM-Close'})
jpm = jpm.rename(columns={ 'Open' : str(stock1).upper() + ' Open' , 'Adj Close': str(stock1).upper() + ' Close'})
jpm = jpm.reset_index()
print(jpm)



# Define Index, this should be constantthe benchmark we want to compare against
print('---------------------------------------------------------')
#sp500 = pdr.get_data_yahoo(symbols='^gspc', start=datetime(2019, 5, 10), end=datetime(2019, 6, 24))
sp500 = pdr.get_data_yahoo(symbols='^gspc', start=beg_date , end=end_date)
sp500 = sp500[[ 'Open','Adj Close']]
sp500 = sp500.rename(columns={ 'Open' : 'SP500-Open'  , 'Adj Close':'SP500-Close'})
sp500 = sp500.reset_index()
print(sp500)

print('---------------------------------------------------------')
# Merge the  dataframes

jpm_sp500 = sp500.merge(jpm, left_on='Date',right_on= 'Date', how='inner' )
#js = jpm_sp500[['Date' , 'SP500-Close' , 'JPM-Close']]
js = jpm_sp500[['Date' , 'SP500-Close' , str(stock1).upper() + ' Close']]
js = js.set_index('Date')
print(js)
print('---------------------------------------------------------')



# Calculate Daily Percent Returns
pct_change = js.pct_change()
print(pct_change)

#breakpoint()

#jpm_percent = jpm.pct_change()  # calculate percent change
#print(jpm_percent)
#sp500_percent = sp500.pct_change()  # calculate percent change
#print(sp500_percent)

#### charting`````


print(js.corr())

fig , ax = plt.subplots()
pct_change.plot(ax=ax)
ax.legend(loc = 'best')
ax.set_title('Percent Daily Returns' , fontsize = 24 , loc = 'left')
#ax.ticklabel_format(useOffset = False)
plt.show()
#
#
#fig , ax = plt.subplots()
#js.plot(ax=ax)
#ax.legend(loc = 'best')
#ax.set_title('GDP Data' , fontsize = 24 , loc = 'left')
##ax.ticklabel_format(useOffset = False)
#plt.show()

#### charting`````


#print(jpm_sp500)
#print("That's cool!!")








