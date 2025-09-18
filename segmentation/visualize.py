import plotly.express as px

def cluster_scatter(rfm):
    # Ensure marker size is always positive
    rfm_plot = rfm.copy()
    rfm_plot['Monetary_abs'] = rfm_plot['Monetary'].abs()
    fig = px.scatter_3d(
        rfm_plot.reset_index(),
        x='Recency', y='Frequency', z='Monetary',
        color='Cluster', symbol='Cluster',
        size='Monetary_abs',  # Use absolute value for size
        hover_data=['CustomerID']
    )
    return fig