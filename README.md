# Netflix Content Analytics & Content-Based Recommendation System

A data analytics and recommendation project exploring Netflix titles using Python, MySQL, and Power BI. The project cleans and analyzes the Netflix titles dataset, visualizes content trends, and generates content-based recommendations using TF-IDF and cosine similarity.

## Features
- Data cleaning and handling of missing or duplicate records
- Movies vs. TV Shows comparison
- Analysis of release years, countries, and genres
- Data visualizations for content trends and ratings
- Content-based recommendation system using TF-IDF and cosine similarity
- MySQL import workflow
- Power BI dashboard

## Tools & Technologies
- Python: Pandas, NumPy, Matplotlib, Seaborn, scikit-learn
- MySQL
- Power BI

## Repository Structure
```text
.
├── data/
│   ├── raw/          # Source dataset
│   └── processed/    # Cleaned dataset, recommendations, charts
├── MySQL/            # MySQL export files
├── powerbi/          # Power BI dashboard
└── python/           # Python scripts for cleaning, analysis, visuals, recommendations
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Netflix-Content-Analytics-Recommendation-System.git
   cd Netflix-Content-Analytics-Recommendation-System
   ```
2. Install Python dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn mysql-connector-python
   ```
3. Run the scripts from the `python` directory so their relative file paths resolve:
   ```bash
   cd python
   python 01_data_cleaning.py
   python 02_data_analysis.py
   python 03_content_trends.py
   python 05_data_visualization.py
   python 06_recommendation_system.py
   ```
   `04_import_to_mysql.py` is optional and requires a configured MySQL database.
4. Open `powerbi/Netflix_Dashboard.pbix` in Power BI Desktop to view the dashboard.

## Recommendation Approach
The recommender combines genre metadata (weighted more heavily) with title descriptions and content type, transforms the text with TF-IDF, and ranks titles by cosine similarity.

## Data
The project includes a Netflix titles CSV in `data/raw/` and cleaned/output CSV files in `data/processed/`. Check dataset provenance and licensing before redistributing.

## Author
**Kavi Keerthana R**

---
*Data Analytics · Python · SQL · Power BI · Recommendation Systems*
