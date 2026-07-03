import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Mi App en Streamlit Cloud", page_icon="🚀")

st.title("Ejemplo de Placeholder en Streamlit")
st.write("Esta app muestra cómo simular una carga de datos usando contenedores dinámicos.")

# --- 1. CREAR EL PLACEHOLDER ---
# Este contenedor reserva el espacio en la interfaz
contenedor_placeholder = st.empty()

# --- 2. MOSTRAR CONTENIDO TEMPORAL (EL PLACEHOLDER) ---
# Usamos un bloque 'with' para meter elementos dentro de ese espacio específico
with contenedor_placeholder.container():
    st.info("⏳ Conectando con el servidor de Streamlit Cloud...")
    # Agregamos una animación de carga nativa
    st.spinner("Cargando base de datos...")
    
    # Simulamos un proceso que toma tiempo (ej. leer un CSV o llamar una API)
    time.sleep(3)

# --- 3. REEMPLAZAR EL PLACEHOLDER CON LOS DATOS REALES ---
# Al volver a escribir sobre el mismo objeto '.empty()', lo temporal desaparece
with contenedor_placeholder.container():
    st.success("¡Datos cargados con éxito! 🎉")
    
    # Aquí ya muestras tus métricas, gráficos o tablas reales
    col1, col2 = st.columns(2)
    col1.metric(label="Usuarios Activos", value="1,240", delta="12%")
    col2.metric(label="Conversión", value="4.3%", delta="-0.5%")
    
    st.write("Aquí abajo puedes seguir agregando el resto de tu aplicación de forma normal.")
