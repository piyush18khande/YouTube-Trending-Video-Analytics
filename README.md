# YouTube-Trending-Video-Analytics
This project is a full-stack **YouTube Analytics Dashboard** built using **SQL, Python, and Power BI**.
# YouTube Content Intelligence Platform

🚀 This project is a full-stack **YouTube Analytics Dashboard** built using **SQL, Python, and Power BI**.  
It helps creators and analysts uncover trends in **views, likes, comments, and subscribers** to optimize their content strategy.  

## 🔑 Features
- **SQL (MySQL Workbench):**
  - Structured raw YouTube data (videos, channels, comments).
  - Wrote queries for KPIs like Top 10 Videos, Engagement Rate, Subscriber Growth.
- **Python:**
  - Preprocessed data for analysis.
  - (Optional) Performed NLP on comments for sentiment insights.
- **Power BI:**
  - Built interactive dashboards with slicers, KPIs, and visuals.
  - Engagement Funnel, Engagement Mix (Donut Chart), Subscriber Growth KPI, Top Videos chart.

## 📊 Insights Delivered
- *Top 10 videos account for ~60% of total views.*
- Engagement breakdown (% Likes vs % Comments vs % Shares).
- Subscriber growth trends with KPIs.
- Recommendations for content strategy.

## 📂 Project Structure
📁 YouTube-Analytics-Project
┣ 📜 youtube.py # Python script for data extraction (YouTube API)
┣ 📜 Sentiments.py # (Optional) NLP sentiment analysis on comments
┣ 📜 schema.sql # MySQL tables creation script
┣ 📜 queries.sql # SQL queries for KPIs & insights
┣ 📊 PowerBI_Dashboard.pbix # Power BI dashboard file
┣ 📜 requirements.txt # Python dependencies
┗ 📜 README.md # Project documentation


## 🛠️ Tech Stack
- **SQL (MySQL Workbench)** → Data modeling & KPIs.
- **Python (pandas, matplotlib, nltk, wordcloud)** → Data prep & analytics.
- **Power BI** → Interactive dashboards.

## 🚀 How to Run
1. Clone this repo.
2. Import `schema.sql` into MySQL Workbench.
3. Load your dataset (from YouTube API or CSV) into the tables.
4. Run `youtube.py` or `Sentiments.py` for preprocessing.
5. Open `PowerBI_Dashboard.pbix` → Connect to SQL database → Refresh data.

## 📌 Future Enhancements
- Add ML model for **view prediction** based on early engagement.
- Improve NLP analysis for **comment sentiment trends**.
- Automate ETL pipeline for live updates.
