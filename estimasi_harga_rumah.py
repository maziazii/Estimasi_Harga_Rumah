import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah')

SquareFeet = st.number_input('Input Luas Rumah')
Bedrooms = st.number_input('Input Jumalah Kamar Tidur')
Bathrooms = st.number_input('Input Jumlah Kamar Mandi')
YearBuilt = st.number_input('Input Tahun Pembangunan Rumah')

predict = ''

if st.button('Estimasi Harga Rumah'):
    predict = model.predict([[SquareFeet, Bedrooms, Bathrooms, YearBuilt]])

    st.write('Estimasi Harga Rumah: ', predict)