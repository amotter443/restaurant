#Read in libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
from statistics import mode

#Read in data files
re1 = pd.read_csv(r'restaurants\geoplaces2.csv')
re2 = pd.read_csv(r'restaurants\chefmozaccepts.csv')
re3 = pd.read_csv(r'restaurants\chefmozcuisine.csv')
re4 = pd.read_csv(r'restaurants\chefmozhours4.csv')
re5 = pd.read_csv(r'restaurants\chefmozparking.csv')

#Merge into singular df
#df = re1.merge(re2, how='left', on='placeID')
df = re1.join(re2, lsuffix="DROP").filter(regex="^(?!.*DROP)")
df = df.join(re3, lsuffix="DROP").filter(regex="^(?!.*DROP)")
df = df.join(re4, lsuffix="DROP").filter(regex="^(?!.*DROP)")
df = df.join(re5, lsuffix="DROP").filter(regex="^(?!.*DROP)")


#Convert to geopandas df 
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
#Remove old dfs
del df,re1,re2,re3,re4,re5


#Drop useless columns 
gdf.drop(['the_geom_meter','country','fax','name','address','zip','Rambience','other_services','url'], axis=1, inplace=True)

#Convert ? to NA
gdf = gdf.replace({'?':np.NAN})

#NA count by column
print(gdf.apply(lambda a: a.isnull().sum(),axis=0).sort_values())


#### Cleaning Section ####
gdf.loc[gdf['dress_code']=="casual",'dress_code'] = 0
gdf.loc[gdf['dress_code']=="informal",'dress_code'] = 1
gdf.loc[gdf['dress_code']=="formal",'dress_code'] = 2

gdf.loc[gdf['accessibility']=="no_accessibility",'accessibility'] = 0
gdf.loc[gdf['accessibility']=="partially",'accessibility'] = 0.5
gdf.loc[gdf['accessibility']=="completely",'accessibility'] = 1

gdf.loc[gdf['price']=="low",'price'] = 1
gdf.loc[gdf['price']=="medium",'price'] = 2
gdf.loc[gdf['price']=="high",'price'] = 3

gdf.loc[gdf['franchise']=="f",'franchise'] = 0
gdf.loc[gdf['franchise']=="t",'franchise'] = 1

gdf.rename(columns={'area':'open_area'}, inplace=True)
gdf.loc[gdf['open_area']=="closed",'open_area'] = 0
gdf.loc[gdf['open_area']=="open",'open_area'] = 1

gdf.rename(columns={'smoking_area':'smoking'}, inplace=True)
gdf.loc[gdf['smoking']=="not_permitted",'smoking'] = 0
gdf.loc[gdf['smoking']!=0,'smoking'] = 1

gdf.rename(columns={'Rpayment':'cash_only'}, inplace=True)
gdf.loc[gdf['cash_only']=="cash",'cash_only'] = 1
gdf.loc[gdf['cash_only']!=1,'cash_only'] = 0

gdf['full_bar'] = 0
gdf.loc[gdf['alcohol']=="Full_Bar",'full_bar'] = 1
gdf['alcohol_served'] = 1
gdf.loc[gdf['alcohol']=="No_Alcohol_Served",'alcohol_served'] = 0
gdf.drop(['alcohol'], axis=1, inplace=True)

gdf.rename(columns={'days':'weekday'}, inplace=True)
gdf.loc[gdf['weekday']=="Mon;Tue;Wed;Thu;Fri;",'weekday'] = 1
gdf.loc[gdf['weekday']!=1,'weekday'] = 0

gdf['valet'] = 0
gdf.loc[gdf['parking_lot']=="valet parking",'valet'] = 1
gdf.rename(columns={'parking_lot':'parking'}, inplace=True)
gdf.loc[gdf['parking']=="none",'parking'] = 0
gdf.loc[gdf['parking']!=0,'parking'] = 1

gdf.loc[gdf.city.isin(["s.l.p.","S.L.P.","s.l.p","SLP","slp","san luis potosi","san luis potosi ","san luis potos"]),'city'] = 'San Luis Potosi'
gdf.loc[gdf.city.isin(["Cd Victoria","Cd. Victoria","Ciudad Victoria","victoria","victoria "]),'city'] = 'Victoria'
gdf.loc[gdf.city.isnull(),"city"] = mode(gdf.city)

gdf.loc[gdf.state.isin(["s.l.p.","S.L.P.","San Luis Potosi","san luis potosi","san luis potos"]),'state'] = 'SLP'
gdf.loc[gdf['state']=="mexico",'state'] = np.nan
gdf.loc[gdf['state']=="tamaulipas",'state'] = 'Tamaulipas'
gdf.state = gdf.state.str.replace(' ','')
gdf['state']= gdf['state'].fillna(gdf.groupby('city')['state'].transform(mode))


gdf.rename(columns={'Rcuisine':'cuisine'}, inplace=True)
gdf.loc[gdf['cuisine']=="Brazilian",'cuisine'] = 'Latin_American'
gdf.loc[gdf['cuisine']=="Steaks",'cuisine'] = 'Contemporary'
gdf.loc[gdf.cuisine.isin(["Chinese","Japanese","Mongolian","Sushi"]),'cuisine'] = 'Asian'
gdf.loc[gdf.cuisine.isin(["Bar","Bar_Pub_Brewery","Burgers","Cafe-Coffee_Shop","Cafeteria","Deli-Sandwiches","Diner","Hot_Dogs","Fast_Food","Pizzeria"]),'cuisine'] = 'Fast_Casual'
gdf['international'] = 0
gdf.loc[gdf.cuisine.isin(["Asian","International","Italian","Latin_American","Mediterranean","Mexican","Spanish"]),'international'] = 1
gdf['fast_casual'] = 0
gdf.loc[gdf['cuisine']=="Fast_Casual",'fast_casual'] = 1


gdf.hours = gdf.hours.str.replace(':','')
gdf.loc[gdf['hours']=="0000-0000;",'hours'] = '30-30'
gdf[['open_time','close_time']] = gdf.hours.str.split("-",expand=True)
gdf.close_time = gdf.close_time.str.replace(';','')
gdf.drop(['hours'], axis=1, inplace=True)
gdf.loc[gdf['open_time']=='30','open_time'] = np.nan
gdf.loc[gdf['close_time']=='30','close_time'] = np.nan
gdf['open_time']= gdf['open_time'].fillna(mode(gdf['open_time']))
gdf['close_time']= gdf['close_time'].fillna(mode(gdf['close_time']))

gdf['open_early'] = np.where(gdf['open_time']<='0900',1,0)
gdf['open_late'] = np.where(gdf['open_time']>='1300',1,0)
gdf['close_early'] = np.where(gdf['close_time']<='2000',1,0)
gdf['close_late'] = np.where(gdf['close_time']>='2200',1,0)
gdf.drop(['open_time','close_time'], axis=1, inplace=True)

#Re-code string features to numeric
gdf['city'] = gdf['city'].astype('category')
gdf['city'] = gdf['city'].cat.codes + 1
gdf['state'] = gdf['state'].astype('category')
gdf['state'] = gdf['state'].cat.codes + 1
gdf['cuisine'] = gdf['cuisine'].astype('category')
gdf['cuisine'] = gdf['cuisine'].cat.codes + 1

#Output to file
gdf.to_csv(r'restaurants\restaurant_output.csv', index=False, header=True)