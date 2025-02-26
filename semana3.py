import streamlit as st

#función para clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excellent"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "necesita mejorar"
    
#Menú lateral
st.sidebar.title("Menú de Navegación")
opcion = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Clasificación de puntajes"])

#Sección inicio
if opcion == "Inicio":
    st.title("Bienvenido a la aplicación")
    st.write("Mueva el deslizador para ver como se clasifica el puntaje en tiempo real")

    #filtro desplazable
    puntaje_slider = st.slider("Selccione un puntaje : ", 0, 100, 50)

    #Mostrar la clasificaación en tiempo real
    st.info(f"El puntaje {puntaje_slider} es clasificado como: ** {clasificar_puntaje(puntaje_slider)}**")

#Seccion: clasificación de puntajes
elif opcion == "Clasificación de puntajes":
    st.title("Clasificación de puntajes")
    st.write("Ingrese un puntaje y el sistema lo claisificará")

    #entrada de usuario
    puntaje = st.number_input("Ingrese un puntaje (0-100): ", min_value=0, max_value=100, step=1)

    #botón para clasificar
    if st.button("Clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"El puntaje {puntaje} es clasificado como: { resultado}")