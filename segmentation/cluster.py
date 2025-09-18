from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def run_kmeans(rfm, n_clusters=4):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(rfm)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    rfm['Cluster'] = labels
    return rfm, kmeans