# app.py

import streamlit as st
import pandas as pd
import plotly.express as px


# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------

st.set_page_config(
    page_title="IA y Comunicación Audiovisual",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# DATOS DEL PROYECTO
# ---------------------------------------------------------

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
    "Icono": [
        "🔍",
        "✍️",
        "🎥",
        "✂️",
        "🎨",
        "📡",
        "📊"
    ],
    "Uso de IA": [
        "Análisis de tendencias, audiencias y grandes volúmenes de información.",
        "Generación de ideas, apoyo en escritura, escaletas y estructuras narrativas.",
        "Planificación, organización de recursos y asistencia en procesos técnicos.",
        "Edición automática, subtítulos, transcripción, limpieza y mejora de audio.",
        "Creación de imágenes, conceptos visuales, storyboards y variaciones gráficas.",
        "Personalización, recomendación de contenido y adaptación a diferentes plataformas.",
        "Interpretación de métricas, comportamiento del público y evaluación del desempeño."
    ],
    "Beneficio": [
        "Comprender mejor al público y fundamentar decisiones.",
        "Acelerar la ideación y explorar distintas alternativas narrativas.",
        "Optimizar recursos, tiempos y organización de tareas.",
        "Reducir tiempos de edición y automatizar tareas repetitivas.",
        "Producir conceptos visuales con mayor rapidez.",
        "Mejorar el alcance y adaptar contenidos a diferentes audiencias.",
        "Tomar decisiones basadas en datos y resultados."
    ],
    "Riesgo": [
        "Sesgos en los datos o conclusiones incorrectas.",
        "Dependencia de propuestas genéricas o pérdida de originalidad.",
        "Dependencia tecnológica y errores de automatización.",
        "Pérdida de criterio humano o resultados poco naturales.",
        "Problemas de autoría, derechos de imagen y homogeneización.",
        "Manipulación algorítmica o pérdida de diversidad de contenidos.",
        "Interpretación incorrecta de métricas o decisiones automatizadas."
    ],
    "Competencia": [
        "Análisis de datos y verificación de información.",
        "Pensamiento creativo, escritura y dirección narrativa.",
        "Gestión audiovisual y toma de decisiones.",
        "Edición profesional y supervisión técnica.",
        "Dirección visual, creatividad y ética.",
        "Marketing digital y estrategia de contenidos.",
        "Visualización de datos y pensamiento crítico."
    ],
    "Nivel de transformación": [
        4,
        3,
        3,
        5,
        4,
        4,
        5
    ],
    "Aplicación profesional": [
        "Investigación documental, análisis de públicos y detección de tendencias.",
        "Desarrollo de conceptos, guiones, escaletas y propuestas narrativas.",
        "Planeación de rodajes, organización de recursos y previsualización.",
        "Postproducción, subtitulado, traducción, audio y automatización de procesos.",
        "Diseño de campañas, storyboards, piezas gráficas y dirección de arte.",
        "Adaptación de formatos, personalización y estrategia multiplataforma.",
        "Evaluación de campañas, métricas, audiencias y rendimiento de contenidos."
    ]
}

df = pd.DataFrame(datos)


# ---------------------------------------------------------
# PANEL LATERAL
# ---------------------------------------------------------

st.sidebar.title("🎛️ Panel de control")

etapa_seleccionada = st.sidebar.selectbox(
    "Selecciona una etapa",
    df["Etapa"].tolist()
)

nivel_minimo = st.sidebar.slider(
    "Nivel mínimo de transformación",
    min_value=1,
    max_value=5,
    value=1
)

etapas_comparacion = st.sidebar.multiselect(
    "Comparar etapas",
    options=df["Etapa"].tolist(),
    default=df["Etapa"].tolist()
)

mostrar_tabla = st.sidebar.checkbox(
    "Mostrar tabla completa",
    value=True
)

informacion_mostrar = st.sidebar.radio(
    "Información a mostrar",
    ["Beneficio", "Riesgo", "Competencia", "Aplicación profesional"]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Los niveles mostrados tienen fines didácticos.
    Representan una estimación construida para explicar
    cómo la IA interviene en cada etapa del flujo audiovisual.
    """
)


# ---------------------------------------------------------
# FILTROS
# ---------------------------------------------------------

df_filtrado = df[
    (df["Nivel de transformación"] >= nivel_minimo)
    & (df["Etapa"].isin(etapas_comparacion))
].copy()

fila = df[df["Etapa"] == etapa_seleccionada].iloc[0]


# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------

st.title("🎬 Mapa Interactivo del Impacto de la IA en la Comunicación Audiovisual")

st.write(
    """
    Esta aplicación muestra cómo la Inteligencia Artificial está transformando
    las distintas etapas del proceso audiovisual, identificando beneficios,
    riesgos, competencias y aplicaciones profesionales.
    """
)


# ---------------------------------------------------------
# FLUJO AUDIOVISUAL
# ---------------------------------------------------------

st.header("🗺️ Mapa del flujo audiovisual con IA")

columnas = st.columns(len(df))

for indice, columna in enumerate(columnas):
    etapa = df.iloc[indice]

    with columna:
        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:12px;
                border-radius:12px;
                border:1px solid #444;
                min-height:160px;
                background-color:#151922;
            ">
                <div style="font-size:34px;">{etapa['Icono']}</div>
                <div style="font-size:17px; font-weight:bold; margin-top:8px;">
                    {etapa['Etapa']}
                </div>
                <div style="font-size:13px; color:#B7BDC8; margin-top:12px;">
                    {etapa['Uso de IA']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# ETAPA SELECCIONADA
# ---------------------------------------------------------

st.markdown("---")
st.header(f"📍 Etapa seleccionada: {etapa_seleccionada}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Nivel estimado de transformación",
        f"{fila['Nivel de transformación']} / 5"
    )

with col2:
    st.metric(
        "Área",
        "Comunicación Audiovisual"
    )

with col3:
    st.metric(
        "Tecnología",
        "Inteligencia Artificial"
    )


st.subheader("🤖 Uso de la IA")
st.info(fila["Uso de IA"])


# ---------------------------------------------------------
# BENEFICIOS, RIESGOS, COMPETENCIAS Y APLICACIÓN
# ---------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "✅ Beneficio",
        "⚠️ Riesgo",
        "🎓 Competencia",
        "💼 Aplicación profesional"
    ]
)

with tab1:
    st.success(fila["Beneficio"])

with tab2:
    st.warning(fila["Riesgo"])

with tab3:
    st.info(fila["Competencia"])

with tab4:
    st.write(fila["Aplicación profesional"])


# ---------------------------------------------------------
# GRÁFICA
# ---------------------------------------------------------

st.markdown("---")
st.header("📊 Nivel estimado de transformación por etapa")

fig = px.bar(
    df_filtrado,
    x="Etapa",
    y="Nivel de transformación",
    text="Nivel de transformación",
    hover_data=[
        "Uso de IA",
        "Beneficio",
        "Riesgo",
        "Competencia"
    ],
    range_y=[0, 5],
    title="Comparación del nivel de transformación en el flujo audiovisual"
)

fig.update_layout(
    xaxis_title="Etapa del proceso audiovisual",
    yaxis_title="Nivel estimado de transformación",
    showlegend=False
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ---------------------------------------------------------
# COMPARACIÓN
# ---------------------------------------------------------

st.header("📋 Comparación de etapas")

columnas_comparacion = [
    "Etapa",
    "Uso de IA",
    informacion_mostrar,
    "Nivel de transformación"
]

st.dataframe(
    df_filtrado[columnas_comparacion],
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# COMPETENCIAS PROFESIONALES
# ---------------------------------------------------------

st.markdown("---")
st.header("🎓 Competencias del comunicólogo audiovisual")

competencias = [
    "Pensamiento crítico",
    "Creatividad y dirección narrativa",
    "Alfabetización en Inteligencia Artificial",
    "Ética y verificación de información",
    "Visualización y análisis de datos",
    "Comunicación estratégica",
    "Supervisión de procesos automatizados",
    "Aprendizaje continuo"
]

col_comp_1, col_comp_2 = st.columns(2)

mitad = len(competencias) // 2

with col_comp_1:
    for competencia in competencias[:mitad]:
        st.write(f"✅ {competencia}")

with col_comp_2:
    for competencia in competencias[mitad:]:
        st.write(f"✅ {competencia}")


# ---------------------------------------------------------
# TABLA COMPLETA
# ---------------------------------------------------------

if mostrar_tabla:
    st.markdown("---")
    st.header("🗂️ Base de datos")

    st.dataframe(
        df[
            [
                "Etapa",
                "Uso de IA",
                "Beneficio",
                "Riesgo",
                "Nivel de transformación",
                "Competencia",
                "Aplicación profesional"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# DESCARGA DE DATOS
# ---------------------------------------------------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Descargar base de datos en CSV",
    data=csv,
    file_name="impacto_ia_comunicacion_audiovisual.csv",
    mime="text/csv"
)


# ---------------------------------------------------------
# NOTA METODOLÓGICA
# ---------------------------------------------------------

st.markdown("---")
st.header("📚 Nota metodológica")

st.write(
    """
    Los niveles de transformación presentados en esta aplicación son estimaciones
    con fines académicos y didácticos. No representan una medición universal de la
    industria audiovisual.

    La aplicación busca sintetizar cómo la Inteligencia Artificial puede intervenir
    en cada etapa del proceso audiovisual, mostrando beneficios, riesgos y competencias
    profesionales necesarias.
    """
)


# ---------------------------------------------------------
# FUENTES
# ---------------------------------------------------------

st.header("🔗 Fuentes de referencia")

st.markdown(
    """
    - Organisation for Economic Co-operation and Development (OECD).
    - International Labour Organization (ILO).
    - UNESCO.
    - Stanford Institute for Human-Centered Artificial Intelligence.
    - Reuters Institute for the Study of Journalism.
    - United Nations Conference on Trade and Development (UNCTAD).
    - Artículos científicos sobre IA generativa, creatividad y comunicación audiovisual.

    Las referencias completas deberán integrarse en la bibliografía final del proyecto.
    """
)


# ---------------------------------------------------------
# CONCLUSIÓN
# ---------------------------------------------------------

st.markdown("---")
st.header("🎯 Conclusión")

st.success(
    """
    La Inteligencia Artificial está transformando todas las fases de la
    Comunicación Audiovisual.

    Su verdadero potencial no consiste en reemplazar al profesional, sino en
    potenciar su creatividad, optimizar procesos y apoyar la toma de decisiones.

    El desafío es utilizar estas herramientas de forma ética, crítica,
    estratégica y responsable.
    """
)
