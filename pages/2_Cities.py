#libraries
import streamlit as st
import pandas as pd
import numpy  as np

from utils import process as pc
from utils import cities as ct

st.set_page_config(page_title='City Vision',layout = 'wide')

def make_sidebar(df):
    
    st.sidebar.markdown("## Filters")

    countries = st.sidebar.multiselect(
        "Select countries to view information:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )
    return list(countries)

df = pc.import_dataset('zomato.csv')

countries = make_sidebar(df)

st.markdown("# City Vision")
st.markdown("#     ")

with st.container():
    fig = ct.restaurants_by_cities(df, countries)
    st.markdown('##### Top 10 cities with more registered restaurants')
    st.plotly_chart( fig, use_container_width=True )
    
with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('##### Restaurants with table booking')
        fig = ct.booking_by_city(df, countries)
        st.plotly_chart(fig)

    with col2:
        st.markdown('##### Online ordering restaurants')
        fig = ct.online_order_by_city(df, countries)
        st.plotly_chart(fig)

    with col3:
        st.markdown('##### Restaurants that deliver')
        fig = ct.delivery_by_city(df, countries)
        st.plotly_chart(fig)
        
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('##### Top 10 cities with an average score above 4')
        fig = ct.top_10_above_4 (df, countries)
        st.plotly_chart( fig, use_container_width=True )
    
    with col2:
        st.markdown('##### Top 10 cities with an average score below 2.5')
        fig = ct.top_10_below_2 (df, countries)
        st.plotly_chart( fig, use_container_width=True )
        
with st.container():
        st.markdown('##### Top 10 cities with the most different types of cuisine')
        fig = ct.cities_with_cuisines (df, countries)
        st.plotly_chart( fig, use_container_width=True )
