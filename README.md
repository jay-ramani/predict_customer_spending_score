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

## Approach of Analysis
The approach of analysis:
1. Gain a deep understanding of the business problem that needs to be solved, and the outcome that needs to be delivered (detailed out in writing)
2. Understand the data; what impact (if any) do each of the existing features have on the others? Are additional features needed? 
3. Determine if the data has natural clustering or groupings of customers and if there are any patterns
4. Create a baseline regression model, and test it against a validation data set - fine tune the predictions to maximize
5. Revisit the problem statement to confirm if it has been addressed 

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