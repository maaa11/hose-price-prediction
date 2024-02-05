import numpy as np
import pickle
import streamlit as st
import joblib

#from PIL import Image

# Load the trained model
loaded_model = joblib.load(open('C:/Users/Default user.E5AD/Desktop/zzzzzzzzzz/model.pkl', 'rb'))

def predict_Prices(input_data):
    #input_data = np.asarray(features)
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
   ## return prediction 
    if (prediction[0] == 0):
      return('سعر العقار منخفض')
    else:
      return('سعر العقار مرتفع')


def main():
    st.set_page_config(layout="wide") 
    # تعيين الشريط الجانبي لليسار
    st.title('House Price Prediction')
    st.sidebar.header('House Price Prediction')
    size = st.number_input('Enter the size: ')
    elevator = st.number_input('Select the elevator:')
    fireplace = st.number_input('Select the fireplace:')
    stairs = st.number_input('Select the stairs:')
    pool = st.number_input('Select the pool:')
    driver_room = st.number_input('Select the driver room:')
    garage = st.number_input('Select the garage:')
    kitchen = st.number_input('Select the kitchen: ')
    bedrooms = st.number_input('Select the bedrooms: ')
    district = st.number_input('Enter the district: ')
    city = st.number_input('Select the city:')
    property_age = st.number_input('Enter the property age:', step=1, min_value=0, max_value=35)

    # Code for prediction
    Prices = ''
    if st.button('Predict Price'):
        Prices = predict_Prices([size, elevator, fireplace, stairs, pool,garage, driver_room, kitchen, bedrooms, district, city, property_age])
    st.success(Prices)



if __name__ == '__main__':
    main()
