
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
df = pd.read_excel("inventory.xlsx")
#------------import data---------------#

#------------data transformation---------------#
# df[["Probenbezeichnung","Projekt Nr","Datum"]] = df[["Probenbezeichnung","Projekt Nr","Datum"]].astype('string')

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

jahr = st.sidebar.multiselect("Select one or more options:",
        options=df["Jahr"].unique(),
        default=df["Jahr"].unique()
)

probenart = st.sidebar.multiselect(
   "Select Sample Type:", 
    options=df["Probenart"].unique(),
    default=df["Probenart"].unique()
)

herkunft = st.sidebar.multiselect(
    "Select Origin:",
    options=df["Herkunft"].unique(),
    default=df["Herkunft"].unique()
)


# author = st.sidebar.multiselect(
#     "Select Author:",
#     options=df["Auftraggeber-FD"].unique()
# )

method = st.sidebar.multiselect(
    "Select Method:",
    options=df["Methoden"].unique(),
    default=df["Methoden"].unique()
)

#------------add  multi selection for other variables ---------------#


st.header('The Whole Database')

df_selection = df.query(
   "Jahr == @jahr & Probenart == @probenart & Herkunft == @herkunft & Methoden == @method"
   )


st.dataframe(df_selection)






#------------download data set ---------------#
# @st.cache
# def convert_df(df6):
#      # IMPORTANT: Cache the conversion to prevent computation on every rerun
#      return df6.to_csv().encode('utf-8')

# csv = convert_df(df6)

# st.download_button(
#      label="Download the selected data as CSV",
#      data=csv,
#      file_name='lab.csv',
#      mime='text/csv',
#  )
#------------download data set ---------------#



#df_selection = df.query(
#    "(Jahr == @jahr) and (Probenart == @probenart) and (Herkunft == @herkunft) and (Methoden == @method)"
#)
#AgGrid(df_selection)