#Import libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import joblib




# Input title
st.title("File Input with Submit Button")

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
                df = pd.read_csv(uploaded_file)
                st.write("File contents (first 5 rows):", df.head())
                #finding_optimal_K(df)
            else:
                st.write("File type not handled in this example, but uploaded successfully.")
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.warning("Please upload a file before submitting.")


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

# Display optimal K using line graph
st.title('Finding Optimal K using KMeans Clustering')
fig, ax=plt.subplots(figsize=(8,5))
ax=plt.plot(range(1, 10), inertia, marker='o')
ax=plt.xlabel("Number of Clusters (K)")
ax=plt.ylabel("Inertia")
#plt.title("Elbow Method")
st.pyplot(fig)


#Use Silhouette score to measure how well each data point fits within its assigned cluster compared to other clusters. 
def silhouette():
    from sklearn.metrics import silhouette_score
    st.session_state['button_clicked'] = True

    X = df[["annual_income", "spending_score"]]

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    for k in range(2, 9):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(X_scaled)
        score = silhouette_score(X_scaled, labels)
        st.write(f"K = {k}, Silhouette Score = {score:.4f}")


if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

st.button('Silhouette', on_click=silhouette)

    
