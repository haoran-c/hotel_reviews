# Sentiment Analysis on Hotel Reviews



## Dataset Information

We use and compare various different models for sentiment analysis on hotel reviews (a binary classification problem). The training dataset is expected to be a csv file containing `text,sentiment` where the `sentiment` is either `1` (positive) or `0` (negative), and `text` is the review text. 

## Requirements

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.  
* `numpy`
* `scikit-learn`
* `scipy`
* `zipcodes`
* `joblib`
* `folium`
* `requests`
* `pandas`


## Usage

### Preprocessing 

Run `normalize_data_set.py` to generate both train and test data from data folder. This will generate a preprocessed version of the dataset.

### Compare Classifiers
Run `compare_classifiers.py` it will show the accuracy results of six different models on training dataset.

### Apply to the data set
Run `predict.py` it will generate a json file, containing the name, address and applause rate of the hotels

### Visualization
Run `visualization.py` to generate an html file, which shows the choropleth map of the states

### Choropleth Map
'map.html' is now at the directory, open with any web browser to view


## Information about other files

* `data/Datafiniti_Hotel_Reviews.csv`: csv file of reviews with accurate rating
* `data/raw_data.csv`: csv file of approximately 35000 reviews from Datafiniti
