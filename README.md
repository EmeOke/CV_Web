Visual CV Dashboard for Luis Sáenz 📊✨
Welcome to the Visual CV Dashboard! This interactive Streamlit application showcases the professional journey of Luis Sáenz through dynamic visualizations, highlighting roles, skills, tools, certifications, and more. Built with Python and Plotly, it brings the CV to life with colorful charts and animations! 🚀
📖 Overview
This project transforms Luis Sáenz's CV into an interactive dashboard, featuring:

Professional Timeline 📅: A horizontal bar chart showing 7 roles from 2017 to 2025.
Skill Meters 📈: Progress bars for 10 key skills (e.g., ServiceNow, Azure, ITSM).
Technical Tools 🔧: Animated bubble chart tracking proficiency and usage of tools like ServiceNow, Jira, and AWS.
Tools & Platforms 🛠️: Logo gallery of 9 key technologies.
Word Cloud ☁️: Top 10 terms from the CV, emphasizing ITSM, Cloud, and Support.
Certifications 🎓: Bar chart of 8 certifications earned from 2017 to 2025.
Languages 🌐: Radar chart showing proficiency in Spanish, English, and French.
Time by Role/Company 🕒: Pie chart breaking down 93 months across 6 TCS roles and 1 INVISO role.

🚀 Getting Started
Prerequisites

Python 3.8+ 🐍
Streamlit, Pandas, Matplotlib, Seaborn, WordCloud, Plotly 📚

Installation

Clone the repository:git clone https://github.com/your-repo/visual-cv-luis-saenz.git


Navigate to the project directory:cd visual-cv-luis-saenz


Install dependencies:pip install -r requirements.txt



Running the App
Run the Streamlit app locally:
streamlit run visual_cv.py

Open your browser at http://localhost:8501 to explore the dashboard! 🌐
🎨 Features

Interactive Navigation 🧭: Use the sidebar to select specific sections or view all visualizations.
Dynamic Animations 🎥: The bubble chart animates tool proficiency over time (2017–2025).
Responsive Design 📱: Wide layout with clean styling for desktop and mobile.
Emphasized Metrics 📊: Highlights 7 roles, 8 certifications, and 93 months of experience.
Custom Styling ✨: Uses a modern color palette and CSS for a polished look.

📂 Project Structure
visual-cv-luis-saenz/
├── visual_cv.py       # Main Streamlit application 🎯
├── requirements.txt   # Dependencies 📋
├── README.md          # This file 📖

📈 Data Sources
The visualizations are based on Luis Sáenz's CV (updated to September 2025), with:

Roles: 6 at TCS (Call Taker, Shift Lead, Quality Analyst, Knowledge Manager, Incident Manager, Change Manager) and 1 at INVISO (Technical Consultant).
Tools: ServiceNow, Jira, Confluence, Azure, AWS, SolarWinds, Dr. Migrate, M365, GitHub, Render.
Certifications: CompTIA A+, Azure Essentials, ITIL 4, Scrum Master, and more.

🛠️ Customization
Want to tweak the dashboard? Here’s how:

Add New Data ➕: Update timeline_df, skills, tech_df, or other DataFrames in visual_cv.py.
Change Colors 🎨: Modify the color_discrete_sequence in Plotly charts or CSS in st.markdown.
Extend Visuals 📉: Add new sections by following the structure of existing visualizations.

🤝 Contributing
Contributions are welcome! 🙌

Fork the repo 🍴
Create a new branch (git checkout -b feature/awesome-addition)
Commit your changes (git commit -m "Added awesome feature")
Push to the branch (git push origin feature/awesome-addition)
Open a Pull Request 🚀

📬 Contact
Connect with <a href="https://www.linkedin.com/in/lsaenz" target="_blank">Luis Sáenz</a> on LinkedIn for more details about his professional journey! 📩

Created with 💻 and ❤️ by the Luis Saenz Visual CV Team • Updated September 2025 🗓️