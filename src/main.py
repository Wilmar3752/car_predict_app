import streamlit as st
import requests
from _settings import all_makes, locations, CAR_PREDICT_URL, all_models, versions
import json
from utils import format_pesos_colombianos, get_info_from_ip
from db_manager import insert_data_into_database
from PIL import Image
MAKES = all_makes.keys()
DEPARTAMENTOS = locations.keys()

# Config
page_icon = Image.open('./src/assets/carro.png')
st.set_page_config(layout="centered", page_title="CAR PREDICT", page_icon=page_icon)
# Inicializar el estado de sesión si no existe
if 'etapa_actual' not in st.session_state:
    st.session_state.etapa_actual = 1

# Etapa 1: Información Personal
if st.session_state.etapa_actual == 1:
    st.title("Información Personal")
    # Lógica para recopilar información personal
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    telefono = st.text_input("Teléfono")  # Agregamos el input para el teléfono
    objetivo = st.radio(
        "¿Que quieres hacer?",
        ["Comprar", "Vender"]
    )

    st.session_state.nombre = nombre
    st.session_state.email = email
    st.session_state.telefono = telefono
    st.session_state.objetivo = objetivo
    
    # Cuando el usuario presione un botón para continuar, avanzar a la siguiente etapa
    # Botón para continuar solo habilitado si todos los campos están completos
    if st.button("Continuar") and nombre and email and telefono:  # Verificamos que todos los campos estén llenos
        st.session_state.etapa_actual += 1

# Etapa 2: Información del Vehículo
elif st.session_state.etapa_actual == 2:
    st.title("🚗 Conoce El Precio De Tu Carro 🚗")
    with st.container():
        st.markdown('<style>h1{color:#007ACC;}</style>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<style>h2{color:#007ACC;}</style>', unsafe_allow_html=True)
        st.subheader("Elige tus opciones:")
    vehicle_make = st.selectbox("🛠️ Marca del vehículo", MAKES)
    vehicle_line = st.selectbox("🔧 Línea del vehículo", all_makes[vehicle_make])
    version = st.selectbox("📌 Versión del vehículo", versions[vehicle_line])
    location_state = st.selectbox("📍 Departamento", DEPARTAMENTOS)
    if location_state == "Bogotá D.C.":
        location_city = st.selectbox("Selecciona la localidad más cercana", locations[location_state])
    else:
        location_city = st.selectbox("Selecciona la ciudad más cercana", locations[location_state])

    kilometraje = st.number_input("Ingresa el Kilometraje", value = 20000)
    vehicle_model = st.selectbox("Ingresa el modelo", all_models)

    payload = {
        "vehicle_model": vehicle_model,
        "vehicle_make": vehicle_make,
        "vehicle_line": vehicle_line,
        "version": version,
        "kilometraje": kilometraje,
        "location_city": location_city,
        "location_state": location_state
    }

    ip_data = get_info_from_ip()
    nombre = st.session_state.nombre
    email = st.session_state.email
    telefono = st.session_state.telefono
    objetivo = st.session_state.objetivo

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


