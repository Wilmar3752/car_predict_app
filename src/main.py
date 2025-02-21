import streamlit as st
import requests
from _settings import all_makes,all_makes_motos, CAR_PREDICT_URL, all_models, MOT_PREDICT_URL
import json
from utils import format_pesos_colombianos, get_info_from_ip
from db_manager import insert_data_into_database
from footer import add_footer
from PIL import Image
MAKES = all_makes.keys()
MAKES_MOTOS = all_makes_motos.keys()


# Config
page_icon = Image.open('./src/assets/carro.png')
st.set_page_config(layout="centered", page_title="CAR PREDICT", page_icon=page_icon)

st.title("CONOCE EL PRECIO DE TU VEHÍCULO")
with st.container():
    st.markdown('<style>h1{color:#007ACC;}</style>', unsafe_allow_html=True)

with st.container():
    st.markdown('<style>h2{color:#007ACC;}</style>', unsafe_allow_html=True)
    st.subheader("Elige tus opciones:")

# Crear tabs principales
carros_tab, motos_tab = st.tabs(["🚗 Carros","🛵 Motos"])

# Contenido para motos
with carros_tab:
    with st.container():
        st.markdown('<style>h2{color:#007ACC;}</style>', unsafe_allow_html=True)

    vehicle_make = st.selectbox("🛠️ Marca del vehículo", MAKES)
    vehicle_line = st.selectbox("🔧 Línea del vehículo", all_makes[vehicle_make].keys())
    version = st.selectbox("📌 Versión del vehículo", all_makes[vehicle_make][vehicle_line])
    kilometraje = st.number_input("Ingresa el Kilometraje", value = 20000)
    vehicle_model = st.selectbox("Ingresa el modelo", all_models)

    payload = {
        "vehicle_model": vehicle_model,
        "vehicle_make": vehicle_make,
        "vehicle_line": vehicle_line,
        "version": version,
        "kilometraje": kilometraje,
    #    "location_city": location_city,
    #    "location_state": location_state
    }

    ip_data = get_info_from_ip()
    nombre = "default"
    email = "default"
    telefono = "default"
    objetivo = "default"
    location_city = "default"
    location_state = "default"

    if st.button("Predict"):
        with st.spinner('Procesando...'):
            # Realizar la solicitud POST
            response = requests.post(CAR_PREDICT_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
            price = response.json()['expected_price']
            price_print = format_pesos_colombianos(price)
                # Asegúrate de tener una función para formatear el precio si es necesario
            st.success(f'El precio de este vehículo es ${price_print}')
            insert_data_into_database(nombre, email, telefono, objetivo, 
                            vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state, price,
                            ip=ip_data['ip'], ip_city=ip_data['city'], ip_state=ip_data['region'], ip_org=ip_data['org'],
                            ip_postal=ip_data['postal'], version=version)
            
with motos_tab:
    with st.container():
        st.markdown('<style>h2{color:#007ACC;}</style>', unsafe_allow_html=True)

    moto_make = st.selectbox("🛠️ Marca de la moto", MAKES_MOTOS)
    moto_line = st.selectbox("🔧 Línea del vehículo", all_makes_motos[moto_make].keys())
    moto_cilindraje = st.selectbox("📌 Cilindraje", all_makes_motos[moto_make][moto_line])
    moto_kilometraje = st.number_input("Kilometraje", value = 20000)
    moto_model = st.selectbox("Modelo", all_models)

    payload_motos = {
    "vehicle_model": moto_model,
    "vehicle_make": moto_make,
    "vehicle_line": moto_line,
    "kilometraje": moto_kilometraje,
    "cilindraje": moto_cilindraje
        }
    if st.button("Predict moto"):
        with st.spinner('Procesando...'):
            # Realizar la solicitud POST
            response = requests.post(MOT_PREDICT_URL, data=json.dumps(payload_motos), headers={'Content-Type': 'application/json'})
            price = response.json()['expected_price']
            price_print = format_pesos_colombianos(price)
                # Asegúrate de tener una función para formatear el precio si es necesario
            st.success(f'El precio de este vehículo es ${price_print}')
            insert_data_into_database(nombre, email, telefono, objetivo, 
                            moto_model, moto_make, moto_line, moto_kilometraje, location_city, location_state, price,
                            ip=ip_data['ip'], ip_city=ip_data['city'], ip_state=ip_data['region'], ip_org=ip_data['org'],
                            ip_postal=ip_data['postal'], version=moto_cilindraje)
add_footer()