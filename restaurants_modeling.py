#Read in libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
from statistics import mode
from shapely.geometry import Point, Polygon
from sklearn.cluster import KMeans, AgglomerativeClustering

#Read in cleaned input
df = pd.read_csv(r'restaurants\restaurant_output.csv')

#Re-order columns by name
df = df.reindex(columns=['geometry','placeID','latitude','longitude','city','state','smoking','dress_code','accessibility',
                         'price','franchise','open_area','cash_only','cuisine','weekday','parking','full_bar','alcohol_served',
                        'valet','international','fast_casual','open_early','open_late','close_early','close_late'])

#Convert back to geopandas dataframe
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))


#### K-Means Section ####

#Use elbow method to determine optimal k
intert = [] 
k_count = range(1,50,2)
for x in k_count:
    kmeanModel = KMeans(n_clusters=x)
    kmeanModel.fit_predict(gdf[gdf.columns[4:25]])
    intert.append(kmeanModel.inertia_)
    
#Plot elbow method results
plt.figure(figsize=(16,8))
plt.plot(k_count, intert, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()


#Initialize model
cluster=KMeans(n_clusters=5)
#Fit to dataset, use 4:25 to ignore locational values
gdf['k_means'] = cluster.fit_predict(gdf[gdf.columns[4:25]])

#Plot output
gdf.plot(column='k_means', legend=True)



#### Hierarchical Clustering Section ####

#Repeated for multiple different linkage methods and 'cutting' cluster at various points
#Initialize model
cluster=AgglomerativeClustering(n_clusters=40, linkage = 'single')
#Fit to dataset, use 0:20 to ignore Street
gdf['single'] = cluster.fit_predict(gdf[gdf.columns[4:25]])

#Plot output 
gdf.plot(column='k_means', legend=True)
