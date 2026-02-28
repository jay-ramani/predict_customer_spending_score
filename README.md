# Predit Customer Spending Score

## Business Motivation

## Dataset Used
The dataset **`Customers.csv`** serves as the foundation for this analysis.  

The data represents customer information collected by a fictional retail store through its membership program. Each row corresponds to one customer and includes demographic (age, gender, family size), socioeconomic (income, profession, work experience), and behavioral (spending score) attributes.

The dataset contains **2,000 records** and **8 features**.

### Dataset Schema

| Column | Data Type | Modeling Role |
|--------|-----------|---------------|
| Customer ID | Identifier | Excluded (Primary Key) |
| Age | Numerical | Input (X) |
| Annual Income | Numerical | Input (X) |
| Family Size | Numerical | Input (X) |
| Gender | Categorical | Input (X) |
| Profession | Categorical | Input (X) |
| Work Experience (years) | Numerical | Input (X) |
| **Spending Score** | Numerical | **Target (y)** |


The Spending Score is assigned by the store based on customer purchasing behavior for this dataset.
The objective of the trained machine learning model is to predict the Spending Score of a new customer using the available input features.

## Risks/Unknowns
### Data
- Data is not robust (ie. data is fake or not true)
- Incomplete or mislabelled data
- Unrepresentative data where our training data does not accurately reflect real world data (ie. data may be old and monetary figures may not take inflation into account)
- Inconsistent data (ie. different formats of the similar data)
- Data duplication
### Model
- Data overfitting to training dataset 
- Small dataset 
- Selection bias of data

### Goals & Objectives
#### Goals
The goal of this project is to analyze customer characteristics to understand spending behavior and determine the most effective modeling approach for estimating customer value. Both supervised and unsupervised learning techniques are explored to assess whether customer spending is better predicted directly or better understood through segmentation. We aim to evaluate whether limited customer data is sufficient to support reliable value estimation and informed marketing decision-making.

#### Objectives
- Perform data validation and cleaning to ensure logical consistency and business realism.
- Explore relationships between customer attributes and Spending Score.
- Develop and compare supervised learning models to predict Spending Score.
- Compare predictive performance between a limited-feature model and a full-feature model.
- Evaluate model performance using appropriate regression metrics (MAE, RMSE, R²).
- Apply clustering techniques to identify natural customer segments.
- Interpret model results to identify key drivers of customer value.
- Translate predictive outputs into actionable marketing recommendations (e.g., customer value tiers).

In summary, this project applies both predictive modeling and customer segmentation techniques to understand spending behavior. By comparing supervised and unsupervised approaches, the study evaluates how customer data can best support informed marketing and business decisions.

### Success Metrics
1. At a minimum, 80% accuracy in comparison to the customer spending score published in the dataset.
2. Also, the ability to predict the score with missing fields like profession, family size etc..

## Stakeholders
In a corporate setting, we could have the following stakeholders

### Marketing
Marketing teams could use insights from our modelling to target customers based on the analysis

### Finance
Finance teams could use the modelling for Return on Investment (ROI) to measure investment and Marketing budgets

### Technical
Technical stakeholders can include the team that manages data platforms, and also have other technical teams relying on the solution's modelling

### C-Suite
Executives like CEOs, CDOs, CTOs, CMOs and CFOs can have a high level view of customer spending to assess goals and re-visit company charter

### Legal
Legal teams dealing with customer privacy would need be involved in what and how much information we could use to model

## Breakdown of Roles and Tasks