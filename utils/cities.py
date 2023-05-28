#libraries
import pandas as pd
import plotly.express as px
import numpy  as np


def restaurants_by_cities (df, countries):
    df_aux = (df.loc[df['country_name'].isin(countries),['country_name','city', 'restaurant_id']]
                 .groupby(['country_name','city'])
                 .count()
                 .sort_values(['restaurant_id', 'city'], ascending=[False, True])
                 .reset_index())    
              
    fig = px.bar(
        df_aux.head(10),
        x='city',
        y='restaurant_id',
        text='restaurant_id',
        text_auto='.2f',
        color='country_name',
        color_discrete_sequence=px.colors.qualitative.D3,
        labels={
            'city': 'City',
            'restaurant_id': 'Number of Restaurants',
            'country_name': 'Country'
        },
    )
    return fig

def booking_by_city (df, countries):
    df_aux1 = df.loc[df['country_name'].isin(countries),['country_name','city', 'restaurant_id']].groupby(['country_name','city']).nunique().reset_index()
    #reserva
    df_aux2 = df.loc[df['has_table_booking'] == 1, ['city', 'restaurant_id']].groupby('city').nunique().reset_index()
    df_aux1=pd.merge(df_aux2, df_aux1, on=['city'], how='left')
    df_aux1.columns = ['City','Table_booking', 'Country', 'Restaurants']
    df_aux1 = df_aux1[['Country','City', 'Restaurants', 'Table_booking']]
    df_aux1['Table_booking'] = df_aux1['Table_booking'].fillna(0)
    df_aux = df_aux1.loc[df_aux1['Country'].isin(countries),['Country','City', 'Restaurants', 'Table_booking']].sort_values('Table_booking', ascending = False).reset_index()

    fig = px.sunburst(
        df_aux, 
        path=['Country', 'City'], 
        values='Restaurants',
        color='Table_booking', 
        color_continuous_scale='Darkmint', 
        color_continuous_midpoint = np.average(df_aux['Table_booking'])
    return fig

def delivery_by_city (df, countries):
    df_aux1 = df.loc[df['country_name'].isin(countries),['country_name','city', 'restaurant_id']].groupby(['country_name','city']).nunique().reset_index()
    df_aux2 = df.loc[df['is_delivering_now'] == 1, ['city', 'restaurant_id']].groupby('city').nunique().reset_index()
    df_aux1=pd.merge(df_aux2, df_aux1, on=['city'], how='left')
    df_aux1.columns = ['Cidade','Delivery', 'País', 'Restaurants']
    df_aux1 = df_aux1[['País','Cidade', 'Restaurants', 'Delivery']]
    df_aux1['Delivery'] = df_aux1['Delivery'].fillna(0)
    df_aux = df_aux1.loc[df_aux1['País'].isin(countries),['País','Cidade', 'Restaurants', 'Delivery']].sort_values('Delivery', ascending = False).reset_index()

    fig = px.sunburst(
        df_aux, 
        path=['País', 'Cidade'], 
        values='Restaurants',
        color='Delivery', 
        color_continuous_scale='Darkmint', 
        color_continuous_midpoint = np.average(df_aux['Delivery'] ) )
    return fig

def online_order_by_city (df, countries):
    df_aux1 = df.loc[df['country_name'].isin(countries),['country_name','city', 'restaurant_id']].groupby(['country_name','city']).nunique().reset_index()
    df_aux2 = df.loc[df['has_online_delivery'] == 1, ['city', 'restaurant_id']].groupby('city').nunique().reset_index()
    df_aux1=pd.merge(df_aux2, df_aux1, on=['city'], how='left')
    df_aux1.columns = ['Cidade','Online_order', 'País', 'Restaurants']
    df_aux1 = df_aux1[['País','Cidade', 'Restaurants', 'Online_order']]
    df_aux1['Online_order'] = df_aux1['Online_order'].fillna(0)
    df_aux = df_aux1.loc[df_aux1['País'].isin(countries),['País','Cidade', 'Restaurants', 'Online_order']].sort_values('Online_order', ascending = False).reset_index()

    fig = px.sunburst(
        df_aux, 
        path=['País', 'Cidade'], 
        values='Restaurants',
        color='Online_order', 
        color_continuous_scale='Darkmint', 
        color_continuous_midpoint = np.average(df_aux['Online_order'] ) )
    return fig

def top_10_above_4 (df, countries):
    df_aux = (df.loc[df['aggregate_rating'] > 4, ['country_name','city', 'restaurant_id']]
               .groupby(['country_name','city'])
               .nunique()
               .sort_values('restaurant_id', ascending = False )
               .reset_index())
    df_aux = df_aux.loc[df_aux['country_name'].isin(countries),:].reset_index()

    fig = px.bar(
            df_aux.head(10),
            x="city",
            y="restaurant_id",
            text="restaurant_id",
            text_auto=".2f",
            color="country_name",
            color_discrete_sequence=px.colors.qualitative.D3,
            labels={
                'city': 'City',
                'restaurant_id': 'Number of Restaurants',
                'country_name': 'Country'
            },
        )
    return fig

def top_10_below_2 (df, countries):
    df_aux = (df.loc[df['aggregate_rating'] < 2.5, ['country_name','city', 'restaurant_id']]
                .groupby(['city','country_name'])
                .nunique()
                .sort_values('restaurant_id', ascending = False )
                .reset_index())
    df_aux = df_aux.loc[df_aux['country_name'].isin(countries),:].reset_index()

    fig = px.bar(
            df_aux.head(10),
            x="city",
            y="restaurant_id",
            text="restaurant_id",
            text_auto=".2f",
            color="country_name",
            color_discrete_sequence=px.colors.qualitative.D3,
            labels={
                'city': 'City',
                'restaurant_id': 'Number of Restaurants',
                'country_name': 'Country'
            },
        )
    return fig

def cities_with_cuisines (df, countries):
    df_aux = (df.loc[df["country_name"].isin(countries), ['country_name','city', 'cuisines']]
                .groupby(['city','country_name'])
                .nunique()
                .sort_values('cuisines', ascending = False )
                .reset_index())

    fig = px.bar(
            df_aux.head(10),
            x="city",
            y="cuisines",
            text="cuisines",
            text_auto=".2f",
            color="country_name",
            color_discrete_sequence=px.colors.qualitative.D3,
            labels={
                'city': 'City',
                'cuisines': 'Number of cuisines',
                'country_name': 'Country'
            },
        )
    return fig
