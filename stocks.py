
## Portfolio Analysis

import os
import sys
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime , date, time, timedelta
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


## Define URL's to which csv data will be posted

portfolio_url = os.path.join(os.path.dirname(__file__),   "portfolio.csv")
combined_portfolio_url = os.path.join(os.path.dirname(__file__),  "combined_portfolio.csv")
percent_change_url = os.path.join(os.path.dirname(__file__),  "percent_changes.csv")
correlations_url = os.path.join(os.path.dirname(__file__),  "correlation.csv")
stats_url = os.path.join(os.path.dirname(__file__),  "stats.csv")
#regression_url =  os.path.join(os.path.dirname(__file__),  "regression.csv")

## Create an empty list and dictionary and append/update based on data inputted. 


print('---------------------------------------------------------')
print('PORTFOLIO ANLYSIS')
print('---------------------------------------------------------')

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
            total_shares = int(input("please enter number of shares: "))
            dic.update({selected_id : total_shares})
    except ValueError:
        print('Entry seems invalid; Please try again: ')
        sys.exit()


portfolio = portfolio[:-1]


### Define time range

end_date = datetime.today()
beg_date = end_date - timedelta(365)

# Pull data for the SP500; this should be the benchmark we want to compare against.  


sp500 = pdr.get_data_yahoo(symbols='^gspc', start=beg_date , end=end_date)
sp500 = sp500['Adj Close']
sp500 = pd.DataFrame(sp500).reset_index()
sp500.columns = ['Date','SP500']
sp500 = sp500.dropna() ## drop null entries
sp500 = sp500.round(2)
print('----------------------------------------------------------------------------------')
print('Portfolio' , dic , sep = '    ')
print('----------------------------------------------------------------------------------')
print('MY PORTFOLIO')

### Pull data for our portfolio of stocks

my_portfolio = pdr.get_data_yahoo(portfolio, start=beg_date, end=end_date)
my_portfolio = my_portfolio['Adj Close'].reset_index()
my_portfolio = my_portfolio.dropna()  ## drop null entries
my_portfolio = my_portfolio.round(2)
##my_portfolio = my_portfolio.dropna(axis = 1, how = 'all')  ### 
print(my_portfolio)
my_portfolio.to_csv(portfolio_url)
print('---------------------------------------------------------')



# Merge the  dataframes

print('MY PORTFOLIO vs. SP500')
combined_df = sp500.merge(my_portfolio, left_on='Date',right_on= 'Date', how='inner' )
combined_df = combined_df.set_index('Date')
print(combined_df)
combined_df.to_csv(combined_portfolio_url)
print('---------------------------------------------------------')



# Calculate Daily Percent Returns

pct_change = combined_df.pct_change().round(6)
print('Daily % Change')
pct_change.to_csv(percent_change_url)
print(pct_change)
print('---------------------------------------------------------')

## Print Correlations based on daily closing prices

print('CORRELATIONS BASED ON DAILY CLOSING PRICES')
corr = combined_df.corr().round(4)
print(corr)
corr.to_csv(correlations_url)
print('---------------------------------------------------------')

print('STATISTICS BASED ON DAILY PERCENT CHANGES')
stats = pct_change.describe().round(5)
stats = stats.rename(index={ 'std' : 'STD_DEV'  })
print(stats)
stats.to_csv(stats_url)

## select most and least volatile stocks
std_dev = stats.loc['STD_DEV']
most_volatile = std_dev.sort_values( ascending= False)
most_volatile_stock = most_volatile.index[0]
least_volatile_stock = most_volatile.index[-1]


# Create a dictionary of stock symbol as keys and total in dollar amount as values

value_stocks = {}
for i in list(dic.keys()):
    value_stocks.update({i: int(dic[i]) * my_portfolio[i].iloc[-1] })

## Create bar chart of the volatility of the stocks and color most and least volatile differently from the rest

fig, ax = plt.subplots()
std_dev.plot(ax=ax, kind='barh',figsize=(6,4), width=.25, color='blue')
ax.set_title('Highest Volatility', fontsize=20, loc='left')
ax.set_ylabel('Stock Ticker',color='red',fontsize=16)
ax.set_xlabel('Daily Standard Deviation',color='red',fontsize=16)                
ax.tick_params(axis='x',labelcolor='blue')
ax.tick_params(axis='y',labelcolor='blue')
ax.legend(loc='best')
ax.get_children()[list(std_dev.index).index(most_volatile_stock)].set_color('orange')
ax.get_children()[list(std_dev.index).index(least_volatile_stock)].set_color('red')
plt.show()

## create pie chart 
## determine magnitude by which to explode the pie pieces.

ex = [0.1 for i in range(len(list(value_stocks.keys())))]  
explode = tuple(ex)
labels = list(value_stocks.keys())
sizes = list(value_stocks.values())
plt.title('% Stock Values' , bbox={'facecolor':'0.5', 'pad':4} , loc = 'left',fontsize = 18 )
plt.pie(sizes, explode = explode ,labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()


# Time Series Line Graph for percent changes if portfolio has two or less stocks

print('---------------------------------------------------------')
fig , ax = plt.subplots()
pct_change.plot(ax=ax , subplots = True, sharey = True , sharex = True)  # colormap = 'cubehelix'
ax.legend(loc = 'right')
plt.suptitle('Percent Daily Returns' , size = 24 , color = 'blue')
plt.show()

# Create bar graph showing correlation with the SP 500

print('---------------------------------------------------------')
corr_1 = corr['SP500']
least_correlated = corr_1.sort_values( ascending= False)
least_correlated_stock= least_correlated.index[-1]

#fig, ax = plt.subplots()
#corr_1.plot(ax=ax, kind='bar',figsize=(6,4), width=.25, color='blue')
#ax.set_title('Correlation with SP500', fontsize=20, loc='left')
#ax.set_ylabel('Correlation',color='red',fontsize=16)
#ax.set_xlabel('Stock Ticker',color='red',fontsize=16)                
#ax.tick_params(axis='x',labelcolor='blue')
#ax.tick_params(axis='y',labelcolor='blue')
#ax.legend(loc='best')
#ax.get_children()[list(corr_1.index).index(least_correlated_stock)].set_color('red')
#plt.show()
fig, ax = plt.subplots()
corr.plot(ax=ax, kind='bar')
ax.set_title('Correlation', fontsize=20, loc='left')
ax.set_ylabel('Correlation',color='red',fontsize=16)
ax.set_xlabel('Stock Ticker',color='red',fontsize=16)                
ax.tick_params(axis='x',labelcolor='blue')
ax.tick_params(axis='y',labelcolor='blue')
ax.legend(loc='best')
plt.show()




## Create regression table for the most volatile stock

reg_table = smf.ols( most_volatile_stock + ' ~ ' + 'SP500' , data=combined_df).fit().summary()
print(reg_table)

breakpoint()

print('Good luck with your Investments!!!!')





