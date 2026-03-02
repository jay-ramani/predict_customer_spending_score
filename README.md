# Predit Customer Spending Score
A project of Cohort 8 of the Machine Learning team 9 at the Data Sciences Institute, University of Toronto
Project Repo: https://github.com/jay-ramani/predict_customer_spending_score

## Members (in no particular order)
* [Itzel Polin](https://github.com/ItzelPolin)
* [Stanley Wong](https://github.com/stan-2828)
* [Saqib Syed](https://github.com/saqsyed)
* [Jay Ramani](https://github.com/jay-ramani)
* [Ganga Ratnam](https://github.com/ganga-ai)

## Industry Valiue
Retail is a high-volume, competitive industry where margins are often thin and marketing dollars must be allocated carefully. Customer populations are diverse across age, income, household structure, and professional backgrounds, which creates real variability in spending habits. A recurring business challenge is deciding which customers to prioritize for targeted campaigns, loyalty benefits, and promotional incentives, especially when a store does not yet have rich purchase history for every customer.

This project provides value to retail organizations by demonstrating how customer value estimation can be approached under realistic data constraints. In many cases, retailers only have limited onboarding attributes (for example age, income, and work experience) for new loyalty members. We test whether these early-stage attributes can predict a customer’s Spending Score with sufficient accuracy to support decision-making. If demographic attributes alone do not strongly predict Spending Score, that insight is still actionable. It suggests that behavioral signals may be required for reliable value estimation and helps inform what additional data is worth collecting.

If direct prediction is not feasible, the project still delivers business value through a structured alternative: segmentation. Clustering can reveal natural customer groups based on income and spending behavior, which can be translated into practical strategies such as differentiated loyalty tiers, tailored messaging, and targeted promotions. Overall, this work provides a repeatable methodology that helps retailers focus their marketing resources on the customers most likely to drive value, while keeping the analysis grounded in model validation and responsible data use.

## Business Motivation
Department stores operate in competitive retail environments where marketing budgets must be allocated strategically to maximize return on investment. Loyalty programs, promotions, and personalized offers can increase revenue, but distributing incentives broadly reduces efficiency and profitability. The key business challenge is identifying which customers are likely to generate higher value, especially when limited purchase history is available.

At the time of customer registration, retailers often only have access to basic demographic and socioeconomic information such as age, income, and work experience. This raises a practical question: can limited early-stage information be used to estimate customer value in a meaningful way?

Within the Canadian context, private-sector organizations are governed by the Personal Information Protection and Electronic Documents Act (PIPEDA), which emphasizes purpose limitation and collecting only information necessary for clearly defined objectives. Attributes such as income, profession, and family-related information can be considered sensitive and require justification. Evaluating whether predictive performance improves significantly when additional features are included supports responsible data practices while still enabling data-driven decision-making.

In this project, Spending Score serves as a proxy for customer value. If it can be estimated reliably from limited attributes, the store could prioritize high-potential customers earlier and allocate marketing resources more efficiently.

Reference: Office of the Privacy Commissioner of Canada, Overview of PIPEDA – https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/

## Purpose & Overview
This project evaluates whether Spending Score can be predicted using demographic and socioeconomic attributes typically available at customer onboarding. The analysis is structured in two stages.

Stage 1 focuses on supervised regression modeling to test whether Spending Score can be predicted from a limited feature set with acceptable accuracy. Model performance is evaluated using MAE, RMSE, and R² to determine feasibility.

If predictive performance is insufficient, Stage 2 shifts toward extracting business value through segmentation analysis. In this case, clustering techniques are used to identify natural customer groups based on income and spending behavior. These segments are then profiled using demographic attributes to support targeted marketing strategies.

This staged approach ensures that the project remains outcome-focused. Whether through predictive modeling or segmentation, the goal is to generate actionable retail insights rather than forcing model performance.


## Addressing the Business Question
We begin by validating and cleaning the dataset, removing logically inconsistent records such as invalid ages or impossible work experience values. Two feature scenarios are then constructed: a limited-feature model using Age, Annual Income, and Work Experience, and a broader model that may incorporate Gender, Profession, and Family Size.

Supervised regression models are trained and evaluated using cross-validation to assess generalization performance. Metrics include MAE, RMSE, and R².

### Dataset Used
The [Shop Customer dataset from Kaggle](https://www.kaggle.com/datasets/datascientistanna/customers-dataset/data) serves as the foundation for this analysis.

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

## Potential Risks and Unknowns
We are working with a dataset representing an imaginative shop’s ideal customers. As such, all data is generated (how this data is generated is unknown) and may not reflect real world scenarios. Here are some potential risks and uncertainties of the dataset:

* Incomplete, False, or Mislabelled Data: There are data that looks to be false or incomplete. For example, we have customers with age 0 with substantial income. This may represent missing age data that is filled in with ‘0’
* There is a relative equal distribution of customers across all age groups from 0-99 which may skew the model 
* There is gender imbalance with 1186 females vs 814 males. Any insights modeled with respect to gender may bias towards females
* Artists (612 entries representing ~30%) and Healthcare (339 entries representing ~17%) professions together denote almost 50% of all professions in the dataset. This may not represent real world population and may skew our model results towards those two professions
* The dataset does not include a temporal feature, thus the models will not be able to account for seasonality or changes in customers behaviour overtime
* There are 81 entries (representing ~4% of the dataset) where the work experience is greater than the age 
* A large number of entries have 1 year or less in work experience with 901 entries

### Potential Violation of Canadian Personal Information Regulations
In Canada, private-sector organizations are regulated by PIPEDA (Personal Information Protection and Electronic Documents Act) which emphasizes:

* Purpose limitation
* Meaningful consent
* Data minimization

As such, organizations should collect only the personal information necessary for clearly defined business objectives. Sensitive attributes (e.g. income, profession, family data) require strong justification under privacy best practices. Because our dataset includes such attributes, our analysis and models may run afoul of PIPEDA when we use these attributes.

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
Data Analysis - Explore the data and analyze if there are any anomalies or outliers, null values, duplications etc. If there are, make decisions on treatment of each.

Data Cleaning - Based on the data analysis, perform the cleaning required for the data (e.g. removal of nulls, imputation of data if required for any illogical values, etc.).

Modeling - Use the data to perform regression modeling and clustering of the data; determine if the model is performing as required based on MAE, RMSE, and r^2. Test the model for predictive outcomes and validate against provided Spending Score column.

Visual Plots - Add the visual plots for data exploration, models and clustering (including feature evaluation etc.).

Report - Summarize the activities and findings in a final report in the README.md file.

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

To recreate the models, we need to use the parameters below

Seed: Random_State = 42

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


## Visuals & Credits
