import mysql.connector
import streamlit as st

# Function to connect to MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="music-streaming-service"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None


