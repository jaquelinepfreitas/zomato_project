#libraries
import streamlit as st
from PIL import Image
import pandas as pd
import folium
from streamlit_folium import folium_static
import inflection

from utils import process as pc
from utils import general as gn

#barra lateral
def create_sidebar (df):
    image_path = 'garfo.png'
    image = Image.open(image_path)

    col1, col2 = st.sidebar.columns([2, 3], gap="large")
    col1.image(image, width=120)
    col2.markdown("# Zomato")
    st.sidebar.markdown("""___""")

    st.sidebar.markdown("## Filters")

    countries = st.sidebar.multiselect(
        "Select countries to view information:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )


    st.sidebar.markdown("### Processed data:")

    processed_data = pd.read_csv("zomato.csv")

    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )
    return list(countries)

def main():
    df = pc.import_dataset('zomato.csv')
    st.set_page_config(page_title='Home', layout = 'wide')

    selected_countries =create_sidebar(df)

    st.markdown('# Zomato')
    st.markdown('## Global Platform')
    st.markdown("#### We have the following brands within our platform:")
    st.markdown("#     ")
    restaurants, countries, cities, ratings, cuisines = st.columns(5)

    restaurants.metric(
        "Registered restaurants",
        gn.qty_restaurants(df)
    )

    countries.metric(
        "Registered countries",
        gn.qty_countries(df)
    )

    cities.metric(
        "Registered cities",
        gn.qty_cities(df)
    )

    ratings.metric(
        "Ratings made on the Platform",
        f"{gn.qty_ratings(df):,}".replace(",", "."),
    )

    cuisines.metric(
        f"Types of Cuisine Offered",
        f"{gn.qty_cuisines(df):,}",
    )

    map_df = df.loc[df["country_name"].isin(selected_countries), :]

    gn.create_map(map_df)
    
main()