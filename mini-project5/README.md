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
- **Interactive Normalization & Class Insights Tool** — input a custom age and select a passenger class (1st, 2nd, or 3rd) to:
  - Calculate Min-Max and Z-score normalized values in real time.
  - Compare the input age to the class average (highlighting age differences).
  - Show the class overall survival rate.
  - View gender-specific survival rates for the selected class.
- Formatted tabular layouts for Grouped DataFrame outputs
- Interactive Multi-dimensional **Pivot Grid** visualizing survival rates

## How to Run

### CLI Version (Terminal)
```bash
pip install pandas
python Titanic.py
```

### Web Version (Localhost)
Start a local HTTP server from the root projects directory:
```bash
python -m http.server 8080
```
Then navigate to:
**[http://localhost:8080/mini-project5/index.html](http://localhost:8080/mini-project5/index.html)**

*Alternatively, you can open `index.html` directly in any web browser.*

## Files
| File | Description |
|------|-------------|
| `Titanic.csv` | Original Titanic dataset |
| `Titanic.py` | Preprocessing script |
| `titanic_project5_output.csv` | Processed dataset (generated output) |
| `index.html` | Interactive preprocessing dashboard |
| `README.md` | Documentation |

## Concepts Used
- Data normalization (Min-Max, Z-score formulas)
- Feature encoding & Pivot tables
- HTML5, CSS3 Grid layouts & transitions
- Real-time client-side calculation (JavaScript)
