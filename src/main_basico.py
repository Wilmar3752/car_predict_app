import streamlit as st
import requests
from _settings import all_makes, locations, CAR_PREDICT_URL
import json
from utils import format_pesos_colombianos, client_ip, get_user_agent, get_screen_resolution
from db_manager import insert_data_into_database

MAKES = all_makes.keys()
DEPARTAMENTOS = locations.keys()

st.title("Conoce el precio de tu carro")
vehicle_make = st.selectbox("Selecciona la marca del vehiculo", MAKES)
vehicle_line = st.selectbox("Selecciona la línea", all_makes[vehicle_make])
location_state = st.selectbox("Selecciona tu departamento o el más cercano", DEPARTAMENTOS)
if location_state == "Bogotá D.C.":
    location_city = st.selectbox("Selecciona la localidad más cercana", locations[location_state])
else:
    location_city = st.selectbox("Selecciona la ciudad más cercana", locations[location_state])

kilometraje = st.number_input("Ingresa el Kilometraje", value=10_000)
vehicle_model = st.number_input("Ingresa el modelo", value = 2023)

ip = client_ip()
user = get_user_agent()

payload = {
    "vehicle_model": vehicle_model,
    "vehicle_make": vehicle_make,
    "vehicle_line": vehicle_line,
    "kilometraje": kilometraje,
    "location_city": location_city,
    "location_state": location_state
}


if st.button("Predict"):
    with st.spinner('Procesando...'):
        # Realizar la solicitud POST
        response = requests.post(CAR_PREDICT_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        
        price = response.json()['expected_price']
        formatted_price = format_pesos_colombianos(price)
        # Insert data into the database
        insert_data_into_database(vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state)
        st.success(f'El precio sugerido de este vehículo es ${formatted_price}')
