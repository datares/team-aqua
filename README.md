# Top Selling Products on Amazon

This is a project for Data Blog at DataRes during Spring 2021. The article published on this project can be found on the DataRes Medium site.

Link to Medium Article: https://ucladatares.medium.com/what-does-everyone-buy-on-amazon-3cc6955a182c

Project Lead: Avishek Ghosh

Team Members: Sudhanshu Agrawal, Angelina Kim, Zoey Meng, Cyrus Ho

## Project Description
The goal of this project is to identify any trends in products that become Best Sellers on Amazon.

## Data
We used a dataset from Kaggle that was collected using web scraping. It contains product information for over 2,000,000 products sold on Amazon that had been labelled as Best Seller. We also used another dataset containing information about 30,000 products sold at Walmart.

Link to Amazon dataset: https://www.kaggle.com/waqarahmad101/amazon-best-seller-product-data

Link to Walmart dataset: https://www.kaggle.com/promptcloud/walmart-product-dataset-usa

## Data Processing
For the purpose of this project, we decided to take a random sample of 10,000 products from the Amazon dataset to optimize code run time. The data from the random sample was cleaned up before conducting any analysis. Irrevelant columns such as links to the image url and Amazon page were dropped. Any data points that contained a price range was replaced by the midpoint price of the range. The product prices, number of reviews and ratings were correctly formatted by removing any commas or dollar signs, and then converting the strings to the appropriate data type (int/float). For product titles, filler words and any duplicate words were removed. A similar process was followed for cleaning the Walmart dataset.

## Data Analysis
We conducted our analysis to answer the following questions:
#### Product Titles
What are the most common words in the product titles from different categories?
#### Price / Rating
What is the distribution of prices and ratings for all products?
#### Product Categories
How can the different product categories be clustered together and what is the differences in product price, rating and number of reviews for these clustered categories?
#### Amazon vs Walmart
How do the most popular product categories from Amazon differ from those from Walmart?
