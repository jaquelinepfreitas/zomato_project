import pandas as pd
from PIL import Image
import folium
import inflection


#Para renomear as colunas do DataFrame
def rename_columns(df1):
    df = df1.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def clean_code(df):
    """ Esta funcao tem a responsabilidade de limpar o dataframe

            Tipos de limpeza:
            1. Para colocar o nome dos países com base no código de cada país;
            2. Criar a categoria do tipo de comida com base no range de valores;
            3. Criar o nome das cores com base nos códigos de cores;
            4. Categorizar todos os restaurantes somente por um tipo de culinária;
            5. Remover coluna 'Switch to order menu' com um dado único;
            6. Identificar e remover dados duplicados.

            Input: Dataframe
            Output: Dataframe  
    """
    
    #1. Para colocar o nome dos países com base no código de cada país
    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }
    df['country_name'] = df['country_code'].map(COUNTRIES)
    
    #2. Criar a categoria do tipo de comida com base no range de valores.
    PRICE = {
    1: "cheap",
    2: "normal",
    3: "expensive",
    4: "gourmet",
    }
    df['price_tye'] = df['price_range'].map(PRICE)
    
    #3. Criar o nome das cores com base nos códigos de cores
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred"
    }
    df['color_drop_duplicatesname'] = df['rating_color'].map(COLORS)
    
    #categorizar todos os restaurantes somente por um tipo de culinária.
    df['cuisines'] = df['cuisines'].astype( str )
    df['cuisines'] = df.loc[:, 'cuisines'].apply(lambda x: x.split(",")[0])
    
    #Remover coluna 'Switch to order menu' com um dado único
    df =df.drop('switch_to_order_menu',axis='columns')
    
    #Identificar e remover dados duplicados
    df = df.drop_duplicates()
    
    #Identificar e remover dados 'nan'
    df = df.loc[df['cuisines'] != 'nan', :]
    
    return df

def import_dataset (file_path):
    df1 = pd.read_csv(file_path)
    df = rename_columns(df1)
    df = clean_code(df)
    return df
