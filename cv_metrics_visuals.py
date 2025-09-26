import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
from math import pi

# Page configuration
st.set_page_config(layout="wide", page_title="Visual CV – Luis Sáenz", page_icon="📊")
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    h1, h2, h3 {color: #2c3e50;}
    .stProgress .st-bo {background-color: #e6f3ff;}
    .stSidebar {background-color: #e9ecef;}
    .stButton>button {background-color: #007bff; color: white; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.markdown("Explore the visualizations of Luis Sáenz's CV (updated to September 2025).")
    section = st.selectbox("Select Section", ["All", "Timeline", "Skill Meters", "Technical Tools", "Tools & Platforms", "Word Cloud", "Certifications", "Languages", "Distribution by Company"])

# Title with total experience metric
total_experience = 93  # Total months from analysis
st.title(f"📊 Visual CV – Luis Sáenz | {total_experience // 12} years of IT experience")
st.markdown("Interactive visualization based on CV analysis. Includes metrics such as 7 roles, 8 certifications, and 9 key tools.")

# Embedded data (based on initial analysis)
# Timeline (updated to Sep 2025)
timeline_df = pd.DataFrame({
    'Role': [
        "Call Taker",
        "Shift Lead / SME",
        "Quality Analyst",
        "Knowledge Manager",
        "Incident Manager",
        "Change Manager",
        "Technical Consultant"
    ],
    'Start': [2017.6, 2018.0, 2018.8, 2019.0, 2022.0, 2022.3, 2023.8],
    'End': [2018.0, 2018.8, 2019.0, 2022.0, 2022.3, 2023.3, 2025.75],  # Updated to Sep 2025
    'Area': ['Support', 'Support', 'Quality', 'Knowledge Management', 'ITSM', 'ITSM', 'Cloud']
})
timeline_df['Duration'] = timeline_df['End'] - timeline_df['Start']

# Skill Meters (expanded with categories from analysis)
skills = {
    "ServiceNow": 90,
    "Azure": 80,
    "AWS": 65,
    "ITSM": 85,
    "Knowledge Management": 95,
    "Technical Support": 88,
    "Jira": 75,
    "Confluence": 70,
    "Change Management": 85,
    "Cloud Migration": 75
}

# Technical Tools (animated bubbles, expanded)
tech_df = pd.DataFrame({
    'Year': [2017, 2018, 2018, 2019, 2019, 2020, 2021, 2022, 2023, 2023, 2024, 2025],
    'Tool': ['ServiceNow', 'Jira', 'Confluence', 'ServiceNow', 'Azure', 'AWS', 'ServiceNow', 'Jira', 'Azure', 'AWS', 'SolarWinds', 'Dr. Migrate'],
    'Proficiency': [6, 5, 4, 7, 5, 4, 8, 6, 7, 6, 7, 8],
    'Usage': [60, 50, 40, 70, 50, 40, 80, 60, 80, 70, 75, 85]
})
tech_df['Tool_Year'] = tech_df['Tool'] + '_' + tech_df['Year'].astype(str)

# Tools and Platforms (expanded with more from analysis)
tools = {
    "Azure": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Microsoft_Azure.svg",
    "AWS": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
    "ServiceNow": "https://logos-world.net/wp-content/uploads/2022/02/ServiceNow-Emblem.png",
    "Jira": "https://cdn.worldvectorlogo.com/logos/jira-1.svg",
    "Confluence": "https://www.svgrepo.com/show/353597/confluence.svg",
    "M365": "https://cdn.worldvectorlogo.com/logos/office-2.svg",
    "SolarWinds": "https://www.svgrepo.com/show/303661/solarwinds.svg",
    "GitHub": "https://cdn.worldvectorlogo.com/logos/github-icon.svg",
    "Render": "https://www.svgrepo.com/show/354057/render.svg"
}

# Word Cloud (with frequencies from initial analysis)
word_freq = {
    "ITSM": 9,
    "ServiceNow": 7,
    "Cloud": 6,
    "Azure": 6,
    "Incident": 8,
    "Change": 7,
    "Technical": 6,
    "Support": 10,
    "Management": 10,
    "Knowledge": 4
}
wc = WordCloud(width=800, height=300, background_color='white', colormap='viridis').generate_from_frequencies(word_freq)

# Certifications by Year (from analysis)
certs_df = pd.DataFrame({
    'Year': [2017, 2019, 2019, 2022, 2023, 2023, 2023, 2025],
    'Certification': ['CompTIA A+', 'Azure Essentials', 'ITIL 4 Foundation', 'Scrum Master', 'Azure Fundamentals', 'Data Fundamentals', 'Change Management', 'Data Analyst']
})
certs_count = certs_df.groupby('Year').size().reset_index(name='Count')

# Languages (from analysis)
languages_data = {
    'Language': ['Spanish', 'English', 'French'],
    'Level': [5, 5, 1]  # Native=5, C2=5, A2=1
}
df_languages = pd.DataFrame(languages_data)

# Distribution by Company (updated with roles)
company_data = pd.DataFrame({
    'Role/Company': [
        "Call Taker (TCS)",
        "Shift Lead / SME (TCS)",
        "Quality Analyst (TCS)",
        "Knowledge Manager (TCS)",
        "Incident Manager (TCS)",
        "Change Manager (TCS)",
        "Technical Consultant (INVISO)"
    ],
    'Months': [5, 9, 3, 36, 3, 12, 24]  # Calculated from CV timeline
})

# Visualizations
# 1. Timeline
if section in ["All", "Timeline"]:
    st.markdown("---")
    st.markdown("### 1. Professional Timeline")
    st.markdown("Duration of roles (2017-2025), with key areas.")
    fig_timeline = px.bar(
        timeline_df,
        x="Duration",
        y="Role",
        color="Area",
        orientation="h",
        text="Duration",
        hover_data=["Start", "End"],
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_timeline.update_layout(
        title="Professional Timeline",
        xaxis_title="Years",
        yaxis_title="Role",
        showlegend=True
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

# 2. Skill Meters
if section in ["All", "Skill Meters"]:
    st.markdown("---")
    st.markdown("### 2. Progress Bars: Skills")
    st.markdown("Proficiencies in 10 key categories (0-100%).")
    cols = st.columns(2)
    for i, (skill, level) in enumerate(skills.items()):
        with cols[i % 2]:
            st.write(f"**{skill}** ({level}%)")
            st.progress(level)

# 3. Animated Bubbles
if section in ["All", "Technical Tools"]:
    st.markdown("---")
    st.markdown("### 3. Development of Tool Proficiencies")
    st.markdown("Evolution with animation by year (size = usage, color = tool).")
    # Initialize figure
    fig_tech = go.Figure()
    # Define colors for each tool
    colors = {
        'ServiceNow': '#636EFA',
        'Jira': '#00CC96',
        'Confluence': '#EF553B',
        'Azure': '#FF7F0E',
        'AWS': '#FFBB78',
        'SolarWinds': '#2CA02C',
        'Dr. Migrate': '#D62728'
    }
    # Add scatter traces for each tool
    for tool in tech_df['Tool'].unique():
        tool_data = tech_df[tech_df['Tool'] == tool]
        fig_tech.add_trace(
            go.Scatter(
                x=tool_data['Year'],
                y=tool_data['Proficiency'],
                mode='markers',
                name=tool,
                marker=dict(
                    size=tool_data['Usage'],
                    sizemode='area',
                    sizeref=2.0 * max(tech_df['Usage']) / (60**2),
                    sizemin=10,
                    line=dict(width=1, color='DarkSlateGrey'),
                    color=colors[tool]
                ),
                hovertemplate='%{x}, Proficiency: %{y}<br>Tool: %{text}<br>Usage: %{marker.size}',
                text=[tool] * len(tool_data)
            )
        )
    # Create animation frames
    frames = []
    for year in sorted(tech_df['Year'].unique()):
        frame_data = []
        for tool in tech_df['Tool'].unique():
            tool_data = tech_df[(tech_df['Tool'] == tool) & (tech_df['Year'] == year)]
            frame_data.append(
                go.Scatter(
                    x=tool_data['Year'],
                    y=tool_data['Proficiency'],
                    mode='markers',
                    name=tool,
                    marker=dict(
                        size=tool_data['Usage'],
                        sizemode='area',
                        sizeref=2.0 * max(tech_df['Usage']) / (60**2),
                        sizemin=10,
                        line=dict(width=1, color='DarkSlateGrey'),
                        color=colors[tool]
                    ),
                    hovertemplate='%{x}, Proficiency: %{y}<br>Tool: %{text}<br>Usage: %{marker.size}',
                    text=[tool] * len(tool_data)
                )
            )
        frames.append(go.Frame(data=frame_data, name=str(year)))
    # Update figure with frames and animation settings
    fig_tech.update(frames=frames)
    fig_tech.update_layout(
        xaxis_title="Year",
        yaxis_title="Proficiency (1-10)",
        title="Development of Technical Tools",
        showlegend=True,
        legend=dict(title="Tool", tracegroupgap=0),
        xaxis=dict(range=[2017, 2026], tickmode='linear', dtick=1),
        yaxis=dict(range=[0, 10]),
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": True,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }],
        sliders=[{
            "steps": [
                {"args": [[str(year)], {"frame": {"duration": 500, "redraw": True}, "mode": "immediate"}],
                 "label": str(year),
                 "method": "animate"} for year in sorted(tech_df['Year'].unique())
            ],
            "x": 0.1,
            "len": 0.9,
            "xanchor": "left",
            "y": 0,
            "yanchor": "top",
            "pad": {"b": 10, "t": 50},
            "currentvalue": {"xanchor": "right", "prefix": "Year: ", "font": {"size": 20}}
        }]
    )
    st.plotly_chart(fig_tech, use_container_width=True)

# 4. Tools and Platforms
if section in ["All", "Tools & Platforms"]:
    st.markdown("---")
    st.markdown("### 4. Tools and Platforms (9 key)")
    cols = st.columns(3)
    for i, (name, url) in enumerate(tools.items()):
        with cols[i % 3]:
            st.image(url, width=60)
            st.caption(name)

# 5. Word Cloud
if section in ["All", "Word Cloud"]:
    st.markdown("---")
    st.markdown("### 5. Word Cloud (Top 10 from Analysis)")
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wc, interpolation='bilinear')
    ax_wc.axis("off")
    st.pyplot(fig_wc)

# 6. Certifications
if section in ["All", "Certifications"]:
    st.markdown("---")
    st.markdown("### 6. Certifications by Year (8 total)")
    fig_certs = px.bar(
        certs_count,
        x="Year",
        y="Count",
        title="Evolution of Certifications",
        color_discrete_sequence=['#FF6B6B']
    )
    fig_certs.update_layout(xaxis_title="Year", yaxis_title="Number of Certifications")
    st.plotly_chart(fig_certs, use_container_width=True)
    st.markdown("**Full List:** CompTIA A+ (2017), Azure Essentials & ITIL 4 Foundation (2019), Scrum Master (2022), Azure Fundamentals, Data Fundamentals & Change Management (2023), Data Analyst (2025).")

# 7. Languages
if section in ["All", "Languages"]:
    st.markdown("---")
    st.markdown("### 7. Language Proficiencies (Scale 1-5)")
    categories = df_languages["Language"].tolist()
    values = df_languages["Level"].tolist()
    values += values[:1]
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]
    fig_radar, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color="skyblue", alpha=0.4)
    ax.plot(angles, values, color="blue", linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Language Radar", size=20, color="navy", pad=20)
    plt.tight_layout()
    st.pyplot(fig_radar)

# 8. Distribution by Company
if section in ["All", "Distribution by Company"]:
    st.markdown("---")
    st.markdown("### 8. Time Distribution by Role/Company (93 months total)")
    fig_company = px.pie(
        company_data,
        values="Months",
        names="Role/Company",
        title="Time by Role/Company",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_company.update_traces(
        textinfo="percent+label",
        pull=[0, 0, 0, 0.1, 0, 0, 0.1]  # Highlight Knowledge Manager and Technical Consultant
    )
    st.plotly_chart(fig_company, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Created with analysis of Luis Sáenz's CV** • [LinkedIn](https://linkedin.com/in/lsaenz) • Updated to September 2025")