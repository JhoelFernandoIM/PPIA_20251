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

if __name__ == "__main__":
    main()