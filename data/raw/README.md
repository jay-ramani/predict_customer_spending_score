The dataset appears to be synthetic and contains several inconsistencies that may impact model reliability and business interpretation.

# Data Quality Issues
* Invalid Age Values: 23 records (1.15%) have age = 0, likely representing missing values.
* Unrealistic Ages: 210 entries (10.5%) represent customers under 12 years old.
* Work Experience Errors: 81 records (4.05%) report work experience greater than age.
* Low Work Experience Concentration: 45.05% of customers report 1 year or less of work experience.
* Missing Profession: 1.75% of records have no profession listed.

# Distribution Bias
* Gender Imbalance: 59.3% female vs 40.7% male.

# Dataset Limitations
* Synthetic dataset: relationships between variables may not reflect real customer behavior.
* Limited features: dataset only includes demographic variables (no purchase history or behavioral data).
* No temporal data: models cannot account for seasonality or changes in behavior over time.