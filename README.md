# Predit Customer Spending Score

## Business Motivation

## Dataset Used

## Risks/Unknowns
We are working with a dataset representing an imaginative shop’s ideal customers. As such, all data is generated (how this data is generated is unknown) and may not reflect real world scenarios. Here are some potential risks and uncertainties of the dataset:

* Incomplete, False, or Mislabelled Data: There are data that looks to be false or incomplete. For example, we have customers with age 0 with substantial income. This may represent missing age data that is filled in with ‘0’
* There is a relative equal distribution of customers across all age groups from 0-99 which may skew the model 
* There is gender imbalance with 1186 females vs 814 males. Any insights modeled with respect to gender may bias towards females
* Artists (612 entries representing ~30%) and Healthcare (339 entries representing ~17%) professions together denote almost 50% of all professions in the dataset. This may not represent real world population and may skew our model results towards those two professions
* The dataset does not include a temporal feature, thus the models will not be able to account for seasonality or changes in customers behaviour overtime
* There are 81 entries (representing ~4% of the dataset) where the work experience is greater than the age. 
* A large number of entries have 1 year or less in work experience with 901 entries

### Potential Violation of Canadian Personal Information Regulations
In Canada, private-sector organizations are regulated by PIPEDA (Personal Information Protection and Electronic Documents Act) which emphasizes:

* Purpose limitation
* Meaningful consent
* Data minimization

As such, organizations should collect only the personal information necessary for clearly defined business objectives. Sensitive attributes (e.g. income, profession, family data) require strong justification under privacy best practices. Because our dataset includes such attributes, our analysis and models may run afoul of PIPEDA when we use these attributes.

## Approach of Analysis

## Breakdown of Roles and Tasks