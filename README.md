# Everything Markets - I publish a Python-based Machine Learning/AI model daily on this repository
This repository contains my market prediction code. The goal is to share and evaluate various forecasting strategies using Machine Learning and AI. Email me at saurabh.nagda.mba24@oxford.said.edu

# Project Overview
This project utilizes historical stock data to predict future stock prices using machine learning algorithms. The repository includes data preprocessing, feature engineering, model training, and evaluation scripts.

# Features
- Implementation of various machine learning algorithms
- Evaluation of different regression models for stock price prediction
- Data fetching from Yahoo Finance
- Data preprocessing and feature engineering
- Evaluation metrics to assess model performance
- Visualization of predicted vs. actual stock prices

# List of Python Codes in this project (in reverse chronological order):
- Simple code to perform an inner join on customer data in SQL
- Updated code to cleanup data to remove outliers using Z-score
- A simple code to cleanup data for stock analysis by excluding days with extreme returns
- Adjusting Data and Analyzing Post-Earnings Day Anomalies for AAPL
- Update on ARIMA Forecast: Excluding Post-Earnings Days to Remove Trading Anomalies
- Simple code to use Statsmodels ARIMA to forecast AAPL price
- Updated to seek user input on a year to backtest the momentum trading algorithm for that year
- Updated - Pick the top 10 momentum stocks and share the returns, standard deviation, VaR, and Sharpe ratio for the portfolio for 2024
- The code will pick the top 10 momentum stocks using 2023 data and share the returns for the portfolio for 2024
- Back-Testing Code for Momentum Stock Picking: Selects the Top 10 Momentum Stocks from the Last 4 Years Based on Strength and Quality
- Automated stock selection based on average P/E ratio, momentum health indicator, and the top 10 highest 2024 returns
- Added Delta Normal VaR to the existing code for Momentum Investing
- Added a "Momentum Health Indicator" column to calculate the difference between the percentage of days the stock went up and the percentage of days it went down
- Starting code to import yearly returns and P/E ratios for the momentum investing strategy
- S&P500 2024 data analysis in Excel
- Added 2024 Sharpe Ratio to Previous Code to List 500 S&P 500 Stocks and their 2024 Returns and Standard Deviation
- Added 2024 Standard Deviation to Previous Code to List 500 S&P 500 Stocks and their 2024 Returns
- New year 2025 code to fetch 2024 returns of 500 S&P 500 companies 
- Simple code to import daily trading volume for MSFT, GOOG, QQQ and SPY using yFinance
- Code to add Moving Average Convergence Divergence (MACD) to identify trend changes
- Added plots for 20-day moving averages for MSFT, GOOG, QQQ, and SPY
- Added Correlation Matrix for MSFT, GOOG, SPY, and QQQ
- Optimize Portfolio VaR by Adjusting Composition of MSFT and GOOG in the portfolio
- Calculate the Value at Risk (VaR) for a 50:50 portfolio Microsoft (MSFT) and Google (GOOG).
- Calculate the Sharpe Ratio for MSFT and GO using SPY as the proxy for market returns and standard deviation
- Calculate expected returns for MSFT and GOOG using CAPM
- Calculate VaR (Value at Risk) for GOOG and MSFT with 95% confidence intervals
- Calculate the market risk premium for MSFT and GOOG, using SPY as proxy for the Market
- Code to add Beta values of GOOG, MSFT
- Code to analyze EPS and P/E ratios for GOOG, MSFT, QQQ and SPY
- Starting code to analyze and plot growth and correlation between GOOG, MSFT, QQQ, and SPY
- Updated MSFT price prediction code to use the RandomForest machine learning prediction model
- Updated Polynomial Regression code to split the data into training and test data
- Program to run polynomial regression from Scikit-learn to determine the price of diamonds using length, width, and depth
- A simple code to invoke OpenAI LangChain and use it to tell a short story
- Code to read an SQL database stored locally and run some SQL queries to update the contents in the database
- A simple program to transfer Excel data to a local SQL database
- Code to update the price of NVDA from YFinance to chart Protective Put and Covered Call strategy after earnings
- Before NVDA earnings call today, 11/20/24, code used to chart Covered Call and Protective Put trading strategy
- Code to perform sentiment analysis for content related to the US from FT.com
- A new code added to generate a word cloud of the summary generated from FT.com
- Simple code to retrieve and summarize a webpage (not an LLM-based code)
- Excel data clean-up and summarization using Pivot Table in the code
- Python program to take an Excel file for product sales, clean it up for blanks, NaNs, and non-logical values, and write the file with sales and average price summaries
- Updated clustering into three categories: 'Low', 'Medium', and 'High' along with summary statistics of these categories
- Clustering of historical inflation data using K-Means from Scikit-learn
- Updated the forecasting model to use the RandomForest algorithm
- A program to find the lag between advertising spend and realized sales. The lag is determined by maximizing R-squared in simple OLS/linear regression
- Simple program to forecast MSFT stock price using a linear regression machine learning model
