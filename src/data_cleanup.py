##This program loads the Customers.csv file from the data/raw folder, cleans and preprocesses it,
# and then saves the cleaned dataset to the data/processed folder using the same file name (Customers.csv).

import pandas as pd

#Read the data file Customers.csv into dataframe, and inspect first few rows
df = pd.read_csv("../data/raw/Customers.csv")

#Remove customers who are under age 12 to comply with data protection act.
df = df[df["Age"] >= 12]

#Remove records where work experience > age
df = df[df["Work Experience"] <= df['Age']]

#Remove records where family size is greater than 7 to remove outliers
df = df[(df["Family Size"] <= 7)]

#Remove records where family size is greater than 7 to remove outliers
df = df[df["Profession"].notna()]

#Renamed column names to snake case for easier reference in code
df = df.rename(
    columns = {
        'Gender': 'gender',
        'Age': 'age',
        'Annual Income ($)': 'annual_income',
        'Spending Score (1-100)': 'spending_score',
        'Profession': 'profession',
        'Work Experience': 'work_experience',
        'Family Size': 'family_size',
    }
)

df.to_csv("../data/processed/Customers.csv", index=False)