import streamlit as st
import requests
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

st.title("APPLICATION DE Jean MOYENGA")
st.write("Bienvenue dans mon application streamlit")

# Charger les donnees et les fusionner
clics = pd.read_csv("clics.csv")
impressions = pd.read_csv("impressions.csv")
achats = pd.read_csv("achats.csv")

merged_data = pd.merge(impressions,clics, on="cookie_id")
merged_data = pd.merge(merged_data, achats, on="cookie_id")
df = merged_data
  # Utilisation de data pour créer un DataFrame df

    # Calcul du chiffre d'affaires
chiffre_affaires = df['price'].sum()
st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

    ## Box plot
fig = px.box(df, x='product_id', y='age')
fig.update_layout(
    xaxis_title='Produits',
    yaxis_title="Âge",
    title="Âge des clients en fonction des produits")
st.plotly_chart(fig)

fig1 = px.bar(df,x='campaign_id', y='price')
fig1.update_layout(
    xaxis_title='campagne',
    yaxis_title="price",
    title="Les ventes par campagnes")
st.plotly_chart(fig1)

fig3 = px.histogram(df, x='gender', y='product_id')
fig3.update_layout(
     xaxis_title='gender',
     yaxis_title="produits",
     title="Produit par sexe")
st.plotly_chart(fig3)


