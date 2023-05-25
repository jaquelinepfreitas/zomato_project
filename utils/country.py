import pandas as pd
import plotly.express as px
from PIL import Image

def cities_by_country (df, countries):
    
    
    df_aux = (df.loc[df["country_name"].isin(countries), ['country_name', 'city']]
                                       .groupby('country_name')
                                       .nunique()
                                       .sort_values('city', ascending = False )
                                       .reset_index())
    fig = px.bar(
        df_aux, 
        x = 'country_name', 
        y = 'city', 
        text = 'city', 
        labels={
        "country_name": "Countries",
        "city": "Number of Cities",
        }, 
        color_discrete_sequence=px.colors.qualitative.D3)

    return fig

def restaurant_by_country (df, countries):
    df_aux = (df.loc[df['country_name'].isin(countries), ['country_name', 'restaurant_id']]
                                       .groupby('country_name')
                                       .nunique()
                                       .sort_values('restaurant_id', ascending = False )
                                       .reset_index())
    fig = px.bar(
        df_aux, 
        x = 'country_name', 
        y = 'restaurant_id', 
        text = 'restaurant_id', 
        labels={
        "country_name": "Countries",
        "restaurant_id": "Number of Restaurants",
        },
        color_discrete_sequence=px.colors.qualitative.D3)
    return fig
    
def cuisines_by_country (df, countries):
    df_aux = (df.loc[df['country_name'].isin(countries), ['country_name', 'cuisines']]
                .groupby('country_name')
                .nunique()
                .sort_values('cuisines', ascending = False )
                .reset_index())
    df_aux.columns = ['Country', 'Number of Culinary type']
    return df_aux.head(15)

def common_cuisines (df, countries):
    df_aux = (df.loc[df['country_name'].isin(countries), ['country_name', 'cuisines']].groupby('cuisines')
                                                    .nunique()
                                                    .sort_values('country_name', ascending = False )
                                                    .reset_index())
    df_aux.columns = ['Culinary type', 'Number of Countries']
    return df_aux.head(15)

def rating_made_by_country (df, countries):
    df_aux = (df.loc[df['country_name'].isin(countries), ['country_name', 'votes']].groupby('country_name')
                                                  .mean()
                                                  .sort_values('votes', ascending = False )
                                                  .reset_index())
    fig = px.bar(
        df_aux, 
        x = 'country_name', 
        y = 'votes', 
        text = 'votes', 
        text_auto=".1f",
        labels={
        "country_name": "Countries",
        "city": "Number of Ratings",
        }, 
        color_discrete_sequence=px.colors.qualitative.D3)

    return fig

def rating_by_country (df, countries):    
    df_aux = (df.loc[df['country_name'].isin(countries), ['aggregate_rating', 'country_name']].groupby('country_name')
                                                             .mean()
                                                             .sort_values('aggregate_rating', ascending = False)
                                                             .reset_index())
    fig =px.line( 
        df_aux, 
        x='country_name', 
        y='aggregate_rating', 
        labels={
        "country_name": "Countries",
        "aggregate_rating": "Average Rating",
        }, 
        color_discrete_sequence=px.colors.qualitative.D3 )
    
    return fig