# Predit Customer Spending Score

## Value the Project Brings to the Industry
The Retail industry is one where margins are often thin, and costs need to be tightly managed to maintain operations and continuity of growth. As the population grows, there is a constant challenge given the variety of customers that have to be addressed. There are people of all ages, diverse backgrounds, and different cultural and professional demographics that have different spending habits. In such an environment, how does a Business in the Retail industry identify which customers are the right customers to focus on with marketing campaigns? Which customers should be offered incentives and loyalty benefits? This Project will attempt to answer such questions through the use of Machine Learning models and in turn will drive value for the Retail industry as a whole by providing an approach and methodology to determine which customers are worth focusing on based on predicting their propensity to spend more. 

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

## Approach of Analysis
The approach of analysis:
1. Gain a deep understanding of the business problem that needs to be solved, and the outcome that needs to be delivered (detailed out in writing)
2. Understand the data; what impact (if any) do each of the existing features have on the others? Are additional features needed?
3. Determine if the data has natural clustering or groupings of customers and if there are any patterns
4. Create a baseline regression model, and test it against a validation data set - fine tune the predictions to maximize
5. Revisit the problem statement to confirm if it has been addressed

## Success Metrics
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

## Key Findings
TBD based on analysis that will be performed using ML techniques

## Instructions
The setup of the Github repository is as follows:

-Predict_Customer_Spending_Score
--data
----processed
----raw
----sql
--experiments
----experiment#
----README.MD
--models
----model_notebook#
----README.MD
--reports
----README.MD
--src
----README.MD
-README.MD

To recreate the models, the following libraries have to be available
- <list of libraries and packages>

Seed: <##>

Hyperparameters:
- TBD