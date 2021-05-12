# Top Selling Products on Amazon

This is a project for Data Blog at DataRes during Spring 2021. The article published on this project can be found on the DataRes Medium site.

## Project Description
The goal of this project is to identify any trends in consumer buying habits from over 2 million rows of products data.

## Data
We used a dataset from Kaggle that was collected using web scraping. It contains product information for over 2,000,000 products sold on Amazon that had been labelled as Best Seller.

Link to datatset: https://www.kaggle.com/waqarahmad101/amazon-best-seller-product-data

## Data Processing
For the purpose of this project, we decided to take a random sample of 10,000 products to optimize code run time. The data from the random sample was cleaned up before conducting any analysis. Irrevelant columns such as links to the image url and Amazon page were dropped. Any data points that contained a price range was replaced by the midpoint price of the range. The product prices, number of reviews and ratings were correctly formatted by removing any commas or dollar signs, and then converting the strings to the appropriate data type (int/float). For product titles, filler words and any duplicate words were removed.

## Data Analysis
