import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análisis de Datos con Streamlit")

# Subir archivo CSV
archivo = st.file_uploader("Sube tu archivo CSV", type=['csv'])
if archivo:
    try:
        datos = pd.read_csv(archivo)
        st.success("Datos cargados correctamente")

        # Mostrar datos
        st.write("## Datos Cargados")
        st.dataframe(datos.head())

        # Mostrar estadísticas
        st.write("## Estadísticas Descriptivas")
        st.write(datos.describe())

        # Graficar datos
        st.write("## Gráfico de Valores a lo largo del Tiempo")
        if 'Fecha' in datos.columns and 'Valor' in datos.columns:
            fig, ax = plt.subplots(figsize=(10,6))
            ax.plot(datos['Fecha'], datos['Valor'])
            ax.set_title('Valor a lo largo del tiempo')
            ax.set_xlabel('Fecha')
            ax.set_ylabel('Valor')
            st.pyplot(fig)
        else:
            st.warning("Las columnas 'Fecha' y 'Valor' no se encontraron en el archivo CSV.")
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
