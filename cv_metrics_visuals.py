import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from math import pi
from wordcloud import WordCloud
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visual CV – Luis Sáenz")

# --- 1. Timeline ---
st.markdown("---")
st.markdown("### 1. Timeline profesional")

timeline_df = pd.DataFrame({
    'Rol': [
        "Call Taker",
        "Shift Lead",
        "Knowledge Manager",
        "Incident Manager",
        "Consultor Técnico"
    ],
    'Inicio': [2017, 2018, 2019, 2022, 2023],
    'Fin':    [2018, 2019, 2022, 2023, 2025],
    'Área': ['Soporte', 'Gestión', 'Documentación', 'ITSM', 'Cloud']
})

timeline_df['Duración'] = timeline_df['Fin'] - timeline_df['Inicio']

fig_timeline = px.bar(
    timeline_df,
    x="Duración",
    y="Rol",
    color="Área",
    orientation="h",
    text="Inicio",
    hover_data=["Inicio", "Fin"],
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig_timeline.update_layout(
    title="Timeline profesional (duración por rol)",
    xaxis_title="Años",
    yaxis_title="Rol",
    showlegend=True
)

st.plotly_chart(fig_timeline, use_container_width=True)

# --- 2. Radar ---
st.markdown("---")
st.markdown("### 2. Radar de competencias principales")

radar_labels = ['ITSM', 'Soporte Técnico', 'Cloud', 'Documentación', 'Gestión de Cambios', 'Entrenamiento']
values = [9, 8, 7, 9, 7, 8]
values += values[:1]
angles = [n / float(len(radar_labels)) * 2 * pi for n in range(len(radar_labels))]
angles += angles[:1]

fig2, ax2 = plt.subplots(figsize=(2, 2), subplot_kw=dict(polar=True))

# Graficar
ax2.plot(angles, values, linewidth=1, linestyle='solid')
ax2.fill(angles, values, 'skyblue', alpha=0.4)

# Ajustar etiquetas
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(radar_labels, fontsize=6, wrap=True)

# Opcional: quitar etiquetas del eje radial
ax2.set_yticklabels([])
ax2.tick_params(axis='x', pad=4)  # separa un poco las etiquetas del centro

st.pyplot(fig2)

# --- 3. Heatmap ---
st.markdown("---")
st.markdown("### 3. Mapa de calor de habilidades por año")

heat_data = pd.DataFrame({
    'ServiceNow': [1, 1, 1, 1, 1, 1],
    'Azure': [0, 0, 0, 1, 1, 1],
    'AWS': [0, 0, 0, 0, 0, 1],
    'Jira': [0, 0, 0, 0, 1, 1],
    'Gestión de Cambios': [0, 0, 0, 0, 1, 1]
}, index=["2018", "2019", "2020", "2021", "2022", "2023"])

fig3, ax3 = plt.subplots()
sns.heatmap(heat_data.T, cmap="YlGnBu", cbar=False, linewidths=1, linecolor='white', ax=ax3)
st.pyplot(fig3)

# --- 4. Evolución de herramientas técnicas (burbujas animadas) ---
st.markdown("---")
st.markdown("### 4. Evolución de herramientas técnicas (burbujas animadas)")

tech_df = pd.DataFrame({
    'Año': [2018, 2018, 2019, 2019, 2020, 2021, 2022, 2023],
    'Herramienta': ['ServiceNow', 'Office 365', 'Jira', 'Azure', 'AWS', 'ServiceNow', 'Jira', 'AWS'],
    'Dominio': [6, 4, 5, 5, 6, 8, 6, 9],
    'Uso': [60, 40, 50, 50, 60, 80, 60, 90]
})

# Añadir esta línea clave para evitar agrupamiento no deseado
tech_df['Herramienta_Año'] = tech_df['Herramienta'] + '_' + tech_df['Año'].astype(str)

fig_tech = px.scatter(
    tech_df,
    x="Año",
    y="Dominio",
    size="Uso",
    color="Herramienta",
    hover_name="Herramienta",
    animation_frame="Año",
    animation_group="Herramienta_Año",  # Esto evita que se mezclen las burbujas
    size_max=60,
    range_x=[2017, 2024],
    range_y=[0, 10],
    title="Evolución del dominio en herramientas técnicas"
)

fig_tech.update_layout(
    xaxis_title="Año",
    yaxis_title="Nivel de dominio (1-10)",
    showlegend=True
)

# Asegurar que todas las herramientas aparezcan en la leyenda
fig_tech.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

st.plotly_chart(fig_tech, use_container_width=True)

# --- 5. Logos / Tools map ---
st.markdown("---")
st.markdown("### 5. Herramientas y plataformas utilizadas")

tools = {
    "Azure": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Microsoft_Azure.svg",
    "AWS": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
    "ServiceNow": "https://upload.wikimedia.org/wikipedia/commons/7/7a/ServiceNow_logo.svg",
    "Jira": "https://upload.wikimedia.org/wikipedia/en/8/8e/Jira_Logo.png",
    "Confluence": "https://upload.wikimedia.org/wikipedia/en/e/e3/Confluence_Logo.png",
    "Office 365": "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_Office_logo_%282013–2019%29.svg"
}

cols = st.columns(3)
for i, (name, url) in enumerate(tools.items()):
    with cols[i % 3]:
        st.image(url, width=60)
        st.write(name)

# --- 6. Word Cloud ---
st.markdown("---")
st.markdown("### 6. Nube de palabras del CV")

text = "Azure AWS ServiceNow ITSM documentación Trainer Change Management Support Jira Confluence Knowledge Base Customer Services Incident"
wordcloud = WordCloud(width=800, height=300, background_color='white').generate(text)
fig6, ax6 = plt.subplots()
ax6.imshow(wordcloud, interpolation='bilinear')
ax6.axis("off")
st.pyplot(fig6)

# --- 7. Skill meters ---
st.markdown("---")
st.markdown("### 7. Progress Bars / Skill Meters")

skills = {
    "ServiceNow": 90,
    "Azure": 75,
    "AWS": 60,
    "ITSM": 85,
    "Documentación": 95,
    "Comunicación": 88,
    "Jira": 70,
    "Confluence": 65
}

for skill, level in skills.items():
    st.write(f"{skill} ({level}%)")
    st.progress(level)

# --- Footer ---
st.markdown("---")
st.markdown("Created by Luis Sáenz • [LinkedIn](https://linkedin.com/in/lsaenz)")