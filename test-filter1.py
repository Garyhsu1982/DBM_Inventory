
#------------import packages---------------#

import base64

import numpy as np
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid

import streamlit as st

#------------import packages---------------#


#------------page basic settings---------------#


st.set_page_config(page_title="Lab Inventory")
st.title("Current Status of Lab Inventory")
st.sidebar.header ("User Input Features")

#------------import data---------------#
df = pd.read_excel(
    io='inventory_for_streamlit.xlsx',
    engine='openpyxl',
    sheet_name='Deutsch',
)
#------------import data---------------#

#------------data transformation---------------#
#df[["Jahr","Projekt Nr","Datum"]] = df[["Jahr","Projekt Nr","Datum"]].astype('string')

# df6 = df.copy()

#------------data transformation---------------#

#------------add select all funcation and multi selection for variable Jahr---------------#
# container = st.sidebar.container()
# all = st.sidebar.checkbox("Select all")
 
# if all:
#     jahr = container.multiselect("Select one or more options:",
#          df6["Jahr"].unique(),df6["Jahr"].unique())
# else:
#     jahr =  container.multiselect("Select one or more options:",
#         df6["Jahr"].unique())


#------------add select all funcation and multi selection for variable Jahr---------------#

#jahr = st.sidebar.multiselect(
#   "Select an Year:", 
#    options=df["Jahr"].unique(),
#   default=df["Jahr"].unique()
#)

#------------add  multi selection for other variables ---------------#

with st.form (key="From1"):
    with st.sidebar:
        jahr = st.sidebar.multiselect("Select one or more options:",
                options=df.Jahr.unique()
                #default=df.Jahr.unique()
        )

        materialart = st.sidebar.multiselect(
        "Select Material Type:", 
            options=df["Materialart"].unique(),
            default=df.Materialart.unique()
        )

        # herkunft = st.sidebar.multiselect(
        #     "Select Origin:",
        #     options=df["Herkunft"].unique()
        # )


        # author = st.sidebar.multiselect(
        #     "Select Author:",
        #     options=df["Auftraggeber-FD"].unique()
        # )

        # method = st.sidebar.multiselect(
        #     "Select Method:",
        #     options=df["Methoden"].unique()
        # )
        



#------------add  multi selection for other variables ---------------#


st.header('The Whole Database')

df_selected = df[(df.Jahr.isin(jahr))&(df.Materialart.isin(materialart))]



if jahr and materialart:
    AgGrid(df_selected.reset_index(drop = True))

else:
    AgGrid(df)

# df_selection = df.query(
#    "Jahr == @jahr or Probenart == @probenart or Herkunft == @herkunft or Methoden == @method"
#    )

# df_selection1 = df_selection.query(
#    "Jahr == @jahr & Probenart == @probenart & Herkunft == @herkunft & Methoden == @method"
#    )
# st.dataframe(df)
# st.dataframe(df_selection)


