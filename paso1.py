import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# Título y descripción
st.title("🔩 Predicción con Regresión Lineal Simple")
st.write("Aplicación interactiva para entrenar un modelo de regresión lineal y visualizar las predicciones.")
st.write("Selecciona la variable dependiente (Y) y la variable independiente (X).")

# Cargar datos
st.subheader(" Cargar datos")
uploaded_file = st.file_uploader("Sube un archivo CSV con tus datos", type=["csv"])

if uploaded_file is not None:
    # Leer datos
    data = pd.read_csv(uploaded_file)
    st.write("Vista previa de los datos:")
    st.dataframe(data.head())

    # Seleccionar columnas
    columnas = data.columns.tolist()
    x_col = st.selectbox("Selecciona la variable independiente (X)", columnas)
    y_col = st.selectbox("Selecciona la variable dependiente (Y)", columnas)

    # Entrenamiento del modelo
    X = data[[x_col]].values
    y = data[y_col].values

    model = LinearRegression()
    model.fit(X, y)

    # Coeficientes del modelo
    pendiente = model.coef_[0]
    interseccion = model.intercept_

    # Mostrar ecuación
    st.subheader("Ecuación del modelo")
    st.latex(f"y = {interseccion:.2f} + {pendiente:.2f}x")

    # Calcular el R²
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    st.metric(label="Coeficiente de determinación (R²)", value=f"{r2:.4f}")
    st.write(f"El modelo explica el {r2*100:.2f}% de la variabilidad de los datos.")

    # Predicción interactiva
    st.subheader("Predicción con nuevo valor de X")
    nuevo_x = st.number_input("Ingresa un valor de X para predecir Y:", value=0.0)
    if st.button("Predecir"):
        prediccion = model.predict([[nuevo_x]])[0]
        st.success(f"Para X = {nuevo_x}, la predicción de Y es: {prediccion:.2f}")

    # Generar gráfico
    st.subheader(" Visualización de la regresión")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Datos reales')
    ax.plot(X, y_pred, color='red', label='Línea de regresión')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    st.pyplot(fig)

else:
    st.info(" Sube un archivo CSV para continuar.")
