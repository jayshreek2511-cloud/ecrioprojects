# Mini Project 3 — Titanic Data Analysis

Exploratory data analysis on the Titanic dataset using Python (Pandas) and a beautiful web dashboard.

## Features
- Survival count and percentage
- Average age per passenger class
- Gender distribution per class
- Female survival percentage
- Survival rate by gender
- Median age by gender
- Average age of survivors vs non-survivors
- Analysis of passengers above age 40
- Age group classification (Child / Adult / Senior)
- Average fare for 1st class survivors
- Data cleaning (missing value imputation) and export

### Web Interface (`index.html`)
- Dark **glassmorphism** design with custom colors and fonts
- Interactive **bar and doughnut charts** powered by **Chart.js**
- Key metrics KPI grid
- Summary data table for Gender Count per Class
- Dynamic animations on load and interactions

## How to Run

### CLI Version (Terminal)
```bash
pip install pandas
python titanic.py
```

### Web Version (Localhost)
Start a local HTTP server from the root projects directory:
```bash
python -m http.server 8080
```
Then navigate to:
**[http://localhost:8080/mini-project3/index.html](http://localhost:8080/mini-project3/index.html)**

*Alternatively, you can open `index.html` directly in any web browser.*

## Files
| File | Description |
|------|-------------|
| `titanic.csv` | Original Titanic dataset |
| `titanic.py` | Analysis script |
| `titanic_cleaned.csv` | Cleaned dataset (generated output) |
| `index.html` | Interactive data analytics dashboard |
| `README.md` | Documentation |

## Concepts Used
- Pandas (`groupby`, `apply`, `fillna`, filtering) — Python
- HTML5, CSS3 (Flexbox, Grid, custom styling) — Web
- Chart.js (Data visualizations, custom legends, animations) — Web
