🌟 Luis Sáenz's Visual CV Dashboard 📊
Welcome to the Visual CV Dashboard, an interactive Streamlit application that brings Luis Sáenz's professional journey to life! 🚀 This dynamic platform uses vibrant visualizations to showcase roles, skills, certifications, and technical expertise. Powered by Python and Plotly, it transforms a traditional CV into an engaging, animated experience.

📖 Project Overview
This project reimagines Luis Sáenz's CV as an interactive dashboard, highlighting his professional milestones through:

Professional Timeline 📅: A horizontal bar chart tracing 7 roles from 2017 to 2025.
Skill Meters 📈: Progress bars showcasing proficiency in 10 key skills, including ServiceNow, Azure, and ITSM.
Technical Tools 🔧: An animated bubble chart illustrating proficiency and usage of tools like ServiceNow, Jira, and AWS.
Tools & Platforms Gallery 🛠️: A visual showcase of 9 key technologies with their logos.
Word Cloud ☁️: A vibrant display of the top 10 terms from the CV, emphasizing ITSM, Cloud, and Support.
Certifications 🎓: A bar chart highlighting 8 certifications earned between 2017 and 2025.
Languages 🌐: A radar chart displaying proficiency in Spanish, English, and French.
Time by Role/Company 🕒: A pie chart breaking down 93 months across 6 TCS roles and 1 INVISO role.


🚀 Getting Started
Prerequisites
To run the dashboard, ensure you have:

Python 3.8+ 🐍
Required libraries: Streamlit, Pandas, Matplotlib, Seaborn, WordCloud, Plotly 📚

Installation

Clone the repository:git clone https://github.com/your-repo/visual-cv-luis-saenz.git


Navigate to the project directory:cd visual-cv-luis-saenz


Install dependencies:pip install -r requirements.txt



Running the App
Launch the Streamlit app locally:
streamlit run visual_cv.py

Open your browser at http://localhost:8501 to explore the dashboard! 🌐

🎨 Key Features

Interactive Navigation 🧭: Use the sidebar to jump between sections or view all visualizations.
Dynamic Animations 🎥: Watch tool proficiency evolve over time (2017–2025) in the bubble chart.
Responsive Design 📱: Optimized for both desktop and mobile with a clean, wide layout.
Highlighted Metrics 📊: Showcases 7 roles, 8 certifications, and 93 months of professional experience.
Custom Styling ✨: Features a modern color palette and polished CSS for a professional look.


📂 Project Structure
visual-cv-luis-saenz/
├── visual_cv.py         # Main Streamlit application 🎯
├── requirements.txt     # Dependencies 📋
├── README.md           # Project documentation 📖


📈 Data Sources
The visualizations are powered by Luis Sáenz's CV (updated September 2025), including:

Roles: 6 at TCS (Call Taker, Shift Lead, Quality Analyst, Knowledge Manager, Incident Manager, Change Manager) and 1 at INVISO (Technical Consultant).
Tools: ServiceNow, Jira, Confluence, Azure, AWS, SolarWinds, Dr. Migrate, M365, GitHub, Render.
Certifications: CompTIA A+, Azure Essentials, ITIL 4, Scrum Master, and more.


🛠️ Customization Guide
Tailor the dashboard to your needs:

Add New Data ➕: Update timeline_df, skills, tech_df, or other DataFrames in visual_cv.py.
Change Colors 🎨: Adjust the color_discrete_sequence in Plotly charts or modify CSS in st.markdown.
Extend Visualizations 📉: Create new sections by following the structure of existing charts.


🤝 Contributing
We welcome contributions to enhance the dashboard! 🙌 Follow these steps:

Fork the repository 🍴
Create a new branch:git checkout -b feature/awesome-addition


Commit your changes:git commit -m "Added awesome feature"


Push to the branch:git push origin feature/awesome-addition


Open a Pull Request 🚀


📬 Connect with Luis
Reach out to Luis Sáenz on LinkedIn to learn more about his professional journey! 📩

Created with 💻 and ❤️ by the Luis Sáenz Visual CV TeamLast Updated: September 2025 🗓️