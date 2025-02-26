import streamlit as st

#función para clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excellent"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "necesita mejorar"

#Interfaz en stremalit
st.title("Clasificación de puntaje")
st.write("Ingrese un puntaje y el sitema lo clasificará")

#entrada de usuario
puntaje = st.number_input("Ingrese un puntaje (0-100): ", min value=0, max_value=100, step=1)

#botón para clasificar
if st.button("Clasificar"):
    resultado = clasificar_puntaje(puntaje)
    st.success(f"El puntaje {puntaje} es clasificado como: { resultado}")