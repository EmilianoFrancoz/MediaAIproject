import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="IA en Comunicación Audiovisual",
    page_icon="🎬",
    layout="wide"
)

# Título principal
st.title("🎬 Mapa interactivo del impacto de la IA en la Comunicación Audiovisual")

st.markdown("""
Esta aplicación complementa la presentación principal mostrando cómo la Inteligencia Artificial 
está transformando distintas etapas del proceso audiovisual.
""")

# Datos
datos = {
    "Etapa": [
        "Investigación",
        "Guion",
        "Producción",
        "Edición",
        "Diseño visual",
        "Distribución",
        "Análisis de audiencia"
    ],
    "Uso de IA": [
        "Análisis de tendencias, audiencias y consumo de contenido.",
        "Generación de ideas, estructuras narrativas y apoyo en escritura.",
        "Planificación de rodajes, organización de recursos y asistencia creativa.",
        "Edición automática, subtitulado, mejora de audio y selección de clips.",
        "Creación de imágenes, storyboards, piezas gráficas y estilos visuales.",
        "Personalización de contenidos y recomendación algorítmica.",
        "Interpretación de métricas, comportamiento del público y engagement."
    ],
    "Beneficio": [
        "Permite comprender mejor al público objetivo.",
        "Acelera la creación de propuestas narrativas.",
        "Optimiza tiempos y recursos de producción.",
        "Reduce tiempos técnicos de postproducción.",
        "Facilita la creación rápida de conceptos visuales.",
        "Mejora el alcance y la segmentación del contenido.",
        "Ayuda a tomar decisiones basadas en datos."
    ],
    "Riesgo": [
        "Sesgos en los datos utilizados.",
        "Pérdida de originalidad o dependencia creativa.",
        "Dependencia excesiva de herramientas tecnológicas.",
        "Pérdida del criterio humano en decisiones estéticas.",
        "Problemas de derechos de autor y autenticidad visual.",
        "Manipulación algorítmica o burbujas de contenido.",
        "Interpretación superficial de las métricas."
    ],
    "Impacto": [4, 3, 3, 5, 4, 4, 5],
    "Competencia profesional": [
        "Lectura crítica de datos.",
        "Curaduría narrativa y pensamiento creativo.",
        "Gestión audiovisual con apoyo tecnológico.",
        "Criterio estético y técnico en edición.",
        "Dirección visual ética.",
        "Estrategia digital y comunicación multiplataforma.",
        "Visualización e interpretación de datos."
    ]
}

df = pd.DataFrame(datos)

# Sidebar
st.sidebar.header("Panel de navegación")
etapa_seleccionada = st.sidebar.selectbox(
    "Selecciona una etapa del proceso audiovisual:",
    df["Etapa"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Esta app muestra cómo la IA impacta el flujo de trabajo audiovisual."
)

# Filtrar datos
fila = df[df["Etapa"] == etapa_seleccionada].iloc[0]

# Métricas principales
st.subheader(f"Etapa seleccionada: {etapa_seleccionada}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Nivel de impacto", f"{fila['Impacto']} / 5")

with col2:
    st.metric("Área", "Comunicación Audiovisual")

with col3:
    st.metric("Enfoque", "IA + Storytelling")

# Información principal
st.markdown("## Uso de IA en esta etapa")
st.write(fila["Uso de IA"])

# Tabs
tab1, tab2, tab3 = st.tabs(["✅ Beneficio", "⚠️ Riesgo", "🎓 Competencia"])

with tab1:
    st.subheader("Beneficio principal")
    st.write(fila["Beneficio"])

with tab2:
    st.subheader("Riesgo o desafío ético")
    st.write(fila["Riesgo"])

with tab3:
    st.subheader("Competencia profesional necesaria")
    st.write(fila["Competencia profesional"])

# Gráfico
st.markdown("## Visualización del impacto por etapa")

grafico = df.set_index("Etapa")["Impacto"]
st.bar_chart(grafico)

# Tabla completa
st.markdown("## Tabla general del análisis")
st.dataframe(df, use_container_width=True)

# Conclusión
st.markdown("---")
st.markdown("""
### Conclusión

La Inteligencia Artificial no reemplaza completamente al comunicador audiovisual, 
pero sí transforma sus herramientas, procesos y competencias.  
El reto principal es combinar automatización con criterio creativo, ético y narrativo.
""")
