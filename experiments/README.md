### Regression and Clustering of Customer Demographic Data

## Regression - Prediction of Spending Score
The Customer.csv dataset contains demographic data including Gender, Age, Annual Income, Profession, Work Experience, and Family Size. Spending Score is also included, appearing to be a derived value. 

The Regression nobebook (02_regression.ipynb) explores the ability to use the Customer demographic data provided to try and predict the Spending Score column. the data set is split into train and test tuples (20% test). The numerical and categorical preprocessing pipelines are defined, with categorical variables being one hot encoded. 

Linear, Polynomial, and Random Forest Regression is performed and cross validation is done on each of the models. However, the regressions have not provided reasonable MSE, MAE and r^2 values:  
- r^2 of ~0 or negative: demonstrates that the model is very poor at predicting Spending Score for a generalized data set.
- MAE of 23 to 25: demonstrates that if we did try to predict, on average our predictions of spending score would be off by up to 25 points (where Spending Score is measured between 0 to 100) - this is a poor performance, and aligned with the r^2 values we are getting.
 
The above demonstrates that there is no relationship between the features that could be used to do a prediction of the Spending Score. This is consistent with our Exploratory Data Analaysis (01_eda.ipynb), that shows a similar outcome that there is a lack of correlation between the features. Furthermore, it proves that Spending Score is quite possibly a manufactured value that is not derived through measurement or mathematical calculation from the data, and is therefore not a deterministic function of any of the features in the data. Hence, Regression will not work as an approach to predict Spending Score. 

## Clustering - Segmentation of Customers

As a next step to continue driving valuable outcomes, we pivot to clustering the data to drive useful observations about the customer base using the demographic data provided. This is covered in the 03_clustering.ipynb notebook. The clustering will help us understand whether the customers fall into particular categories, and will also help us identify next steps such as additional data collection steps, or insights towards shaping marketing campaigns, etc.

To perform the clustering, we will still use Spending Score, because it allows us to have a relative scale for the customers represented in the data set. 

For clustering, we start with standardizing the values in the dataset to avoid different scales of values impacting the placement of clusters. To find the right k-value to use for the clusters, we employ the "Elbow method", and calculate Silhouette scores for the range of k-values. The Silhouette scores will tell us how well separated and cohesive the clusters are, and with the highest score of 0.38, we get a k-value of 4. 

For the purposes of our dataset, we use k = 4 and perform a k-means clustering to see if we can interpret spending propensity based on income or age, while avoiding over-fragmentation of the clusters. We get 4 main clusters:
- High income, high spending (top right quadrant)
- High Income, low spending (bottom right quadrant)
- Moderate Income, high spending (top left quadrant)
- Moderate Income, low spending (bottom left quadrant)

This shows that income alone does not dictate spending propensity as the there are customers with different ranges of incomes in both the high spending and low spending quadrants. 

We assessed whether Profession could be used as a demographic to determine spend, however our data shows it does not, because the same profession can be found in the high income and low income categories, and as we have already seen, income alone is not an indicator of spending propensity. 

As a final step, we attempt to evaluate the impact of Age on spending propensity. Our clustering indicates that combining Age and Income still does not yield cohesive clusters that would determine spending propensity.  

## Key Outcomes
- Our Exploratory Data Analysis demonstrates there is no correlation between the features and the target variable, and there are missing values, as well as unusual values in the dataset - e.g. Ages less than 18 that have incomes (300+ rows), work experiences of 0, etc.
- Multiple types of regressions yield r^2 <= 0, and high MAE and MSE, indicating that the features collected are not conducive to predicting spending score using regression techniques, and furthermore informs us that Spending Score is potentially a relative value as opposed to being a mathematical or measured value. 
- Instead of predicting Spending Score, we switch to attempting to understand customer behavior by clustering the data. Our analysis shows optimal k-value to be used is 4, however our Silhouette score flattening at 0.38 tells us that the dataset does not have strong natural clusters. 
- Clustering further proves that we get 4 broad clusters, but none of them help us conclude that Age or Income can be an indicator of spending propensity. Furthermore, adding Age reduces cohesiveness of the clusters, showing us that it is not a useful feature to add in for this particular dataset. 
- Profession categories are broad and overlapping, and do not provide us a deterministic way of understanding if one profession impacts spending propensity over another, as the incomes for professions are also random (there is no trend that a profession necessarily has a higher income over another, and even if it did, we have already proven that income is not a significant indicator of spending).
- At best, these clusters can be used to understand Personas of customers, with some better quality data collection around other features such as the income, ages and professions.

