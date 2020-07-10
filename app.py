from flask import Flask,request,render_template
import pickle
import sklearn
from flask_cors import cross_origin
import pandas as pd
import numpy as np 
app = Flask(__name__)

model = pickle.load(open("random_model.pkl","rb"))


@app.route('/')
@cross_origin()
def home():
    return render_template("home.html")

@app.route('/predict',methods=[ 'GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        #Date of Journey
        date_dep = request.form['Dep_Time']
        Journey_Day = int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").day)
        Journey_Month = int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").month)
        
        #Departure
        Dep_Hour = int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").minute)

        #Arrival
        arrival_date = request.form['Arrival_Time']
        Arrival_Hour = int(pd.to_datetime(arrival_date,format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arrival_date,format="%Y-%m-%dT%H:%M").minute)

        #Duration
        Duration_hours = abs(Arrival_Hour-Dep_Hour)
        Duration_mins = abs(Arrival_min-Dep_min)

        #Total Stops
        Total_Stops = int(request.form['stops'])

        #Source
        Source = request.form['Source']
        if (Source == 'Delhi'):
            source_Delhi = 1
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0

        elif (Source == 'Kolkata'):
            source_Delhi = 0
            source_Kolkata = 1
            source_Mumbai = 0
            source_Chennai = 0

        elif (Source == 'Mumbai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 1
            source_Chennai = 0

        elif (Source == 'Chennai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 1

        else:
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0

        #Destination
        #Bangalore = 0 (not in column)
        Destination = request.form['Destination']
        if(Destination == "Cochin"):
            des_Cochin = 1
            des_Delhi = 0
            des_New_Delhi = 0
            des_Hyderabad = 0
            des_Kolkata = 0
        elif (Destination == "Delhi"):
            des_Cochin = 0
            des_Delhi = 1
            des_New_Delhi = 0
            des_Hyderabad = 0
            des_Kolkata = 0
        elif (Destination == "New Delhi"):
            des_Cochin = 0
            des_Delhi = 0
            des_New_Delhi = 1
            des_Hyderabad = 0
            des_Kolkata = 0
        elif (Destination == "Hyderabad"):
            des_Cochin = 0
            des_Delhi = 0
            des_New_Delhi = 0
            des_Hyderabad = 1
            des_Kolkata = 0
        elif (Destination == "Kolkata"):
            des_Cochin = 0
            des_Delhi = 0
            des_New_Delhi = 0
            des_Hyderabad = 0
            des_Kolkata = 1
        else:
            des_Cochin = 0
            des_Delhi = 0
            des_New_Delhi = 0
            des_Hyderabad = 0
            des_Kolkata = 0

        #Airline
        #Air Asia = 0 (not in column)
        Airline = request.form['airline']
        if (Airline == "Jet Airways"):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "Indigo"):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "Air India"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "Multiple carriers"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "SpiceJet"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "Vistara"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "GoAir"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif (Airline == "Multiple carriers Premium economy"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0  
        elif (Airline == "Jet Airways Business"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif (Airline == "Vistara Premium economy"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0 
        elif (Airline == "Trujet"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

    
        
        
        
        prediction = model.predict([[
            Total_Stops,
            Journey_Day,
            Journey_Month,
            Dep_Hour,
            Dep_min,
            Arrival_Hour,
            Arrival_min,
            Duration_hours,
            Duration_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            source_Chennai,
            source_Delhi,
            source_Kolkata,
            source_Mumbai,
            des_Cochin,
            des_Delhi,
            des_Hyderabad,
            des_Kolkata,
            des_New_Delhi]])

        price = round(prediction[0],2)
        return render_template("home.html",prediction_text="Your Flight Fare is {} Rs.".format(price))
    else:
        return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)