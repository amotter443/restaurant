# restaurant
An intro ML project using unsupervised Machine Learning to cluster restaurants based on geographic location.


I chose to work on this project because it integrated two areas I previously had worked with disparately but never together: geospatial analytics and unsupervised machine learning. Selecting the optimal quantity of clusters and tuning hyperparameters is an imprecise science that requires both intuition and integration of statistical theories like the bias-variance tradeoff. Given I had an upcoming project integrating these two areas of data science together, this provided an opportunity to refresh these skills and utilize them together in a new way.


Who is this project for?
------------------------
- Beginner data scientists looking to familiarize themselves with basic clustering 
- Early analytics/data science students looking to dip their toes into unsupervised learning
- Data science educators looking for foundational projects to teach their students


Usage
------------------------
- Download the [Kaggle file](https://www.kaggle.com/uciml/restaurant-data-with-consumer-ratings)
- Read the input data files (`geoplaces2.csv`,`chefmozaccepts.csv`,`chefmozcuisine.csv`,`chefmozhours4.csv`,`chefmozparking.csv`) into your environment
- Familiarize yourself with the below data dictionary
- Follow the steps to read in data and perform basic cleaning in `restaurants_cleaning.py`
- _Note: geopandas can prove challenging to download (I have a Windows, pip env for Python 3.7) primarily due to the fiona library dependency. What worked for me was downloading the proper version of fiona's dependency [GDAL](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal), downloading the proper version of [fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona), then pip install geopandas_
- Execute the modeling code in `restaurants_modeling.py`


Data Dictionary
------------------------
- `placeID` -- Unique ID value for the restaurant in the larger restaurant data
- `latitude` -- Latitude of the restaurant's address online 
- `longitude` -- Longitude of the restaurant's address online 
- `city` -- City where the restaurant is located within  
- `state` -- State where the restaurant is located within  
- `smoking` -- Boolean feature indicating whether smoking is allowed in the restaurant   
- `dress code` -- Categorical feature indicating how formal the dress code is in the restaurant (Casual = 0, Informal = 1, Formal = 2)  
- `accessibility` -- Boolean feature indicating whether the restaurant is accessible to people of differing abilities
- `price` -- Categorical feature indicating how pricey the restaurant is (Low = 0, Medium = 1, High = 2)
- `franchise` -- Boolean feature indicating whether the restaurant is freestanding or a franchised location
- `open_area` -- Boolean feature indicating whether the restaurant is a closed or open area
- `cash_only` -- Boolean feature indicating whether the restaurant only takes cash or not
- `cuisine` -- Categorical feature indicating the cuisine of the restaurant from an extensive list of restaurant genres
- `weekday` -- Boolean feature indicating whether the restaurant is only open on the weekdays or not
- `parking` -- Boolean feature indicating whether parking is available in the restaurant
- `full_bar` -- Boolean feature indicating whether the restaurant has a full bar or not 
- `alcohol_served` -- Boolean feature indicating whether the restaurant serves alcohol not 
- `valet` -- Boolean feature indicating whether valet parking is available at the restaurant
- `fast_casual` -- Boolean feature indicating whether the restaurants cuisine is based in the cuisine of another country
- `fast_casual` -- Boolean feature indicating whether the restaurants cuisine is fast casual style
- `open_early` -- Boolean feature indicating whether the restaurant opens early, defined as before 9am  
- `open_late` -- Boolean feature indicating whether the restaurant opens late, defined as after 1pm  
- `close_early` -- Boolean feature indicating whether the restaurant closes early, defined as before 8pm  
- `close_late` -- Boolean feature indicating whether the restaurant closes late, defined as after 10pm  



Project Applications:
------------------------
- The contents of this dataset are very interesting; however, only a limited amount of the data contains coordinates. This project might benefit from focusing more narrowly on the larger restaurant and review data without the geospatial component.
- Similarly, the geospatial clustering aspect could be applied to a more robust dataset with more records containing latitude and longitude values. Other datasets with a locational component, including even other retail spaces that might have address or location data could provide more useful for this use case. Given the free and somewhat cleaned nature of this data, however, another project might require scraping or more challenges to prepare.
- Expanding the data to add more restaurants with the same fields would provide a larger body of data to analyze. Because only a handful of Mexican cities had locational data, expanding the data to include more cities and cuisines would heed to not only more robust clusters but also more usable insights from the research.
