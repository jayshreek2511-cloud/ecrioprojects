# Mini Project 5 — Titanic Data Preprocessing & Grouping

Data preprocessing and transformation on the Titanic dataset using Pandas.

## Features
- Group by passenger class with average age and survival rate
- **Min-Max normalization** of Age column
- **Z-score normalization** of Age column
- Missing value handling (mean imputation)
- Gender encoding (`SexCode`: male=0, female=1)
- Age group classification (Child / Adult)
- **Pivot table** — survival rate by class and gender

## How to Run
```bash
pip install pandas
python Titanic.py
```

## Files
| File | Description |
|------|-------------|
| `Titanic.csv` | Original Titanic dataset |
| `Titanic.py` | Preprocessing script |
| `titanic_project5_output.csv` | Processed dataset (generated output) |

## Concepts Used
- Data normalization (Min-Max, Z-score)
- Feature encoding (categorical → numeric)
- Pivot tables
- Pandas `groupby` with `.agg()`
