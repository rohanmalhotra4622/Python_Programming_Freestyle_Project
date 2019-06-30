


#from pandas.io.data import DataReader
#pip install pandas-datareader
import os
import sys
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime , date, time, timedelta
import matplotlib.pyplot as plt


#url  = r'C:\Users\Rohan Malhotra\Documents\GitHub\Python_Programming_Freestyle_Project\stats.xlsx'
portfolio_url = os.path.join(os.path.dirname(__file__),  "portfolio.csv")
combined_portfolio_url = os.path.join(os.path.dirname(__file__),  "combined_portfolio.csv")
percent_change_url = os.path.join(os.path.dirname(__file__),  "percent_changes.csv")
correlations_url = os.path.join(os.path.dirname(__file__),  "correlation.csv")
stats_url = os.path.join(os.path.dirname(__file__),  "stats.csv")
'''
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
'''
portfolio = []
dic = {}
while True:
    try:
        selected_id = input("Please enter stock: " ).upper()
        if type(selected_id) == str:
            portfolio.append(selected_id)
        if selected_id == 'DONE' or selected_id == 'done':
            break
        else:
            total_shares = int(input("please enter number of shares:"))
            dic.update({selected_id : total_shares})
    except ValueError:
        print('Entry seems invalid; Please try again:')
        sys.exit()

portfolio = portfolio[:-1]


end_date = datetime.today()
beg_date = end_date - timedelta(365)

# Define the Index, this should be the benchmark we want to compare against.  
print('---------------------------------------------------------')
#sp500 = pdr.get_data_yahoo(symbols='^gspc', start=datetime(2019, 5, 10), end=datetime(2019, 6, 24))
sp500 = pdr.get_data_yahoo(symbols='^gspc', start=beg_date , end=end_date)
#sp500 = sp500[[ 'Open','Adj Close']]
sp500 = sp500['Adj Close']
sp500 = pd.DataFrame(sp500).reset_index()
sp500.columns = ['Date','SP500']
sp500 = sp500.round(2)
#sp500 = sp500.rename(columns={ 'Open' : 'SP500-Open'  , 'Adj Close':'SP500-Close'})
#sp500 = sp500.rename(columns={ 'Adj Close':'SP500-Close'})
#sp500 = sp500.reset_index()
#print(sp500)

print('---------------------------------------------------------')
print('MY PORTFOLIO')
# Convert portfolio, which is a list into a dataframe

#df = pd.DataFrame({'Ticker':portfolio} )
my_portfolio = pdr.get_data_yahoo(portfolio, start=beg_date, end=end_date)
my_portfolio = my_portfolio['Adj Close'].reset_index()
my_portfolio = my_portfolio.round(2)
print(my_portfolio)
my_portfolio.to_csv(portfolio_url)
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
combined_df.to_csv(combined_portfolio_url)
print('---------------------------------------------------------')



# Calculate Daily Percent Returns
pct_change = combined_df.pct_change()
print('Daily % Change')
pct_change.to_csv(percent_change_url)
print(pct_change)

print('---------------------------------------------------------')

#jpm_percent = jpm.pct_change()  # calculate percent change
#print(jpm_percent)
#sp500_percent = sp500.pct_change()  # calculate percent change
#print(sp500_percent)

#### charting`````

print('CORRELATIONS BASED ON DAILY CLOSING PRICES')
print(combined_df.corr().round(2))
combined_df.corr().round(2).to_csv(correlations_url)
print('---------------------------------------------------------')

print('STATISTICS BASED ON DAILY PERCENT CHANGES')
stats = pct_change.describe()
stats = stats.rename(index={ 'std' : 'STD_DEV'  })
print(stats)
stats.to_csv(stats_url)

## select most and least volatile stocks
std_dev = stats.loc['STD_DEV']
most_volatile=std_dev.sort_values( ascending= False)
#most_volatile = most_volatile.head(5)
most_volatile_stock= most_volatile.index[0]
least_volatile_stock= most_volatile.index[-1]






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

# Create a dictionary of stock symbol as keys and total in dollar amount as values
value_stocks = {}
#print(list(dic.keys()))
#print(len(list(dic.keys())))
for i in list(dic.keys()):
    value_stocks.update({i: int(dic[i]) * my_portfolio[i].iloc[-1] })


## Create Pie Chart showing value by percent owned
# my_portfolio['jpm'].iloc[-1]
ex = [0.1 for i in range(len(list(value_stocks.keys())))]
#ex = []
#for q in range(len(list(value_stocks.keys()))):
#    ex.append(q/10)
explode = tuple(ex)
#print(explode)

labels = list(value_stocks.keys())
sizes = list(value_stocks.values())
explode
#plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=40)
plt.title('% Stock Values' , bbox={'facecolor':'0.5', 'pad':4} , fontsize = 14 )
plt.pie(sizes, explode = explode ,labels = labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
#breakpoint()




# Time Series Line Graph for percent changes


print('---------------------------------------------------------')
fig , ax = plt.subplots()
pct_change.plot(ax=ax)
ax.legend(loc = 'best')
ax.set_title('Percent Daily Returns' , fontsize = 24 , loc = 'left')
ax.set_ylabel('Percent Change',color='red',fontsize=16)
ax.set_xlabel('Date',color='red',fontsize=16)
ax.tick_params(axis='x',labelcolor='blue')
ax.tick_params(axis='y',labelcolor='blue')
#ax.ticklabel_format(useOffset = False)
plt.show()

breakpoint()

print('hello')





