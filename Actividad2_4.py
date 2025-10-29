import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import io

# === CONFIGURACIÓN DE LA APP ===
st.set_page_config(page_title="Segmentación de Clientes", layout="centered")
st.title("📊 Segmentación de Clientes (Actividad 2.4)")
st.write("Sube tu archivo `clientes.csv` para aplicar **K-Means Clustering** y segmentar a los clientes según sus características numéricas.")

# === SUBIR ARCHIVO CSV ===
uploaded_file = st.file_uploader("Sube el archivo clientes.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Vista previa de los datos:")
    st.dataframe(df.head())

    # --- Seleccionar columnas numéricas ---
    columnas_num = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if len(columnas_num) < 2:
        st.warning("⚠️ Se necesitan al menos 2 columnas numéricas para hacer clustering.")
    else:
        seleccion = st.multiselect("Selecciona las columnas para el análisis:", columnas_num, default=columnas_num[:2])

        if len(seleccion) >= 2:
            # Escalado de datos
            scaler = MinMaxScaler()
            datos_escalados = scaler.fit_transform(df[seleccion])

            # --- Método del Codo ---
            st.subheader("📉 Método del Codo (para determinar el número óptimo de clusters)")
            inercias = []
            K = range(2, 10)
            for k in K:
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(datos_escalados)
                inercias.append(kmeans.inertia_)

            fig, ax = plt.subplots()
            ax.plot(K, inercias, 'bo-')
            ax.set_xlabel('Número de clusters (k)')
            ax.set_ylabel('Inercia')
            ax.set_title('Método del Codo')
            st.pyplot(fig)

            # --- Elección del número de clusters ---
            k = st.slider("Selecciona el número de clusters (k):", 2, 10, 3)

            # --- Aplicar K-Means ---
            kmeans = KMeans(n_clusters=k, random_state=42)
            df["Cluster"] = kmeans.fit_predict(datos_escalados)

            st.subheader(f"🎯 Resultados del Clustering (k = {k})")
            st.dataframe(df)

            # --- Gráfico de dispersión ---
            st.subheader("📊 Visualización de Clusters")
            fig2, ax2 = plt.subplots()
            scatter = ax2.scatter(df[seleccion[0]], df[seleccion[1]], c=df["Cluster"], cmap='tab10')
            ax2.set_xlabel(seleccion[0])
            ax2.set_ylabel(seleccion[1])
            ax2.set_title("Distribución de Clusters")
            st.pyplot(fig2)

            # --- Descarga de resultados ---
            st.subheader("💾 Descargar resultados")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Descargar archivo con clusters",
                data=csv,
                file_name="clientes_segmentados.csv",
                mime="text/csv"
            )
else:
    st.info("👈 Sube un archivo CSV para comenzar.")
