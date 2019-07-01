# Python_Programming_Freestyle_Project

The goal of this project is to extract stock information from Yahoo Finance and run some analytics to help the user make informed decisions to better manage their investments.  In order to extract information we need to import a package called pandas DataReader. Since this is a package it needs to be installed in the environment in which the code will be running.  The instructions to insatll the package are listed below:

pip install pandas-datareader

Depending upon their set up, the user may also need to install other packages. I am leaving that as the responsibilty of the user. 

The user will be required to enter the stocks and the number of shares that they own.  When the user is finished entering the portfolio, they should use 'done' or 'DONE' to see the results.  The code starts of with an empty dictionary labeled 'dic' that will be updated with the stock names as keys and the number of shares as values.  In addition,  there is also an empty list labeled 'portfolio' that will be appended when we enter the stock names.  

The range for which the data is pulled is for the last one year.  The user has the ability ot change this time period. I have set the variable 'end_date'  as todays date and the beginning date with a timedelta of the previous 365 days.  The user can change this beggining date value by inputting a different value in the 'beg_date' variable.

We want to compare our portfolio aginst the S&P 500 index, since that is considered a diversified portfolio.  The code will pull the data for the SP500 index and our portfolio of stocks inputted. Several varibales and dataframes will be created that are mentioned below and numbered.

1) portfolio --> initially an empty list that gets appended based on inputs

2) dic --> initially an empty dictionary that gets updated based on inputs

3) end_date --> todays date

4) beg_date --> end_date - timedelta(365)

5) my_portfolio --> this is a DF of the stocks we entered for the time range choosing only the Adj. Close Column.

6) combined_df --> this is a DF that has the same contents as the DF above with the SP500 values.  This is done by merging the SP500 values retrived with our stock portfolio values.

7) pct_change --> this is DF of percent changes of the combined_df listed in the line above.  This is our measure of volatility.

8) corr --> this is a DF of correlations based on daily closing prices and the not the percent changes.

5) stats --> this is a DF based on daily percent changes and displays key statistical measures.

9) std_dev -->  this is a series, which can be though of as a one column DF that has been extracted from the stats DF.  We sort the values in this series to identify the the most and least volatile stocks so we can display those with more transparecy in the plots.

10) value_stocks -->  this is another empty dictionary that gets updated to reflect the stock names as keys and the values of those stocks based on (shares owned * last stock prices) as values.  

11) ex --> this is a list comprehension that gives the magnitude by which we want the pies to explode in the pie chart. This is needed to make the code dynamic.  

12) explode --> Converting the list 'ex' above into a tuple to be used in code for creating the pie chart.

13) most_volatile_stock --> self explanatory. 

14) least_volatile_stock --> self explanatory.

We then create a bar chart of the volatility of the stocks and color the  most and least volatile stocks differently from the rest.  This is done based on the std_dev series that was extracted from stats.

We then create a pie chart showing the percentages owned based on total value of particular stocks.I also made the pie pieces explode to better visualize the data. 

We also create a line graph based on 'pct_changes' to show volatility over time.  Please note that this last feature will not add a lot of value if our porfolio has many stocks as the visualization will be cluttered. It works well for one or two stocks. The user has the option of entering just one or two stocks to comapre the volatility of their stocks with the SP500 over the time period.

Finally, the DF created are also saved as .csv files in the same location where the code is located. This will help the user if they want to look at the raw data.  













