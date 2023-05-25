#libraries
import streamlit as st
import pandas as pd
import numpy  as np

from utils import process as pc
from utils import cuisines as cs


def make_sidebar(df):
    
    st.sidebar.markdown("## Filters")

    countries = st.sidebar.multiselect(
        "Select countries to view information:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )
    
    top_n = st.sidebar.slider(
        "Select the number of restaurants you want to view:", 1, 20, 10
    )

    cuisines = st.sidebar.multiselect(
        "Select types of cuisine:",
        df.loc[:, "cuisines"].unique().tolist(),
        default=[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ],
    )

    return list(countries), top_n, list(cuisines)

st.set_page_config(page_title='Culinary Vision', layout = 'wide')

df = pc.import_dataset('zomato.csv')

countries, top_n, cuisines = make_sidebar(df)

st.markdown("# Culinary Vision")
st.markdown("#     ")

with st.container():
    st.markdown('#### Best restaurants of the main culinary types')
    col1, col2, col3, col4, col5= st.columns(5)
    
    with col1:
        top_restaurants = cs.top_cuisines (df, 'Italian')
        col1.metric(
            label = f'Italian: {top_restaurants["restaurant_name"]}',
            value = f'{top_restaurants["aggregate_rating"]}/5.0',
            help=f"""
            Country = {top_restaurants["country_name"]}\n
            City = {top_restaurants["city"]}\n
            Average cost for two: {top_restaurants["average_cost_for_two"]} ({top_restaurants["currency"]})
            """
        )
        
    with col2:
        top_restaurants = cs.top_cuisines (df, 'American')
        col2.metric(
            label = f'American: {top_restaurants["restaurant_name"]}',
            value = f'{top_restaurants["aggregate_rating"]}/5.0',
            help=f"""
            Country = {top_restaurants["country_name"]}\n
            City = {top_restaurants["city"]}\n
            Average cost for two: {top_restaurants["average_cost_for_two"]} ({top_restaurants["currency"]})
            """
        )
        
    with col3:
        top_restaurants = cs.top_cuisines (df, 'Japanese')
        col3.metric(
            label = f'Japanese: {top_restaurants["restaurant_name"]}',
            value = f'{top_restaurants["aggregate_rating"]}/5.0',
            help=f"""
            Country = {top_restaurants["country_name"]}\n
            City = {top_restaurants["city"]}\n
            Average cost for two: {top_restaurants["average_cost_for_two"]} ({top_restaurants["currency"]})
            """
        )
        
    with col4:
        top_restaurants = cs.top_cuisines (df, 'Brazilian')
        col4.metric(
            label = f'Brazilian: {top_restaurants["restaurant_name"]}',
            value = f'{top_restaurants["aggregate_rating"]}/5.0',
            help=f"""
            Country = {top_restaurants["country_name"]}\n
            City = {top_restaurants["city"]}\n
            Average cost for two: {top_restaurants["average_cost_for_two"]} ({top_restaurants["currency"]})
            """
        )

    with col5:
        top_restaurants = cs.top_cuisines (df, 'Arabian')
        col5.metric(
            label = f'Arabian: {top_restaurants["restaurant_name"]}',
            value = f'{top_restaurants["aggregate_rating"]}/5.0',
            help=f"""
            Country = {top_restaurants["country_name"]}\n
            City = {top_restaurants["city"]}\n
            Average cost for two: {top_restaurants["average_cost_for_two"]} ({top_restaurants["currency"]})
            """
        )
        
st.markdown("#     ")        
with st.container():
    st.markdown(f"#### Top {top_n} restaurants")
    data = cs.top_restaurants(df, countries, cuisines, top_n)
    st.dataframe(data)
st.markdown("#     ")

with st.container():
    best , worst = st.columns(2)
    with best:
        st.markdown(f"#### Top {top_n} highest rated cuisines")
        fig = cs.top_10_cuisines_best_rating(df, countries, cuisines, top_n)
        st.plotly_chart( fig, use_container_width=True )
               
    with worst:
        st.markdown(f"#### Top {top_n} worst rated cuisines")
        fig = cs.top_10_cuisines_worst_rating(df, countries, cuisines, top_n)
        st.plotly_chart( fig, use_container_width=True )
    