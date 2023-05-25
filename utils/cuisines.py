#libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import matplotlib.pyplot as plt 
import numpy  as np


def top_cuisines (df, key):
        
    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_name",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes"
    ]

    lines = df["cuisines"] == key

    top_cuisines = (df.loc[lines, cols]
                  .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                  .reset_index()   
                  .iloc[0,:]
                  .to_dict())
    return top_cuisines

def top_restaurants (df, countries, cuisines, top_n):
    lines = (df["cuisines"].isin(cuisines)) & (df["country_name"].isin(countries))
    cols = ['restaurant_id', 'restaurant_name', 'country_name', 'city','cuisines','average_cost_for_two','aggregate_rating', 'votes']
    top10 = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
    return top10.head(top_n)

def top_10_cuisines_best_rating (df, countries, cuisines, top_n):
    lines = (df["cuisines"].isin(cuisines)) & (df["country_name"].isin(countries))
    cuisines_best_rating = (df.loc[lines, ['aggregate_rating', 'cuisines']]
                              .groupby('cuisines')
                              .mean()
                              .sort_values('aggregate_rating', ascending = False)
                              .reset_index()
                              .head(top_n))

    fig = px.bar(
        cuisines_best_rating.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        color_discrete_sequence=px.colors.qualitative.D3,
        labels={
            "cuisines": "Culinary type",
            "aggregate_rating": "Rating Average",
        },
    )
    return fig

def top_10_cuisines_worst_rating (df, countries, cuisines, top_n):
    lines = (df["cuisines"].isin(cuisines)) & (df["country_name"].isin(countries))
    cuisines_worst_rating = ( df.loc[lines, ['aggregate_rating', 'cuisines']]
                                .groupby('cuisines')
                                .mean()
                                .sort_values(['aggregate_rating'], ascending = True)
                                .reset_index()
                                .head(top_n))

    fig = px.bar(
            cuisines_worst_rating.head(top_n),
            x="cuisines",
            y="aggregate_rating",
            text="aggregate_rating",
            text_auto=".2f",
            color_discrete_sequence=px.colors.qualitative.D3,
            labels={
                "cuisines": "Culinary type",
                "aggregate_rating": "Rating Average",
            },
    )
    return fig