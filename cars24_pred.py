import pandas as pd
import streamlit as st
import datetime

import pickle

cars_df=pd.read_csv("cars24-car-price.csv")



encode_dict ={
    "fuel_type": {"Diesel":1,"Petrol":2,"Cng":3,"Lpg":4,"Electric":5},
    "seller_type": {"Dealer":1,"Individual":2,"Trustmark dealer":3},
    "transmission_type":{"Manual":1,"Automatic":2}
}

def model_pred(fuel_type,transmission_type,engine,seats):
    # loading the model
    with open("car_pred","rb") as files:
        reg_model=pickle.load(files)
    input_feature=[[2018.0,1,40000,fuel_type,transmission_type,19.70,engine,18.36,seats]]
    return reg_model.predict(input_feature)

# here fuel type,Transmission,seats  will be drop down
# engine power will be slider type

col1,col2=st.columns(2)
fuel_type=col1.selectbox("select the fuel type",
                         ["Diesel","Petrol","Cng","Lpg","Electric"])

engine=col1.slider("set the engine power",
                   500,5000,step=100) # start,end,step size

transmission_type=col2.selectbox("Select transmission type",
                                 ['Manual','Automatic'])

seats= col2.selectbox("No. of seats",[4,5,6,7])

# we will add button which will make the thing load for making the load happens
if (st.button("Predict Price")):

    fuel_type=encode_dict["fuel_type"][fuel_type]
    transmission_type=encode_dict["transmission_type"][transmission_type]

    price=model_pred(fuel_type,transmission_type,engine,seats)
    st.text("Predicted price of the car :"+str(price))
st.write("""
        ## Cars24 use for price Predict
        """)
st.dataframe(cars_df.head())
