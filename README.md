# Predit Customer Spending Score
A project of Cohort 8 of the Machine Learning team 9 at the Data Sciences Institute, University of Toronto

## Members (in no particular order)
[Itzel Polin](https://github.com/ItzelPolin)
[Stan W](https://github.com/stan-2828)
[Saqib Syed](https://github.com/saqsyed)
[Jay Ramani](https://github.com/jay-ramani)
[Ganga Ratnam](https://github.com/ganga-ai)

## Value the Project Brings to the Industry
The Retail industry is one where margins are often thin, and costs need to be tightly managed to maintain operations and continuity of growth. As the population grows, there is a constant challenge given the variety of customers that have to be addressed. There are people of all ages, diverse backgrounds, and different cultural and professional demographics that have different spending habits. In such an environment, how does a Business in the Retail industry identify which customers are the right customers to focus on with marketing campaigns? Which customers should be offered incentives and loyalty benefits? This Project will attempt to answer such questions through the use of Machine Learning models and in turn will drive value for the Retail industry as a whole by providing an approach and methodology to determine which customers are worth focusing on based on predicting their propensity to spend more.

## Business Motivation
Department stores operate in competitive retail environments where marketing budgets must be allocated strategically to maximize return on investment. Loyalty programs, promotions, and personalized offers can increase revenue, but distributing incentives broadly reduces efficiency and profitability. The key business challenge is identifying which customers are likely to generate higher value, especially when limited purchase history is available.

At the time of customer registration, retailers often only have access to basic demographic and socioeconomic information such as age, income, and work experience. This raises a practical question: can limited early-stage information be used to estimate customer value in a meaningful way?

Within the Canadian context, private-sector organizations are governed by the Personal Information Protection and Electronic Documents Act (PIPEDA), which emphasizes purpose limitation and collecting only information necessary for clearly defined objectives. Attributes such as income, profession, and family-related information can be considered sensitive and require justification. Evaluating whether predictive performance improves significantly when additional features are included supports responsible data practices while still enabling data-driven decision-making.

In this project, Spending Score serves as a proxy for customer value. If it can be estimated reliably from limited attributes, the store could prioritize high-potential customers earlier and allocate marketing resources more efficiently.

Reference: Office of the Privacy Commissioner of Canada, Overview of PIPEDA – https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/

## Dataset Used
The [Shop Customer dataset from Kaggle](https://www.kaggle.com/datasets/datascientistanna/customers-dataset/data) serves as the foundation for this analysis

## Purpose & Overview
This project evaluates whether Spending Score can be predicted using demographic and socioeconomic attributes typically available at customer onboarding. The analysis is structured in two stages.

Stage 1 focuses on supervised regression modeling to test whether Spending Score can be predicted from a limited feature set with acceptable accuracy. Model performance is evaluated using MAE, RMSE, and R² to determine feasibility.

If predictive performance is insufficient, Stage 2 shifts toward extracting business value through segmentation analysis. In this case, clustering techniques are used to identify natural customer groups based on income and spending behavior. These segments are then profiled using demographic attributes to support targeted marketing strategies.

This staged approach ensures that the project remains outcome-focused. Whether through predictive modeling or segmentation, the goal is to generate actionable retail insights rather than forcing model performance.
### Industry Value
This project provides value to retail organizations by demonstrating how customer value estimation can be approached under realistic data constraints. Many retailers lack complete behavioral data for all customers, particularly new loyalty members. Testing predictive feasibility before operational use reflects applied machine learning practice and responsible decision-making.

If demographic attributes alone do not strongly predict Spending Score, that insight itself is valuable. It suggests that behavioral data may be necessary for accurate value estimation and informs future data collection strategy. Alternatively, if segmentation reveals clear customer groups, those segments can guide differentiated marketing strategies, loyalty programs, and promotional targeting.

By combining feasibility testing with flexible analytical design, this project reflects how data science is applied in real business environments.

## Adressing the Business Question
We begin by validating and cleaning the dataset, removing logically inconsistent records such as invalid ages or impossible work experience values. Two feature scenarios are then constructed: a limited-feature model using Age, Annual Income, and Work Experience, and a broader model that may incorporate Gender, Profession, and Family Size.

Supervised regression models are trained and evaluated using cross-validation to assess generalization performance. Metrics include MAE, RMSE, and R².

### Dataset Used
The Shop Customer dataset **`Customers.csv`** serves as the foundation for this analysis.

The data represents customer information collected by a fictional retail store through its membership program. Each row corresponds to one customer and includes demographic (age, gender, family size), socioeconomic (income, profession, work experience), and behavioral (spending score) attributes.

The dataset contains **2,000 records** and **8 features**.

#### Dataset Schema

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

### Risks/Unknowns
#### Data
- Data is not robust (ie. data is fake or not true)
- Incomplete or mislabelled data
- Unrepresentative data where our training data does not accurately reflect real world data (ie. data may be old and monetary figures may not take inflation into account)
- Inconsistent data (ie. different formats of the similar data)
- Data duplication
#### Model
- Data overfitting to training dataset
- Small dataset
- Selection bias of data

## Goals & Objectives
### Success Metrics
1. At a minimum, 80% accuracy in comparison to the customer spending score published in the dataset.
2. Also, the ability to predict the score with missing fields like profession, family size etc..

### Stakeholders
In a corporate setting, we could have the following stakeholders

#### Marketing
Marketing teams could use insights from our modelling to target customers based on the analysis

#### Finance
Finance teams could use the modelling for Return on Investment (ROI) to measure investment and Marketing budgets

#### Technical
Technical stakeholders can include the team that manages data platforms, and also have other technical teams relying on the solution's modelling

#### C-Suite
Executives like CEOs, CDOs, CTOs, CMOs and CFOs can have a high level view of customer spending to assess goals and re-visit company charter

#### Legal
Legal teams dealing with customer privacy would need be involved in what and how much information we could use to model

## Breakdown of Roles and Tasks

## Key Findings
TBD based on analysis that will be performed using ML techniques

## Instructions
The setup of the Github repository is as follows:
```bash
Predict_Customer_Spending_Score
    data  
        processed
        raw
        sql
    experiments
        experiment#
        README.md
    models
        model_notebook
        README.md
    reports
        README.md
    src
        README.md
    .gitignore
    README.md
```

To recreate the models, we need to use the paramters below

Seed: Randome_State = 42

Hyperparameters:
- TBD

## Techniques & Technologies
### Steps taken
* Data Cleaning: Handling missing values, removing inconsistencies, and ensuring data readiness
* Pre-analysis, finding correlation: Understanding patterns, correlations, and data distribution
* Regression analysis and validation: Applying linear regression models to determine key loyalty drivers. and create training and test sets, assessing model accuracy
* Visualization: Creating plots to represent insights and model results
* Conclusion

### Approach of Analysis
The approach of analysis:
1. Gain a deep understanding of the business problem that needs to be solved, and the outcome that needs to be delivered (detailed out in writing)
2. Understand the data; what impact (if any) do each of the existing features have on the others? Are additional features needed?
3. Determine if the data has natural clustering or groupings of customers and if there are any patterns
4. Create a baseline regression model, and test it against a validation data set - fine tune the predictions to maximize
5. Revisit the problem statement to confirm if it has been addressed

### Technical Stack:
* Programming Language: Python

* Libraries Used:
** Numpy: matrix operations
** Pandas: data analysis
** Matplotlib: creating graphs and plots
** Seaborn: enhancing matplotlib plots
** SKLearn: regression analysis

## Key Findings & Instructions

## Breakdown of Roles and Tasks

## Visuals & Credits
