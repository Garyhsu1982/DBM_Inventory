import pandas as pd 
import streamlit as st
import openpyxl
import base64
from st_aggrid import AgGrid
import plotly.express as px  
import numpy as np



st.set_page_config(page_title="Lab Inventory")
st.title("Current Status of Lab Inventory")
st.sidebar.header ("User Input Features")

df = pd.read_excel("inventory.xlsx")

df[["Probenbezeichnung","Projekt Nr","Datum"]] = df[["Probenbezeichnung","Projekt Nr","Datum"]].astype('string')

df6 = df.copy()

container = st.sidebar.container()
all = st.sidebar.checkbox("Select all")
 
if all:
    jahr = container.multiselect("Select one or more options:",
         df6["Jahr"].unique(),df6["Jahr"].unique())
else:
    jahr =  container.multiselect("Select one or more options:",
        df6["Jahr"].unique())


#jahr = st.sidebar.multiselect(
#   "Select an Year:", 
#    options=df["Jahr"].unique(),
#   default=df["Jahr"].unique()
#)

probenart = st.sidebar.multiselect(
   "Select Sample Type:", 
    options=df6["Probenart"].unique()
)

herkunft = st.sidebar.multiselect(
    "Select Origin:",
    options=df6["Herkunft"].unique()
)

auftraggeber = st.sidebar.multiselect(
    "Select Author:",
    options=df6["Auftraggeber-FD"].unique()
)

method = st.sidebar.multiselect(
    "Select Method:",
    options=df6["Methoden"].unique()
)

st.header('The Whole Database')
#st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.')


if jahr:
    df6 = df6[df6["Jahr"].isin(jahr)]
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )

elif herkunft:
    df6 = df6[df6["Herkunft"].isin(herkunft)]
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )
elif probenart:
    df6 = df6[df6["Probenart"].isin(probenart)]
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )
elif auftraggeber:
    df6 = df6[df6["Auftraggeber-FD"].isin(auftraggeber)]
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )
elif method:
    df6 = df6[df6["Methoden"].isin(method)]
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )
else:
    st.write('Data Dimension: ' + str(df6.shape[0]) + ' rows and ' + str(df6.shape[1]) + ' columns.'
               )
# st.dataframe(df6.reset_index(drop = True).style.apply(highlight_rows, axis=1))

if jahr or herkunft or probenart or auftraggeber or method:
    AgGrid(df6.reset_index(drop = True))
else:
    AgGrid(df)



@st.cache
def convert_df(df6):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df6.to_csv().encode('utf-8')

csv = convert_df(df6)

st.download_button(
     label="Download Whole data as CSV",
     data=csv,
     file_name='lab.csv',
     mime='text/csv',
 )


df_grouped = df6.groupby(by=["Jahr"]).count()

bar_chart = px.bar (df_grouped,
x="Herkunft",
y="Herkunft",
text="Herkunft",
color_discrete_sequence=["#F63366"]*len(df_grouped),
template="plotly_white")


#df_selection = df.query(
#    "(Jahr == @jahr) and (Probenart == @probenart) and (Herkunft == @herkunft) and (Methoden == @method)"
#)
#AgGrid(df_selection)