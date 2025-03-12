import streamlit as st
from supabase import create_client, Client
import os

#configurar supabase
SUPABASE_URL = "https://bmfyqluttbhuiookplic.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtZnlxbHV0dGJodWlvb2twbGljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU2MTYsImV4cCI6MjA1NzMyMTYxNn0.QH-LObkiMjRWYSaf7uZOyk__mPoWr0ipWWNL2xobzSY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title ("Gestión de clientes - CRUD con Supabase y Streamlit")

#Formulario para agregar cliente
st.header("Agregar cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Teléfono")

if st.button("Agregar Cliente"):
    if nombre and email:
        data = {"nombre":nombre, "email": email, "telefono":telefono}
        response = supabase.table("clientes").insert(data).execute()
    else:
        st.warning("Nombre y Email son obligatorios")