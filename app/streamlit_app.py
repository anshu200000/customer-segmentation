import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(".."))

# Add project root to Python path so 'segmentation' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st # type: ignore
import pandas as pd

import segmentation
print(segmentation.__file__)


from segmentation.preprocess import create_rfm
from segmentation.cluster import run_kmeans
from segmentation.visualize import cluster_scatter



st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("🛍️ Customer Segmentation Dashboard")

uploaded = st.file_uploader("Upload transaction CSV", type="csv")

if uploaded:
    try:
        df = pd.read_csv(uploaded, encoding="utf-8")
    except UnicodeDecodeError:
        uploaded.seek(0)
        df = pd.read_csv(uploaded, encoding="latin1")
    st.subheader("Raw Data")
    st.dataframe(df.head())

    rfm = create_rfm(df)
    clustered, model = run_kmeans(rfm, n_clusters=4)

    st.subheader("Cluster Summary")
    st.dataframe(clustered.groupby('Cluster').mean())

    st.subheader("3D Cluster Plot")
    fig = cluster_scatter(clustered)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Customer-level Data")
    st.dataframe(clustered.reset_index())
else:
    st.info("Upload your CSV file to start analysis.")
