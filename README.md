# Top Selling Products on Amazon

This is a project for Data Blog at DataRes during Spring 2021. The article published on this project can be found on the DataRes Medium site.

## Project Description
The goal of this project is to identify any trends in consumer buying habits from over 2 million rows of products data.

## Data
We used a dataset from Kaggle that was collected using web scraping. It contains product information for over 2,000,000 products sold on Amazon that had been labelled as Best Seller.

Link to datatset: https://www.kaggle.com/waqarahmad101/amazon-best-seller-product-data

## Data Cleaning
Our dataset contain over 2 millions of data. To optimize the code run time, a random sample of 10,000 rows was chosen. We dropped the columns containing any links (such as image url and Amazon link) as it was not relevant for our analysis. For the data cleaning process, the ratings and number of reviews had to be correctly formatted by removing any commas and any text, and then converting the strings to int/float. A similar procedure was followed for the product prices by the removal of the $ sign. Often the price was given as a range. To deal with this, we decided to take the average of the lower and upper price limits. The different product categories were separated by a delimeter (a slash), and we decided to split the different categories for each product and store them in a list. The product title was changed to be in all lowercase letters and any filler words (such as a, the, and) were removed. Additionally, any duplicate words in the title were also removed.
