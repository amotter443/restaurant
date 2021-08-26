# restaurant
An intro ML project using unsupervised Machine Learning to cluster restaurants based on geographic location.


Who is this project for?
------------------------
- Beginner data scientists looking to familiarize themselves with basic clustering 
- Early analytics/data science students looking to dip their toes into unsupervised learning
- Data science educators looking for foundational projects to teach their students


Usage
------------------------
- Read the input data files (`geoplaces2.csv`,`chefmozaccepts.csv`,`chefmozcuisine.csv`,`chefmozhours4.csv`,`chefmozparking.csv`) into your environment
- Familiarize yourself with the below data dictionary
- Follow the steps to read in data and perform basic cleaning in `restaurants_cleaning.py`
- _Note: geopandas can provide some issues with downloading (I have a Windows, pip env for Python 3.7) because of the fiona library dependency. What worked for me was downloading the proper version of fiona's depdency GDAL https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal, download the proper version of fiona https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona, then pip install geopandas_
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

