import streamlit as st
from db_config import get_db_connection

# Streamlit UI
st.title("MySQL Database Connection using Streamlit")

if st.button("Connect to Database"):
    conn = get_db_connection()
    if conn:
        st.success("Connected to the database successfully!")
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")  # Example query to check connection
        tables = cursor.fetchall()
        st.write("Tables in the database:", tables)
        conn.close()
    else:
        st.error("Failed to connect to the database.")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "View Data","Manage Data"])

if page == "Home":
    st.title("Welcome to the Music Streaming App")
    st.write("Use the sidebar to navigate.")

elif page == "View Data":
    import read_data  # This will run read_data.py

elif page == "Manage Data":
    import manage_data  # This runs manage_data.py
