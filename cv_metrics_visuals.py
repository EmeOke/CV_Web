import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
import numpy as np

# ----- 1. Experiencia por empresa/rol -----
experiencia = {
    'Inviso (Consultor Técnico)': 0.75,
    'TCS - Change Manager': 1.0,
    'TCS - Incident Manager': 0.3,
    'TCS - Knowledge Manager': 3.0,
    'TCS - QA / Lead': 0.3,
    'TCS - Shift Lead': 0.75,
    'TCS - Call Taker': 0.4
}

plt.figure(figsize=(10,6))
sns.barplot(x=list(experiencia.values()), y=list(experiencia.keys()), palette='Blues_d')
plt.xlabel("Años de experiencia")
plt.title("Experiencia por Rol / Empresa")
plt.tight_layout()
plt.savefig("experiencia_por_rol.png")
plt.close()


# ----- 2. Herramientas / tecnologías -----
tecnologias = {
    'Azure': 1,
    'AWS': 1,
    'ServiceNow': 1,
    'Jira': 1,
    'Confluence': 1,
    'Office 365': 1,
    'SolarWinds': 1,
    'AirWatch': 1,
    'Dr. Migrate': 1
}
tecnologias_df = pd.DataFrame(list(tecnologias.items()), columns=['Herramienta', 'Relevancia'])

plt.figure(figsize=(10,6))
sns.barplot(data=tecnologias_df, x='Relevancia', y='Herramienta', palette='viridis')
plt.title("Distribución de Tecnologías en el CV")
plt.tight_layout()
plt.savefig("tecnologias_cv.png")
plt.close()


# ----- 3. Certificaciones por año -----
certificaciones = {
    2017: 1,
    2019: 2,
    2022: 1,
    2023: 3,
    2025: 1
}
cert_df = pd.DataFrame(list(certificaciones.items()), columns=["Año", "Certificaciones"])
cert_df.sort_values("Año", inplace=True)

plt.figure(figsize=(8,5))
sns.lineplot(data=cert_df, x="Año", y="Certificaciones", marker="o")
plt.xticks(cert_df["Año"])
plt.title("Certificaciones por Año")
plt.tight_layout()
plt.savefig("certificaciones_por_ano.png")
plt.close()


# ----- 4. Idiomas -----
from math import pi

idiomas = {
    'Español': 5,
    'Inglés': 5,
    'Francés': 2
}
idiomas_df = pd.DataFrame({
    'Idioma': list(idiomas.keys()),
    'Nivel': list(idiomas.values())
})
# Radar chart
labels = idiomas_df['Idioma'].tolist()
stats = idiomas_df['Nivel'].tolist()
stats += stats[:1]
labels += labels[:1]

angles = [n / float(len(labels)) * 2 * pi for n in range(len(labels))]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, stats, linewidth=1, linestyle='solid')
ax.fill(angles, stats, 'skyblue', alpha=0.4)
ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(labels)
plt.title("Nivel de Idiomas")
plt.savefig("idiomas_radar.png")
plt.close()


# ----- 5. Evolución profesional (línea del tiempo simplificada) -----
timeline = {
    "2017": "Call Taker",
    "2018": "Shift Lead",
    "2019": "Knowledge Manager",
    "2022": "Incident / Change Manager",
    "2023": "Consultor Técnico"
}
years = list(timeline.keys())
roles = list(timeline.values())

plt.figure(figsize=(10,4))
plt.plot(years, roles, marker="o")
for i, role in enumerate(roles):
    plt.text(years[i], role, role, fontsize=9, ha='right')
plt.title("Evolución Profesional")
plt.ylabel("Rol")
plt.grid(True, axis='x')
plt.tight_layout()
plt.savefig("evolucion_profesional.png")
plt.close()