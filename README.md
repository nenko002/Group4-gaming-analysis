# 🎮 Group 4: Global Gaming Analysis with PySpark

This project is the final submission for the **DS203: Big Data Fundamentals** course. It presents a cross-platform analysis of gaming behavior using **PySpark** and structured datasets from **Steam**, **PlayStation**, and **Xbox**. Our main goal is to analyze player engagement, pricing trends, and platform-specific dynamics by handling over **1GB of CSV-based game and player data**.

---

## 📁 Project Structure

/steam/ - Steam-specific CSV files and analysis script
/playstation/ - PlayStation CSV files and analysis script
/xbox/ - Xbox CSV files and analysis script
/data/ - Placeholder folder (excluded from Git) for large raw datasets
/images/ - Visualizations, flowcharts, and screenshots
/report/ - Final report in Markdown
Main_steam.py - PySpark analysis for Steam
Main_playstation.py - PySpark analysis for PlayStation
Main_xbox.py - PySpark analysis for Xbox
.gitignore - Excludes /data and system files
README.md - You're here!

yaml
Copy
Edit

---

## 📊 Dataset Source

The dataset used was obtained from Kaggle and includes anonymized player profiles and game metadata across platforms:

🔗 **[Gaming Profiles 2025 – Steam, PlayStation, Xbox](https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox)**

⚠️ **Note:** Raw dataset files are excluded from this Git repository due to size (>1GB). To run the project locally, download the dataset from Kaggle and place the CSV files under each platform folder.

---

## 🛠️ How to Run

### Requirements:
- Python 3.x
- PySpark installed:  
```bash
pip install pyspark
Run the analysis:
bash
Copy
Edit
# For Steam:
python Main_steam.py

# For Xbox:
python Main_xbox.py

# For PlayStation:
python Main_playstation.py
🧠 Key Features
✅ Cross-platform comparison: Steam vs. PlayStation vs. Xbox

📊 Ranking players by total game ownership

🌐 Synthetic grouping of Xbox players (missing region data)

🌎 Aggregation of average game counts by region

💰 Genre and pricing insights

🖼️ Visualizations
We are working on publishing key visualizations here. Samples include:

📈 Average Games per Player by Platform

🧍 Top Players by Total Library Size

🌍 Game Ownership by Country

Folder: /images/

📄 Final Report
The complete methodology, data cleaning, analysis operations, and insights are available in our final project report:

📘 report/final_report.md

👥 Team
Alemu Nenko

Daniel Beltran

Langara College, DS203 – April 2025

🔒 Git History & .gitignore
This repository uses .gitignore to exclude:

/data/ – raw CSV files (>1GB)

Cache files and temporary editor outputs

Please make sure to download the dataset manually from Kaggle before running the PySpark scripts.

