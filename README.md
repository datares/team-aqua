# Top Selling Products on Amazon

Project Lead: Avishek Ghosh

Team Members: Sudhanshu Agrawal, Angelina Kim, Zoey Meng, Cyrus Ho

This is a project for Data Blog at DataRes during Spring 2021. The article published on this project can be found on the DataRes Medium site.

## Project Description
The goal of this project is to identify any trends in consumer buying habits from over 2 million rows of products data.

## Data
Our dataset is the Amazon Best Seller Products Data from Kaggle. It contains over 2,000,000 rows containing descriptions of the products sold on Amazon.

Link: https://www.kaggle.com/waqarahmad101/amazon-best-seller-product-data

## Data Cleaning
Our dataset contain over 2 millions of data. To optimize the code run time, a random sample of 10,000 rows was chosen. We dropped the columns containing any links (such as image url and Amazon link) as it was not relevant for our analysis. For the data cleaning process, the ratings and number of reviews had to be correctly formatted by removing any commas and any text, and then converting the strings to int/float. A similar procedure was followed for the product prices by the removal of the $ sign. Often the price was given as a range. To deal with this, we decided to take the average of the lower and upper price limits. The different product categories were separated by a delimeter (a slash), and we decided to split the different categories for each product and store them in a list. The product title was changed to be in all lowercase letters and any filler words (such as a, the, and) were removed. Additionally, any duplicate words in the title were also removed.
