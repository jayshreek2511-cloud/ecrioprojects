# Mini Project 5 — Titanic Data Preprocessing & Grouping

Data preprocessing and transformation on the Titanic dataset using Python (Pandas) and an interactive web simulator.

## Features
- Group by passenger class with average age and survival rate
- **Min-Max normalization** of Age column
- **Z-score normalization** of Age column
- Missing value handling (mean imputation)
- Gender encoding (`SexCode`: male=0, female=1)
- Age group classification (Child / Adult)
- **Pivot table** — survival rate by class and gender

### Web Interface (`index.html`)
- Dark **glassmorphism** design with vibrant neon accent highlights
- **Interactive Normalization Simulator** — input any custom age to calculate its Z-score and Min-Max value in real time using real Titanic dataset statistics
- Formatted tabular layouts for Grouped DataFrame outputs
- Interactive Multi-dimensional **Pivot Grid** visualizing survival rates

## How to Run

### CLI Version
```bash
pip install pandas
python Titanic.py
```

### Web Version
Open `index.html` in any browser — no server needed.

## Files
| File | Description |
|------|-------------|
| `Titanic.csv` | Original Titanic dataset |
| `Titanic.py` | Preprocessing script |
| `titanic_project5_output.csv` | Processed dataset (generated output) |
| `index.html` | Interactive preprocessing dashboard |

## Concepts Used
- Data normalization (Min-Max, Z-score formulas)
- Feature encoding & Pivot tables
- HTML5, CSS3 Grid layouts & transitions
- Real-time client-side calculation (JavaScript)
