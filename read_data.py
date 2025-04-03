import streamlit as st
import pandas as pd
from db_config import get_db_connection

st.title("View Artists and Songs")

# Function to fetch data
def fetch_data(query):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)  # Get data as a dictionary for Pandas
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    return None

# Fetch and display Artists table
st.subheader("Artists")
artists_query = "SELECT * FROM artist;"
artists_data = fetch_data(artists_query)

if artists_data:
    df_artists = pd.DataFrame(artists_data)
    st.dataframe(df_artists)  # Display as interactive table
else:
    st.warning("No data found for artist.")

# Fetch and display Songs table
st.subheader("Song")
songs_query = "SELECT * FROM song;"
songs_data = fetch_data(songs_query)

if songs_data:
    df_songs = pd.DataFrame(songs_data)
    st.dataframe(df_songs)  # Display as interactive table
else:
    st.warning("No data found for song.")
