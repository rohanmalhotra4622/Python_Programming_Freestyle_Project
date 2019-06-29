


#from pandas.io.data import DataReader
#print(ibm['Adj Close'])

#pip install pandas-datareader
import sys
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime , date, time, timedelta
import matplotlib.pyplot as plt

portfolio = []
while True:
    try:
        #if isinstance(int(selected_id) , int):
            #sys.exit()
        selected_id = input("Please enter stock: " )
        if type(selected_id) == str:
            portfolio.append(selected_id)
        if selected_id == 'DONE' or selected_id == 'done':
            break
    except ValueError:
        print('Entry seems invalid; Please try again:')
        sys.exit()

portfolio = portfolio[:-1]

#my_portfolio = []
#for i in portfolio:
#    if isinstance(int(i) , int):
#        my_portfolio.append(i)
#if isinstance(int(symbol) , int):
        #sys.exit()
#stock1 = input("Please enter stock: ")
#stock2 = input("Please enter stock: ")

end_date = datetime.today()
beg_date = end_date - timedelta(20)

# Define the Index, this should be the benchmark we want to compare against.  
print('---------------------------------------------------------')
#sp500 = pdr.get_data_yahoo(symbols='^gspc', start=datetime(2019, 5, 10), end=datetime(2019, 6, 24))
sp500 = pdr.get_data_yahoo(symbols='^gspc', start=beg_date , end=end_date)
#sp500 = sp500[[ 'Open','Adj Close']]
sp500 = sp500['Adj Close']
sp500 = pd.DataFrame(sp500).reset_index()
sp500.columns = ['Date','sp500']

#sp500 = sp500.rename(columns={ 'Open' : 'SP500-Open'  , 'Adj Close':'SP500-Close'})
#sp500 = sp500.rename(columns={ 'Adj Close':'SP500-Close'})
#sp500 = sp500.reset_index()
#print(sp500)

print('---------------------------------------------------------')
print('MY PORTFOLIO')
# Convert portfolio, which is a list into a dataframe

df = pd.DataFrame({'Ticker':portfolio} )
my_portfolio = pdr.get_data_yahoo(portfolio, start=beg_date, end=end_date)
my_portfolio = my_portfolio['Adj Close'].reset_index()

print(my_portfolio)
print('---------------------------------------------------------')

#jpm = pdr.get_data_yahoo(symbols=stock1, start=datetime(2019, 4, 10), end=datetime(2019, 6, 24))
#jpm = pdr.get_data_yahoo(symbols=stock1, start=beg_date , end=end_date)
#breakpoint()
##Index(['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], dtype='object')
#jpm = jpm[[ 'Open','Adj Close']]
##jpm = jpm.rename(columns={ 'Open' : 'JPM-Open'  , 'Adj Close':'JPM-Close'})
#jpm = jpm.rename(columns={ 'Open' : str(stock1).upper() + ' Open' , 'Adj Close': str(stock1).upper() + ' Close'})
#jpm = jpm.reset_index()
#print(jpm)




# Merge the  dataframes
print('MY PORTFOLIO vs. SP500')
combined_df = sp500.merge(my_portfolio, left_on='Date',right_on= 'Date', how='inner' )
#js = jpm_sp500[['Date' , 'SP500-Close' , 'JPM-Close']]
combined_df = combined_df.set_index('Date')

#js = jpm_sp500[['Date' , 'SP500-Close' , str(stock1).upper() + ' Close']]
#js = js.set_index('Date')
print(combined_df)
print('---------------------------------------------------------')



# Calculate Daily Percent Returns
pct_change = combined_df.pct_change()
print('Daily % Change')
print(pct_change)

print('---------------------------------------------------------')

stats = pct_change.describe()

#jpm_percent = jpm.pct_change()  # calculate percent change
#print(jpm_percent)
#sp500_percent = sp500.pct_change()  # calculate percent change
#print(sp500_percent)

#### charting`````

print('CORRELATIONS BASED ON DAILY CLOSING PRICES')
print(combined_df.corr())
print('---------------------------------------------------------')

print('STATISTICS BASED ON DAILY PERCENT CHANGES')
stats = pct_change.describe()
stats = stats.rename(index={ 'std' : 'STD_DEV'  })
std_dev = stats.loc['STD_DEV']

#most_volatile=New_DF[['Overall_Score']]
most_volatile=std_dev.sort_values( ascending= False)
#most_volatile = most_volatile.head(5)
most_volatile_stock= most_volatile.index[0]
least_volatile_stock= most_volatile.index[-1]
#most_volatile=most_volatile.sort_index(ascending=True)
#y=most_volatile[most_volatile['Overall_Score']== Best_Player['Overall_Score'].max()].index[0]
#y




#std_dev.rename("STD_DEV.")

fig, ax = plt.subplots()
std_dev.plot(ax=ax, kind='barh',figsize=(6,4), width=.25, color='blue')
ax.set_title('Highest Volatility', fontsize=20, loc='left')
ax.set_ylabel('Stock Ticker',color='red',fontsize=16)
ax.set_xlabel('Daily Standard Deviation',color='red',fontsize=16)
#ax.set_xlim(0,4)                 
ax.tick_params(axis='x',labelcolor='blue')
ax.tick_params(axis='y',labelcolor='blue')
ax.legend(loc='best')
ax.get_children()[list(std_dev.index).index(most_volatile_stock)].set_color('orange')
ax.get_children()[list(std_dev.index).index(least_volatile_stock)].set_color('red')
plt.show()



breakpoint()
print('---------------------------------------------------------')
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








