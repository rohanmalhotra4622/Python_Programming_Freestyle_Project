# Python_Programming_Freestyle_Project

INSTALLATION:

Depending upon their set up environment, the user may  need to install certain packages.  Please check the documentation for each to install the latest version.  For example, for the pandas_datareader, the installation instructions are given below. The packages used are as follows:

# pip install pandas-datareader.

1. pandas: To work with DataFrames

2.  pandas_DataReader: To extract information from Yahoo Finance

3.  statsmodels: To perform regression analysis 

4. matplotlib: To create plots and graphs

The modules that need to be imported are as follows:

1. datetime: to define the time period for pulling the data
2. os: to write .csv files for the data produced so people can see the raw data if they so please
3. sys: for validation purposes and exiting the system if non integers are entered for number of shares owned
4. timedelta: perform additions and subtractions to determine time range

EXECUTING THE CODE:

To execute the code the user needs to enter the following command after installation is set up:

python stocks.py


PROCESS/GOAL


The goal of this project is to extract stock information from Yahoo Finance and run some analytics to help the user make informed decisions to better manage their investments.  

The user will be required to enter the stocks and the number of shares that they own.  When the user is finished entering the portfolio, they should use 'done' or 'DONE' to see the results.  The code starts of with an empty dictionary labeled 'dic' that will be updated with the 'stock names' as 'keys' and the 'number of shares' as 'values'.  In addition,  there is also an empty list labeled 'portfolio' that will be appended when we enter the stock names.  

The range for which the data is pulled is for the last one year.  The user has the ability to change this time period. I have set the variable 'end_date'  as todays date and the variable 'beg_date' with a timedelta of the previous 365 days.  The user can change this beggining date value by inputting a different value in the 'beg_date' variable.

We want to compare our portfolio aginst the S&P 500 index, since that is considered a diversified portfolio.  The code will pull the data for the SP500 index and our portfolio of stocks inputted. Several varibales and dataframes will be created that are mentioned below.  

1) portfolio --> initially an empty list that gets appended based on inputs

2) dic --> initially an empty dictionary that gets updated based on inputs

3) end_date --> todays date

4) beg_date --> end_date - timedelta(365)

5) my_portfolio --> this is a DF of the stocks we input for the time range choosing only the Adj. Close Column.

6) combined_df --> this is a DF that has the same contents as the DF above along with the SP500 values.  This is done by merging the SP500 values retrieved  with our stock portfolio values.

7) pct_change --> this is DF of percent changes of the combined_df listed in the line above.  This is our measure of volatility.

8) corr --> this is a DF of correlations based on daily closing prices, and the not the percent changes of all the stocks in the portfolio with each other and the SP500

9) corr_1 --> correlation of all the stocks vs. the SP500 only. This can be used to create a separate plot if user chooses.

10) stats --> this is a DF based on daily percent changes and displays key statistical measures.

11) std_dev -->  this is a series, which can be thought of as a one column DF that has been extracted from the stats DF.  We sort the values in this series to identify  the most and least volatile stocks so we can display those with more transparency  in the plots. The std_dev is finally annualized in percentage terms so it is easy to understand.  

12) value_stocks -->  this is another empty dictionary that gets updated to reflect the 'stock names' as 'keys' and the  '(shares owned * last stock prices)' as 'values'.  

13) ex --> this is a list comprehension that gives the magnitude by which we want the pies to explode in the pie chart. This is needed to make the code dynamic.  

14) explode --> Converting the list 'ex' above into a tuple to be used in code for creating the pie chart.

15) most_volatile_stock --> self explanatory. 

16) least_volatile_stock --> self explanatory.

17) least_correlated_stock --> self explanatory.

Create a bar chart of the volatility of the stocks and color the  most and least volatile stocks differently from the rest.  This is done based on the std_dev series that was extracted from stats.

Create a pie chart displaying the values of stocks owned in percentage terms.  I also made the pie pieces explode to better visualize the data. 

Create subplots of line graphs based on 'pct_changes' to show volatility over time.  The sub plots are important because if we have more than two stocks, the graph will be very cluttered. I have kept the axis to be of the same magnitude to better make sense of the visualizations.

There is also a Bar chart displaying the correlations of all the stocks to the SP500 and to each other.

The last step is a regression analysis of the most volatile stock against the SP500.  This could be a very useful tool for specific users.

Finally, the DataFrames created are also saved as .csv files in the same location where the code is located. This will help the user if they want to look at the raw data.













