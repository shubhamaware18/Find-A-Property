import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Viz Demo")
st.title("Page-2")


with open('df.pkl', 'rb') as file:
    df = pickle.load(file)


with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)
#st.dataframe(df)

# header for User Inputs
st.header('Enter your inputs: ')

# property_type
property_type = st.selectbox("Property Type: ", ['flat', 'house'])

# sector 
sector = st.selectbox("Sector: ",sorted(df['sector'].unique().tolist()))

# Number of BedRooms 
bedrooms = float(st.selectbox("Number of BedRooms: ",sorted(df['bedRoom'].unique().tolist())))

# Number of bathrooms 
bathroom = float(st.selectbox("Number of Bathrooms: ",sorted(df['bathroom'].unique().tolist())))

# Number of Balconies
balcony = st.selectbox('Number of Balconies: ',sorted(df['balcony'].unique().tolist()))

# agePossession
property_age = st.selectbox('Age of Property: ', df['agePossession'].unique().tolist())

# built_up_area
built_up_area = float(st.number_input('Built Up Area: '))

# servant room
servant_room = float(st.selectbox('Servant Room  Available: ',[0.0,1.0]))

# store room
store_room = float(st.selectbox('Store Room Available: ', [0.0, 1.0]))

# furnishing_type
furnishing_type = st.selectbox('furnishing_type: ', df['furnishing_type'].unique().tolist())

# luxury_category
luxury_category = st.selectbox('luxury_category: ', df['luxury_category'].unique().tolist())

# floor_category
floor_category = st.selectbox('floor_category: ', df['floor_category'].unique().tolist())

if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the flat is between {} Cr. and {} Cr.".format(round(low,2),round(high,2)))