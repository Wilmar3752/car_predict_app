import streamlit as st
import requests
from _settings import all_makes, locations, CAR_PREDICT_URL
import json
from babel.numbers import format_currency

def format_pesos_colombianos(value):
    """
    Formatea un valor numérico a una cadena representando pesos colombianos sin decimales.
    
    Args:
    value (float): El valor numérico a formatear.
    
    Returns:
    str: La cadena formateada.
    """
    return format_currency(int(round(value, 0)), 'COP', locale='es_CO', format='#,##0')

MAKES = all_makes.keys()
DEPARTAMENTOS = locations.keys()

st.title("ML Prediction App")
vehicle_make = st.selectbox("Select vehicle brand", MAKES)
vehicle_line = st.selectbox("select line", all_makes[vehicle_make])
location_state = st.selectbox("Selecciona tu departamento o el más cercano", DEPARTAMENTOS)
if location_state == "Bogotá D.C.":
    location_city = st.selectbox("Selecciona la localidad más cercana", locations[location_state])
else:
    location_city = st.selectbox("Selecciona la ciudad más cercana", locations[location_state])

kilometraje = st.number_input("Ingresa el Kilometraje")
vehicle_model = st.number_input("Ingresa el modelo")

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
        st.success(f'El precio de este vehículo es ${formatted_price}')
