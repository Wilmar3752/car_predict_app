
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

def insert_data_into_database(vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state):
    """Inserts data into the PostgreSQL database."""
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO car_prices (vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (vehicle_model, vehicle_make, vehicle_line, kilometraje, location_city, location_state)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data inserted successfully.")
    else:
        st.error("Failed to insert data.")