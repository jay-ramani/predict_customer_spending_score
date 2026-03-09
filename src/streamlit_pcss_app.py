# Import libraries
from seaborn._core.typing import default
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
from pathlib import Path
import joblib
import sys
import os
import time


def display_prompt_input():
	"""
	Prompts the user to input a CSV file containing a shop customer dataset
	with fields as exactly laid out in
	https://www.kaggle.com/datasets/datascientistanna/customers-dataset

	Parameters:
	No parameters

	Returns:
	Pandas data frame containing the cleaned and preprocessed customer data, or None if no valid file was uploaded
	"""

	if "clean_df" in st.session_state:
		return st.session_state["clean_df"]

	df = None

	# Start with a blank slate
	placeholder = st.empty()


	with st.empty():
		# Input title
		placeholder.header(
			body="Welcome to the Shop Customer Data Analysis App",
			help="Upload a CSV file containing shop customer data for analysis",
			anchor=False,
			width="stretch",
			text_alignment="center"
		)

		with st.form(key="file_upload"):
			# Add a file upload widget to the form
			uploaded_file = st.file_uploader("Upload a file", type="csv")
			# Add a summit button to the form
			submit_button = st.form_submit_button(label='Submit')

		if submit_button:
			if uploaded_file is not None:
					# Check file type for appropriate reading
					if uploaded_file.name.endswith('.csv'):
						st.toast("File successfully uploaded and submitted!", icon="✅", duration=5)

						df = data_cleanup(uploaded_file)

						if df is not None:
							st.session_state["clean_df"] = df
							placeholder.empty()  # Clear the placeholder content after processing
							st.empty()
						else:
							st.toast("Data cleanup failed. Please check the file format and contents.", icon="⚠️", duration="infinite")
					else:
						st.toast("File type not handled in this example, but uploaded successfully.", icon="⚠️", duration="infinite")
			else:
				st.toast("Please upload a file before submitting.", icon="⚠️", duration="infinite")

	return df


@st.cache_data
def data_cleanup(uploaded_file):
	'''
	This function takes the raw uploaded .csv file, cleans and preprocesses.

	Parameters:
	uploaded_file: The file uploaded by the user through the Streamlit file uploader widget. Expected to be
	a CSV file containing customer data with specific columns.

	Return:
	A cleaned and preprocessed Pandas DataFrame containing the customer data, ready for analysis and clustering
	'''

	try:
		#Read the data file Customers.csv into dataframe, and inspect first few rows
		df = pd.read_csv(uploaded_file)
	except Exception as e:
		st.error(f"Error reading CSV file: {e}")
		df = None
	else:
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

	return df


def calculate_silhouette_scores(df, dict_k_silhouette_scores=None) :
	"""
	Use Silhouette score to measure how well each data point fits within
	its assigned cluster compared to other clusters

	Parameters:
	1. df: Pandas data frame containing the customer data
	2. dict_k_silhouette_scores: A dictionary to store silhouette scores for each K (number of clusters). If
		None, a new dictionary will be created.

	Returns:
	Returns the maximum silhouette score across K=2 to 8 (both values inclusive), or -1 if no scores were calculated
	"""

	from sklearn.metrics import silhouette_score
	st.session_state['button_state_silhouette'] = True

	X = df[["annual_income", "spending_score"]]

	from sklearn.preprocessing import StandardScaler
	scaler = StandardScaler()
	X_scaled = scaler.fit_transform(X)

	for k in range(2, 9):
		kmeans = KMeans(n_clusters=k, random_state=42)
		labels = kmeans.fit_predict(X_scaled)
		score = silhouette_score(X_scaled, labels)

		#	Track silhouette score for each K in a dictionary
		dict_k_silhouette_scores[k] = score

	return max(dict_k_silhouette_scores.values()) if dict_k_silhouette_scores else -1


def display_optimal_k(inertia) :
	"""
	Displays the optimal K-value (from an Elbow plot))

	Parameters:
	1. inertia: A list of inertia values corresponding to K=1 to 9 (both values inclusive) from KMeans clustering

	Returns:
	No return value, but displays a line graph of inertia vs K to help visually identify the optimal K using the Elbow method
	"""

	# Display optimal K using line graph
	st.title('Finding Optimal K using K-Means Clustering')

	st.header(body="Optimal K Value using Elbow Method", anchor=False, width="content", text_alignment="left")

	fig, ax=plt.subplots(figsize=(8,5))

	ax = plt.plot(range(1, 10), inertia, marker='o')
	ax = plt.xlabel("Number of Clusters (K)")
	ax = plt.ylabel("Inertia")

	st.pyplot(fig)


def display_customer_segment(n_cluster, df, X_scaled):
	"""
	Displays segments of customers based on K-means clustering using annual income and spending score

	Parameters:
	1. n_cluster: number of clusters to use for K-means
	2. df: Pandas data frame containing the customer data
	3. X_scaled: Scaled features for K-means clustering

	Returns:
	No return value, but displays a scatter plot of customer segments based on the specified number of clusters
	"""
	#Fit model
	kmeans = KMeans(n_clusters=n_cluster, random_state=42)
	df["cluster"] = kmeans.fit_predict(X_scaled)

	st.session_state['button_state_cust_clust'] = True

	#Cluster visual
	fig, ax = plt.subplots()
	sns.scatterplot(
		x="annual_income",
		y="spending_score",
		hue="cluster",
		palette="Set1",
		data=df
	)
	ax = plt.title("Customer Segments")

	st.title("Customer Segments (Income + Spending)")

	st.pyplot(fig)


def display_age_income_analysis(n_cluster, df):
	"""
	Displays segments of customers based on K-means clustering using age, annual income, and spending score

	Parameters:
	1. n_cluster: number of clusters to use for K-means
	2. df: Pandas data frame containing the customer data

	Returns:
	No return value, but displays a scatter plot of customer segments based on the specified number of
	clusters using age, annual income, and spending score
	"""

	#Segment analysis useing Age and annual income
	X = df[["age", "annual_income", "spending_score"]]
	scaler = StandardScaler()

	X_scaled = scaler.fit_transform(X)

	kmeans = KMeans(n_clusters=n_cluster, random_state=42)
	df["cluster_3d"] = kmeans.fit_predict(X_scaled)

	st.session_state['button_state_age_income'] = True

	#visualize cluster
	#plt.figure(figsize=(8,6))
	fig, ax = plt.subplots()
	sns.scatterplot(
		x="annual_income",
		y="spending_score",
		hue="cluster_3d",
		palette="Set2",
		data=df
	)

	ax=plt.title("Clusters (Age + Income + Spending)")

	st.title("Customer Segments (Age + Income + Spending)")

	st.pyplot(fig)


def display_silhouette_scores(k_silhouette_scores, max_silhouette_score, n_cluster):
	"""
	Displays the silhouette scores for K=2 to 8 (both values inclusive) and highlights the optimal K based on the highest silhouette score

	Parameters:
	1. k_silhouette_scores: A dictionary containing silhouette scores for each K (number of clusters)
	2. max_silhouette_score: The highest silhouette score among all K values
	3. n_cluster: The optimal number of clusters based on the highest silhouette score

	Returns:
	No return value, but displays a table of silhouette scores for each K and highlights the optimal K
	"""

	st.title("Silhouette Scores for K=2 to 8")
	st.header("Optimal K Value (" + str(n_cluster) + ") based on highest Silhouette Score (" + str(round(max_silhouette_score, 4)) + ")", anchor=False, width="content", text_alignment="left")

	if k_silhouette_scores:
		silhouette_df = pd.DataFrame(list(k_silhouette_scores.items()), columns=["K", "Silhouette Score"])

		st.dataframe(silhouette_df, width="stretch", height="auto")
	else:
		st.write("Silhouette scores not available")


def display_shop_custmer_data(df):
	"""
	Displays the shop customer data in a tabular format

	Parameters:
	df: Pandas data frame containing the cleaned and preprocessed customer data

	Returns:
	No return value, but displays the customer data in a styled table format with missing values highlighted
	"""
	st.title("Shop Customer Data")
	st.header(body="Cleaned and Preprocessed Customer Data", anchor=False, width="content", text_alignment="left")
	st.dataframe(df.style.highlight_null(), width="stretch", height="auto", placeholder="Missing")

def display_prediction():
	"""
	Predict clusters using the cleaned dataframe already uploaded
	"""

	st.title("Customer Segmentation Prediction")

	if "clean_df" not in st.session_state:
		st.warning("Upload and process a dataset first.")
		return

	df = st.session_state["clean_df"]

	MODELS_DIR = Path("../models")

	if not MODELS_DIR.exists():
		st.error("models folder not found.")
		return

	model_files = sorted(list(MODELS_DIR.glob("*.joblib")) + list(MODELS_DIR.glob("*.pkl")))

	if not model_files:
		st.error("No model files found in models folder.")
		return

	selected_file = st.selectbox(
		"Choose a model file",
		options=model_files,
		format_func=lambda p: p.name
	)

	@st.cache_resource
	def load_artifact(path):
		return joblib.load(path)

	artifact = load_artifact(str(selected_file))

	pipeline = artifact.get("pipeline")
	features = artifact.get("features", [])
	cluster_labels = artifact.get("cluster_labels", {})
	cluster_note = artifact.get("cluster_note", "")

	if pipeline is None or not features:
		st.error("Model artifact missing pipeline or features.")
		return

	st.subheader("Model")
	st.write("Model:", artifact.get("model_name", selected_file.stem))
	st.write("Features:", ", ".join(features))

	if st.button("Run Prediction"):

		X_batch = df[features].copy()

		preds = pipeline.predict(X_batch)

		result_df = df.copy()
		result_df["predicted_cluster"] = preds
		result_df["cluster_description"] = result_df["predicted_cluster"].map(cluster_labels)

		if cluster_note:
			st.info(cluster_note)

		st.success("Prediction completed")

		st.dataframe(result_df)

		csv_data = result_df.to_csv(index=False).encode("utf-8")

		st.download_button(
			label="Download Predictions",
			data=csv_data,
			file_name="predicted_clusters.csv",
			mime="text/csv"
		)

def display_toast_on_reset():
    if "clean_df" in st.session_state:
        del st.session_state["clean_df"]

    st.toast(
        "Application reset. Please upload a new file.",
        icon="🔄",
        duration=5
    )

# def display_toast_on_reset():
# 	"""
# 	Displays a toast notification when the user clicks the "Start Over" button to reset the app

# 	Parameters:
# 	No parameters

# 	Returns:
# 	No return value, but shows a toast message indicating that the app has been reset and prompts the user to upload a new file
# 	"""

# 	st.toast("Application reset. Please upload a new file to start over.", icon="🔄", duration=5)


def main() :
	"""
	Main function to run the Streamlit app for customer segmentation using KMeans clustering. It prompts the
	user to upload a customer dataset, performs data cleanup, finds the optimal number of clusters using the
	Elbow method and Silhouette scores, and allows the user to visualize customer segments and make predictions
	based on saved models.

	Parameters:
	No parameters

	Returns:
	No return value, but runs the Streamlit app and displays various interactive components for customer
	segmentation analysis
	"""

	exit_code = 0

	# Change working directory to the directory of the script to ensure relative paths work correctly
	os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

	df = display_prompt_input()
	df = st.session_state.get("clean_df")

	if df is not None:
		# Proceed only if we're dealing with a valid Pandas data frame

		#Remove CustomerID from dataframe since no predictive power.  Renamed column names to snake case for easier reference in code
		df = df.drop(columns=["CustomerID"]).rename(
			columns = {
				'Gender': 'gender',
				'Age': 'age',
				'Annual Income': 'annual_income',
				'Spending Score': 'spending_score',
				'Profession': 'profession',
				'Work Experience': 'work_experience',
				'Family Size': 'family_size',
			}
		)

		# Select features for segmentation
		X = df[["annual_income", "spending_score"]]

		# Scale features
		scaler = StandardScaler()
		X_scaled = scaler.fit_transform(X)

		#Find optimal K using KMeans clustering
		inertia = []

		for k in range(1, 10):
			kmeans = KMeans(n_clusters=k, random_state=42)
			kmeans.fit(X_scaled)
			inertia.append(kmeans.inertia_)

		# Dictionary to store silhouette scores for each K, to be used across function calls without needing to recompute
		k_silhouette_scores = {}

		# Calculate silhouette scores
		max_silhouette_score = calculate_silhouette_scores(df, k_silhouette_scores)

		if max_silhouette_score != -1:
			# Find the K with the highest silhouette score
			n_cluster = [key for key, value in k_silhouette_scores.items() if value == max_silhouette_score][0]
		else:
			n_cluster = 4  # Default to 4 if silhouette scores couldn't be calculated

		# Given that any widget interaction will cause a re-run of the entire script, there's no
		# need to implement complex state management for the buttons. We can simply use the on_click callback
		# to show a toast, and rely on the fact that any interaction will reset the app state and require the
		# user to upload a new file to proceed.
		st.button(
			label="Start Over",
			help="Click to reset the app and upload a new file",
			icon="🔄",
			icon_position="right",
			key=None,
			on_click=display_toast_on_reset,
			shortcut="Ctrl+Alt+S",
			type="secondary"
		)

		tab_shop_customer_data, tab_optimal_k, tab_silhouette_scores, tab_cust_segments, tab_age_income, tab_prediction = st.tabs(
			["Shop Customer Data", "Optimal K", "Silhouette Scores", "Customer Segments", "Age-Income Analysis", "Prediction"],
			width="stretch",
			default="Shop Customer Data",
			key=None,
			on_change="ignore"
		)

		with tab_shop_customer_data:
			display_shop_custmer_data(df)

		with tab_optimal_k:
			display_optimal_k(inertia)

		with tab_silhouette_scores:
			display_silhouette_scores(k_silhouette_scores, max_silhouette_score, n_cluster)

		with tab_cust_segments:
			display_customer_segment(n_cluster, df, X_scaled)

		with tab_age_income:
			display_age_income_analysis(n_cluster, df)

		with tab_prediction:
			display_prediction()
	else:
		# Flag error to the calling shell
		exit_code = -1


if __name__ == '__main__' :
	main()
