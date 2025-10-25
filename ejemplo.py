import streamlit as st

import streamlit as st

# Título de la aplicación
st.title('Sumadora de dos números')

# Obtener el primer número del usuario
numero1 = st.number_input('Ingresa el primer número', value=0)

# Obtener el segundo número del usuario
numero2 = st.number_input('Ingresa el segundo número', value=0)

# Realizar la suma
suma = numero1 + numero2

# Mostrar el resultado
st.write(f'La suma de {numero1} + {numero2} es: {suma}')
