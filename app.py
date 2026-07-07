import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IA en Comunicación Audiovisual",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Mapa Interactivo del Impacto de la IA en la Comunicación Audiovisual")

st.markdown("""
Esta aplicación muestra cómo la Inteligencia Artificial está transformando las distintas
etapas del proceso audiovisual.
""")

# -----------------------------
# Mapa visual del flujo
# -----------------------------
st.markdown("## 🗺️ Mapa del flujo audiovisual con IA")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.markdown("### 🔍")
    st.markdown("**Investigación**")
    st.caption("IA analiza audiencias")

with col2:
    st.markdown("### ✍️")
    st.markdown("**Guion**")
    st.caption("IA apoya ideas")

with col3:
    st.markdown("### 🎥")
    st.markdown("**Producción**")
    st.caption("IA organiza recursos")

with col4:
    st.markdown("### ✂️")
    st.markdown("**Edición**")
    st.caption("IA automatiza procesos")

with col5:
    st.markdown("### 🎨")
    st.markdown("**Diseño visual**")
    st.caption("IA genera conceptos")

with col6:
    st.markdown("### 📡")
    st.markdown("**Distribución**")
    st.caption("IA personaliza contenido")

with col7:
    st.markdown("### 📊")
    st.markdown("**Análisis**")
    st.caption("IA interpreta métricas")

st.markdown("---")

# -----------------------------
# Datos
# -----------------------------
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
        "Análisis de tendencias y audiencias.",
        "Generación de ideas y apoyo en escritura.",
        "Planificación y organización de recursos.",
        "Edición automática, subtítulos y mejora de audio.",
        "Creación de imágenes y storyboards.",
        "Personalización y recomendación de contenido.",
        "Interpretación de métricas y comportamiento del público."
    ],
    "Beneficio": [
        "Comprender mejor al público.",
        "Acelerar la creatividad.",
        "Optimizar recursos.",
        "Reducir tiempos de edición.",
        "Crear conceptos visuales rápidamente.",
        "Mejorar el alcance del contenido.",
        "Tomar decisiones basadas en datos."
    ],
    "Riesgo": [
        "Sesgos en los datos.",
        "Pérdida de creatividad.",
        "Dependencia tecnológica.",
        "Menor criterio humano.",
        "Problemas de derechos de autor.",
        "Manipulación algorítmica.",
        "Malinterpretación de métricas."
    ],
    "Impacto": [4, 3, 3, 5, 4, 4, 5],
    "Competencia": [
        "Análisis de datos.",
        "Pensamiento creativo.",
        "Gestión audiovisual.",
        "Edición profesional.",
        "Dirección visual ética.",
        "Marketing digital.",
        "Visualización de datos."
    ]
}

df = pd.DataFrame(datos)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎛️ Panel de Control")

etapa = st.sidebar.selectbox(
    "Selecciona una etapa",
    df["Etapa"]
)

impacto = st.sidebar.slider(
    "Impacto mínimo",
    1,
    5,
    3
)

comparar = st.sidebar.multiselect(
    "Comparar etapas",
    df["Etapa"],
    default=["Edición", "Diseño visual"]
)

mostrar_tabla = st.sidebar.checkbox(
    "Mostrar tabla completa",
    value=True
)

enfoque = st.sidebar.radio(
    "Información a mostrar",
    ["Beneficio", "Riesgo", "Competencia"]
)

fila = df[df["Etapa"] == etapa].iloc[0]

# -----------------------------
# Métricas
# -----------------------------
st.subheader(f"📍 Etapa seleccionada: {etapa}")

col1, col2, col3 = st.columns(3)

col1.metric("Impacto", f"{fila['Impacto']} / 5")
col2.metric("Área", "Comunicación")
col3.metric("Tecnología", "IA")

# -----------------------------
# Uso de IA
# -----------------------------
st.markdown("## 🤖 Uso de la IA")
st.info(fila["Uso de IA"])

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3 = st.tabs(["✅ Beneficio", "⚠️ Riesgo", "🎓 Competencia"])

with tab1:
    st.success(fila["Beneficio"])

with tab2:
    st.error(fila["Riesgo"])

with tab3:
    st.info(fila["Competencia"])

# -----------------------------
# Información destacada
# -----------------------------
st.markdown("## 🔍 Información destacada")

if enfoque == "Beneficio":
    st.success(fila["Beneficio"])
elif enfoque == "Riesgo":
    st.warning(fila["Riesgo"])
else:
    st.info(fila["Competencia"])

# -----------------------------
# Gráfico
# -----------------------------
st.markdown("## 📊 Nivel de impacto por etapa")

df_filtrado = df[df["Impacto"] >= impacto]

st.bar_chart(
    df_filtrado.set_index("Etapa")["Impacto"]
)

# -----------------------------
# Comparación
# -----------------------------
st.markdown("## 📋 Comparación de etapas")

comparacion = df[df["Etapa"].isin(comparar)]

if len(comparacion) > 0:
    st.dataframe(comparacion, use_container_width=True)
else:
    st.warning("Selecciona al menos una etapa para comparar.")

# -----------------------------
# Tabla completa
# -----------------------------
if mostrar_tabla:
    st.markdown("## 📑 Base de datos")
    st.dataframe(df, use_container_width=True)

# -----------------------------
# Conclusión
# -----------------------------
st.markdown("---")

st.subheader("🎯 Conclusión")

st.write("""
La Inteligencia Artificial está transformando todas las fases de la Comunicación Audiovisual.
Su verdadero potencial no consiste en reemplazar al profesional, sino en potenciar su creatividad,
optimizar procesos y apoyar la toma de decisiones. El desafío es utilizar estas herramientas de
forma ética, crítica y responsable.
""")
