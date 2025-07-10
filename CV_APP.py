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
st.markdown("### 1. Professional Timeline")

timeline_df = pd.DataFrame({
    'Role': [
        "Call Taker",
        "Shift Lead",
        "Knowledge Manager",
        "Incident Manager",
        "Technical Consultant"
    ],
    'Start': [2017, 2018, 2019, 2022, 2023],
    'End':   [2018, 2019, 2022, 2023, 2025],
    'Area': ['Support', 'Incident Management', 'Knowledge Management', 'ITSM', 'Cloud']
})

timeline_df['Duration'] = timeline_df['End'] - timeline_df['Start']

fig_timeline = px.bar(
    timeline_df,
    x="Duration",
    y="Role",
    color="Area",
    orientation="h",
    text="Start",
    hover_data=["Start", "End"],
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig_timeline.update_layout(
    title="Professional Timeline (Role Duration)",
    xaxis_title="Years",
    yaxis_title="Role",
    showlegend=True
)

st.plotly_chart(fig_timeline, use_container_width=True)

# --- 2. Skill meters ---
st.markdown("---")
st.markdown("### 2. Progress Bars / Skill Meters")

skills = {
    "ServiceNow": 90,
    "Azure": 75,
    "AWS": 60,
    "ITSM": 85,
    "Knowledge": 95,
    "Communication Skills": 88,
    "Jira": 70,
    "Confluence": 65
}

for skill, level in skills.items():
    st.write(f"{skill} ({level}%)")
    st.progress(level)

# --- 3. Animated Bubbles ---
st.markdown("---")
st.markdown("### 3. Technical Tools Skills Development Over Time")

tech_df = pd.DataFrame({
    'Year': [2018, 2018, 2019, 2019, 2020, 2021, 2022, 2023],
    'Tool': ['ServiceNow', 'Office 365', 'Jira', 'Azure', 'AWS', 'ServiceNow', 'Jira', 'AWS'],
    'Proficiency': [6, 4, 5, 5, 6, 8, 6, 9],
    'Usage': [60, 40, 50, 50, 60, 80, 60, 90]
})

tech_df['Tool_Year'] = tech_df['Tool'] + '_' + tech_df['Year'].astype(str)

fig_tech = px.scatter(
    tech_df,
    x="Year",
    y="Proficiency",
    size="Usage",
    color="Tool",
    hover_name="Tool",
    animation_frame="Year",
    animation_group="Tool_Year",
    size_max=60,
    range_x=[2017, 2024],
    range_y=[0, 10],
    title="Technical Tools Skills Development Over Time"
)

fig_tech.update_layout(
    xaxis_title="Year",
    yaxis_title="Proficiency (1-10)",
    showlegend=True
)

fig_tech.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
st.plotly_chart(fig_tech, use_container_width=True)

# --- 4. Tools and Platforms Used ---
st.markdown("---")
st.markdown("### 4. Tools and Platforms Used")

tools = {
    "Azure": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Microsoft_Azure.svg",
    "AWS": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
    "ServiceNow": "https://logos-world.net/wp-content/uploads/2022/02/ServiceNow-Emblem.png",
    "Jira": "https://cdn.worldvectorlogo.com/logos/jira-1.svg",
    "Confluence": "https://www.svgrepo.com/show/353597/confluence.svg",
    "Office 365": "https://cdn.worldvectorlogo.com/logos/office-2.svg"
}

cols = st.columns(3)
for i, (name, url) in enumerate(tools.items()):
    with cols[i % 3]:
        st.image(url, width=60)
        st.write(name)

# --- 5. Word Cloud ---
st.markdown("---")
st.markdown("### 5. Word Cloud from CV")

text = "Azure AWS ServiceNow ITSM documentation Trainer Change Management Support Jira Confluence Knowledge Base Customer Services Incident"
wordcloud = WordCloud(width=800, height=300, background_color='white').generate(text)
fig6, ax6 = plt.subplots()
ax6.imshow(wordcloud, interpolation='bilinear')
ax6.axis("off")
st.pyplot(fig6)

# --- Footer ---
st.markdown("---")
st.markdown("Created by Luis Sáenz • [LinkedIn](https://linkedin.com/in/lsaenz)")