#libraries
import streamlit as st
import pandas as pd

from utils import process as pc
from utils import country as cn

st.set_page_config(page_title='Country Vision', layout = 'wide')

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

st.markdown("# Country Vision")
st.markdown("#     ")

st.markdown('##### Cities registered by country')
fig = cn.cities_by_country(df, countries)
st.plotly_chart(fig, use_container_width=True)

st.markdown('##### Restaurants registered by country')
fig = cn.restaurant_by_country (df, countries)
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns( 2 )
with col1:
    tab = cn.cuisines_by_country (df, countries)
    st.markdown('##### Number of culinary type by country')
    st.dataframe(tab)

    
with col2:
    tab = cn.common_cuisines (df, countries)
    st.markdown('##### Number of countries by culinary type')
    st.dataframe(tab)

fig = cn.rating_made_by_country (df, countries)
st.markdown('##### Number of ratings registered by country')
st.plotly_chart(fig, use_container_width=True)

fig = cn.rating_by_country (df,countries)
st.markdown('##### Average rating by country')
st.plotly_chart(fig, use_container_width=True)