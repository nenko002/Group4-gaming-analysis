# 🎮 Group 4: Global Gaming Analysis with PySpark

This project is the final submission for the **DS203: Big Data Fundamentals** course. It presents a cross-platform analysis of gaming behavior using PySpark and structured datasets from **Steam**, **PlayStation**, and **Xbox**. Our main goal is to analyze player engagement, pricing trends, and platform-specific dynamics by handling over 1GB of CSV-based game and player data.

---

## 📁 Project Structure

/steam/ - Contains Steam-specific CSV files and scripts
/playstation/ - Contains PlayStation CSV files and scripts
/xbox/ - Contains Xbox CSV files and scripts
/data/ - Placeholder folder (excluded from Git) for large raw CSV datasets
/images/ - Visualizations, flowcharts, and screenshots
/report/ - Final markdown report for the project
Main_steam.py - PySpark analysis for Steam
Main_playstation.py - PySpark analysis for PlayStation
Main_xbox.py - PySpark analysis for Xbox
.gitignore - Configuration to exclude large files and system artifacts
README.md - You are here!

yaml
Copy
Edit

---

## 📊 Dataset Source

The dataset used was obtained from Kaggle and includes anonymized gaming profiles and game metadata across three platforms:

🔗 [Gaming Profiles 2025 – Steam, PlayStation, Xbox (Kaggle)](https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox)

We excluded raw data files (>1GB) from this Git repository to keep it lightweight. To run this project locally, download the dataset from the Kaggle link above and place the CSV files under the respective platform folders.

---

## 🛠️ How to Run

This project uses **PySpark**. You can run the analysis for each platform using the following commands:

```bash
# Example: Run Steam analysis
python Main_steam.py

# Example: Run Xbox analysis
python Main_xbox.py

# Example: Run PlayStation analysis
python Main_playstation.py
Make sure you have a virtual environment set up with PySpark installed. You can install PySpark using:

bash
Copy
Edit
pip install pyspark
🧠 Key Features
Cross-platform comparison: Steam vs. PlayStation vs. Xbox

Ranking players by total game ownership

Synthetic grouping of Xbox players to handle missing country data

Aggregation of average game counts by region

Genre and pricing insights

👥 Team
Alemu Nenko

Daniel

Langara College, DS203 - April 2025

📄 Final Report
The full methodology, findings, and challenges are described in our project report.

🔒 Note on Git History
We used .gitignore to exclude:

/data/ folder with >1GB datasets

System cache files and temporary editor outputs

Please download the dataset locally before executing the PySpark scripts.

yaml
Copy
Edit

---

Once you're ready:

1. Paste it into the terminal using:
   ```bash
   nano README.md# DS203 Final Project – Cross-Platform Gaming Data Analysis

This project explores and compares gaming behavior on Steam, Xbox, and PlayStation using PySpark. The analysis includes:

- Player engagement by platform
- Game pricing and genre trends
- Regional behavior (where available)
- Cross-platform comparisons

## Project Structure
- `steam/`, `xbox/`, `playstation/`: Raw data & PySpark scripts
- `data/`: CSV files (local only, not on GitHub due to size)
- `report/`: Final report with insights and conclusions

## How to Run
Requires:
- Python 3.x
- PySpark

```bash
spark-submit Main_steam.py
spark-submit Main_xbox.py
spark-submit Main_playstation.py


Contributors

Alemu Nenko
Daniel Beltran

## Dataset Source  
We used the following dataset from Kaggle for our analysis:  
**[Gaming Profiles 2025 – Steam, PlayStation, Xbox](https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox)**  
