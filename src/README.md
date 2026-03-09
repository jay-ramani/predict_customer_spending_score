1. data_cleanup.py is a cleanup file for the raw data. It applies some basic cleansing rules:

* Remove customers who are under age 12 to comply with data protection act
* Remove records where work experience > age
* Remove records where family size is greater than 7 to remove outliers
* Remove records where Profession is missing

Finally, it renames column names to snake case for easier reference in code

It has to be run from the terminal locally where the project folder exists using:
Python data_cleanup.py

If successful, it will take the raw data file as input from the data\raw\ folder and create a cleaned Customers.csv file in the data\processed\ folder.
The latter is where the notebooks take the file as input.

2. streamlit_pcss_app.py is a Streamlit based front-end application for the solution.

It has to be executed on a terminal locally under the root of the project directory with the command

`streamlit run src\streamlit_pcss_app.py`

on a Windows native console,  or with

`streamlit run ./src/streamlit_pcss_app.py`

on a Git BASH terminal