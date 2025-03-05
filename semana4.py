import streamlit as st

st.title("Estructura de control repetitivas")

#Entrada del usuario para límites del bucle
limite = st.number_input("Ingrese un número límite para los búcles: ", min_value=1, step= 1)

st.subheader("Bucle FOR")

for i in range(1,limite + 1):
    st.write(f"Iteración {i} con for")
