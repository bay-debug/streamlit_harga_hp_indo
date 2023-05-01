import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_hp_indo.sav', 'rb'))

st.title('Estimasi Harga Hp Indonesia ')

internal_storage = st.number_input('Input Penyimpanan Internal')
memory = st.number_input('Input Ram')
refesh_rate = st.number_input('Input refesh_rate layar')
battery = st.number_input('Input Baterai')
display_size = st.number_input('Input Ukuran Layar')



predict = ''

if st.button('Estimasi Harga Handphone'):
    predict = model.predict(
        [[internal_storage, memory, refesh_rate,battery,display_size]]
    )
    st.write ('Estimasi harga 1 Unit Handphone ($): ', predict)
    st.write ('Estimasi harga 1 Unit Handphone IDR (Rp) :', predict*15000)