# Flight-Price-Prediction

Flight Fare predictor to travel within Indian States
To view the demo app click this link  https://flight-price-pred.herokuapp.com/



## Dataset Description
The dataset was taken from  kaggle [Flight Price Prediction](https://www.kaggle.com/datasets/jillanisofttech/flight-price-prediction-dataset). There were two datasets, one for training and other for testing .The dataset contained various columns of airlines, flight routes , flight fare , dates.

## Data Preprocessing
The date column was split into different columns for month, day , hour . Categorical columns were one hot encoded. The same techniques were applied on testing data. Feaure extraction was performed using ExtraTreesRegressor.


## Models
We trained 2 models on this dataset
1) Random Forest
2) XGBoost
 
Hyperparameter tuning was performed on both the models to get the best model. R2 score was used to measure the goodnees of fit .
XGBoost performed well on the testing dataset.

## Web App
A web app was created using flask. The web app looks like this ->

![image](https://user-images.githubusercontent.com/51293708/235329438-ef2ba386-8298-4b22-b69e-0f1452df96fb.png)

# Running the app

## Installing prerequisites
First download the trained model
```
random_model.pkl
```

download the template and static folder


download all the libraries in requirements.txt
```
 pip install -r requirements.txt
```

run the command

```
 python app.py
```

