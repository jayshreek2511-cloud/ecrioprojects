# Mini Project 6 — To-Do Web App

A web-based To-Do list application built with Flask and a stunning modern UI.

## Features
- Add, complete, and delete tasks
- **Stats dashboard** — Total, Pending, and Done counters
- **Animated progress bar** showing completion percentage
- **Filter tabs** — All, Pending, Completed
- **Data persistence** — tasks saved to `tasks.json` (Flask) and localStorage (web)
- Custom **checkbox animations** with slide-out delete effect
- Dark **glassmorphism** theme with pulsing gradient background

## How to Run

### Flask Version (with backend)
```bash
pip install -r requirements.txt
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

### Standalone Web Version
Open `templates/index.html` directly in any browser — works without Flask using localStorage.

## Files
| File | Description |
|------|-------------|
| `app.py` | Flask application (routes, JSON persistence) |
| `templates/index.html` | Modern web UI with glassmorphism design |
| `requirements.txt` | Python dependencies (`flask`) |

## Concepts Used
- Flask (routes, Jinja2 templates, form handling, redirects)
- File I/O (JSON persistence for Flask backend)
- HTML5, CSS3 (glassmorphism, gradients, progress bar, animations)
- JavaScript (localStorage, DOM manipulation, filter logic, animations)
