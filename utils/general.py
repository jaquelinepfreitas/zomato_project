#libraries
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def create_map(df):
    df_aux = (df.loc[:, ['latitude','longitude', 'city', 'country_name']]
                .groupby(['country_name','city'])
                .median()
                .reset_index())

    map = folium.Map ( zoom_start=11 )
    for index, location_info in df_aux.iterrows():
        folium.Marker( [location_info['latitude'],
                        location_info['longitude']],
                        popup=location_info[['country_name','city']] ).add_to( map )
    folium_static(map, width=1024 ,height=600)
    return None

#Overview
def qty_countries(df):
    return df.loc[:, 'country_name'].nunique()

def qty_cities(df):
    return df.loc[:, 'city'].nunique()

def qty_restaurants(df):
    return df.loc[:, 'restaurant_name'].nunique()

def qty_ratings(df):
    return df.loc[:, 'votes'].sum()

def qty_cuisines(df):
    return df.loc[:, 'cuisines'].nunique()
