
from _settings import DATABASE_CONFIG
import psycopg2
import streamlit as st

def connect_to_database():
    """Connects to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data_into_database(nombre, email, telefono , objetivo,  #personal
                              vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state, price,#vehiculo
                              ip, ip_city, ip_state, ip_org, ip_postal, version):
    """Inserts data into the PostgreSQL database."""
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO car_prices (nombre, email, telefono, objetivo, 
                                vehicle_model, vehicle_make, vehicle_line ,kilometraje, location_city, location_state, expected_price,
                                ip, ip_city, ip_state, ip_org, ip_postal, version)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (nombre, email, telefono, objetivo, 
                  vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state, price,
                  ip, ip_city, ip_state, ip_org, ip_postal, version)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        st.error("Failed to insert data.")