#Import libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
from pathlib import Path
import joblib
import os


def prompt_input():
	"""
	Prompts the user to input a CSV file containing a shop customer dataset
	with fields as exactly laid out in
	https://www.kaggle.com/datasets/datascientistanna/customers-dataset

	Parameters:
	No parameters

	Returns:
	Pandas data frame
	"""

	df = None

	# Input title
	st.sidebar.title("File Input with Submit Button")

	with st.sidebar:
		with st.form(key="file_upload"):
			# Add a file upload widget to the form
			uploaded_file = st.file_uploader("Upload a file", type="csv")
			# Add a summit button to the form
			submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		if uploaded_file is not None:
			try:
				# Check file type for appropriate reading
				if uploaded_file.name.endswith('.csv'):
					st.success("File successfully uploaded and submitted!")
					df = data_cleanup(uploaded_file)
					st.write("File contents (first 5 rows):", df.head())
					#finding_optimal_K(df)
				else:
					st.write("File type not handled in this example, but uploaded successfully.")
			except Exception as e:
				st.error(f"Error processing file: {e}")
		else:
			st.warning("Please upload a file before submitting.")

	return df


def data_cleanup(uploaded_file):
	'''
	This function takes the raw uploaded .csv file, cleans and preprocesses.

	Parameters:
	Raw .csv file

	Return:
	Processed Pandas data frame
	'''

	#Read the data file Customers.csv into dataframe, and inspect first few rows
	df = pd.read_csv(uploaded_file)

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



def silhouette(df):
	"""
	Use Silhouette score to measure how well each data point fits within
	its assigned cluster compared to other clusters

	Parameters:
	Pandas data frame

	Returns:
	No return value
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
		st.write(f"K = {k}, Silhouette Score = {score:.4f}")




def display_optimal_k(inertia) :
	"""
	Displays the optimal K-value (from an Elbow plot))

	Parameters:
	List of K-means interia

	Returns:
	No return value
	"""

	# Display optimal K using line graph
	st.title('Finding Optimal K using KMeans Clustering')

	fig, ax=plt.subplots(figsize=(8,5))

	ax = plt.plot(range(1, 10), inertia, marker='o')
	ax = plt.xlabel("Number of Clusters (K)")
	ax = plt.ylabel("Inertia")

	#plt.title("Elbow Method")

	st.pyplot(fig)


def customer_segment(n_cluster, df, X_scaled):
	#Fit model using k=4
	kmeans = KMeans(n_clusters=n_cluster, random_state=42)
	df["cluster"] = kmeans.fit_predict(X_scaled)

	st.session_state['button_state_cust_clust'] = True

	#Cluster visual
	#plt.figure(figsize=(8,6))
	fig, ax = plt.subplots()
	sns.scatterplot(
		x="annual_income",
		y="spending_score",
		hue="cluster",
		palette="Set1",
		data=df
	)
	ax = plt.title("Customer Segments")
	#plt.show()
	st.pyplot(fig)

def age_income_analysis(n_cluster, df):
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
	#plt.show()
	st.pyplot(fig)


def prediction():
	st.set_page_config(page_title="Customer Segmentation", layout="centered")
	st.title("Customer Segmentation (KMeans)")
	st.caption("Pick a saved model from /models, enter values, and predict the cluster.")

	MODELS_DIR = Path("models")
	if not MODELS_DIR.exists():
		st.error("models/ folder not found. Create it and put your saved model files inside.")
		st.stop()

	# Find model files
	model_files = sorted(list(MODELS_DIR.glob("*.joblib")) + list(MODELS_DIR.glob("*.pkl")))
	if not model_files:
		st.error("No model files found in models/. Add *.joblib or *.pkl files.")
		st.stop()

	selected_file = st.selectbox(
		"Choose a model file",
		options=model_files,
		format_func=lambda p: p.name
	)

	@st.cache_resource
	def load_artifact(path: str):
		return joblib.load(path)

	artifact = load_artifact(str(selected_file))

	# Support either "artifact is pipeline" OR "artifact is dict with pipeline/features"
	if hasattr(artifact, "predict"):
		pipeline = artifact
		# If it's just a pipeline, you must manually define features here:
		st.warning("This model file is a raw pipeline. Feature list is not stored. Add features to the saved artifact for easier use.")
		features = st.text_input("Enter feature names (comma-separated)", "annual_income,spending_score")
		features = [f.strip() for f in features.split(",") if f.strip()]
		model_name = selected_file.stem
	else:
		pipeline = artifact.get("pipeline")
		features = artifact.get("features", [])
		model_name = artifact.get("model_name", selected_file.stem)

	if pipeline is None or not features:
		st.error("This model artifact is missing 'pipeline' or 'features'. Re-save the model including these fields.")
		st.stop()

	st.subheader("Model")
	st.write(f"**{model_name}**")
	st.write("**Features:**", ", ".join(features))

	st.subheader("Inputs")
	user_inputs = {}
	for f in features:
		user_inputs[f] = st.number_input(f, value=0.0, step=1.0)

	if st.button("Predict Cluster", type="primary"):
		X_row = pd.DataFrame([[user_inputs[f] for f in features]], columns=features)
		pred = pipeline.predict(X_row)
		cluster_id = int(pred[0])
		st.success(f"Predicted cluster: **{cluster_id}**")
		st.dataframe(X_row)


def main() :
	"""
	Entry point of this program

	Parameters:
	No parameters

	Returns:
	No return value
	"""

	exit_code = 0

	df = prompt_input()

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

		display_optimal_k(inertia)

		# Button for silhouette
		if 'button_state_silhouette' not in st.session_state:
			st.session_state['button_state_silhouette'] = True

		st.sidebar.button('Silhouette', on_click=silhouette,  args=(df,))

		# Display slider and button for Customer Segment clustering
		if 'button_state_cust_clust' not in st.session_state:
			st.session_state['button_state_cust_clust'] = True
		n_cluster = 4
		#n_cluster = st.sidebar.slider("Choose the number of clusters", 2, 8, 4)
		st.sidebar.button(
			'Customer Segment', 
			on_click=customer_segment, 
			kwargs={"n_cluster": n_cluster, "df": df, "X_scaled": X_scaled})

		# Display button for analysis for Age and Income
		if 'button_state_age_income' not in st.session_state:
			st.session_state['button_state_age_income'] = True

		st.sidebar.button(
			'Age-Income Analysis',
			on_click=age_income_analysis,
			kwargs={"n_cluster": n_cluster, "df": df}
		)

		if 'button_state_prediction' not in st.session_state:
			st.session_state['button_state_prediction'] = True
		
		st.sidebar.button(
			'Prediction',
			on_click=prediction
		)
	else:
		# Flag error to the callig shell
		exit_code = -1


if __name__ == '__main__' :
	main()
