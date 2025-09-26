# Visual CV Dashboard for Luis Sáenz 📊✨

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

**Welcome to the Visual CV Dashboard!** This interactive Streamlit application showcases the professional journey of Luis Sáenz through dynamic visualizations, highlighting roles, skills, tools, certifications, and more. Built with Python and Plotly, it brings the CV to life with colorful charts and animations! 🚀

![Dashboard Preview](https://via.placeholder.com/800x400/4F46E5/FFFFFF?text=Visual+CV+Dashboard+Preview)

## 📖 Overview

This project transforms Luis Sáenz's CV into an interactive dashboard, featuring:

### 📊 Dashboard Features
- **Professional Timeline 📅**: Horizontal bar chart showing 7 roles from 2017 to 2025
- **Skill Meters 📈**: Progress bars for 10 key skills (ServiceNow, Azure, ITSM, etc.)
- **Technical Tools 🔧**: Animated bubble chart tracking proficiency and usage
- **Tools & Platforms 🛠️**: Logo gallery of 9 key technologies
- **Word Cloud ☁️**: Top 10 terms emphasizing ITSM, Cloud, and Support
- **Certifications 🎓**: Bar chart of 8 certifications (2017-2025)
- **Languages 🌐**: Radar chart showing Spanish, English, and French proficiency
- **Time by Role/Company 🕒**: Pie chart breaking down 93 months across roles

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** 🐍
- **Required Packages**: Streamlit, Pandas, Plotly, WordCloud

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/visual-cv-luis-saenz.git
   cd visual-cv-luis-saenz
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
streamlit run visual_cv.py
Open your browser at http://localhost:8501 to explore the dashboard! 🌐

🎨 Key Features
Feature	Description	Technology
Interactive Navigation 🧭	Sidebar for section selection	Streamlit
Dynamic Animations 🎥	Animated bubble chart (2017–2025)	Plotly
Responsive Design 📱	Optimized for desktop and mobile	CSS
Custom Styling ✨	Modern color palette and themes	Plotly + CSS
📈 Metrics Highlight
7 professional roles

8 certifications

93 months of experience

10 key skills tracked

9 technical tools visualized

📂 Project Structure
text
visual-cv-luis-saenz/
├── visual_cv.py          # Main Streamlit application 🎯
├── requirements.txt      # Python dependencies 📋
├── assets/              # Images and logos (optional)
│   ├── logos/
│   └── screenshots/
└── README.md            # This file 📖
🛠️ Customization Guide
Adding New Data ➕
Update the DataFrames in visual_cv.py:

python
# Example: Add new skills
skills = {
    'ServiceNow': 95,
    'Azure': 85,
    'ITSM': 90,
    # Add your skills here
}
Changing Colors 🎨
Modify the color scheme in Plotly charts:

python
fig.update_layout(
    colorway=['#4F46E5', '#10B981', '#F59E0B', '#EF4444']
)
Extending Visuals 📉
Add new sections by following existing patterns:

python
with st.container():
    st.subheader("New Visualization")
    # Your chart code here
📊 Data Sources
Based on Luis Sáenz's CV (updated September 2025):

🏢 Professional Experience
TCS Roles: Call Taker → Shift Lead → Quality Analyst → Knowledge Manager → Incident Manager → Change Manager

INVISO Role: Technical Consultant

🔧 Technical Stack
Platforms: ServiceNow, Jira, Confluence, Azure, AWS

Tools: SolarWinds, Dr. Migrate, M365, GitHub, Render

Certifications: CompTIA A+, Azure Essentials, ITIL 4, Scrum Master, etc.

🤝 Contributing
We welcome contributions! 🙌

Fork the repo 🍴

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m "Add amazing feature"

Push to branch: git push origin feature/amazing-feature

Open a Pull Request 🚀

📬 Connect
Let's talk! Connect with Luis Sáenz for more details about his professional journey:

https://img.shields.io/badge/LinkedIn-Connect%2520with%2520Luis%2520S%C3%A1enz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white

Created with 💻 and ❤️ by the Luis Saenz Visual CV Team • Updated September 2025 🗓️