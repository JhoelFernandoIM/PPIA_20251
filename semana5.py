import streamlit as st

def main():
    st.title("Ejemplo de while y for en streamlit")

    #Ejemplo de while
    st.subheader("Ejemplo de while")

    n = st.number_input("Ingresa un número para contar hasta 5: ", min_value=0, max_value=5)
    contador = 0
    resultado_while=""

    while contador <=n:
        resultado_while +=f"{contador}"
        contador +=1
    st.write("Secuencia generada con while: ", resultado_while)

    #Ejemplo de for

    st.subheader("Ejemplo con for")
    m=st.number_input("Ingrese un número  para generar una secuencia: ", min_value=1, max_value=10)
    resultado_for = "".join(f"{i} " for i in range (1, m+1))
    