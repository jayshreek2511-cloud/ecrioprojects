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

### Flask Version (Terminal / Localhost)
```bash
pip install -r requirements.txt
python app.py
```
Then navigate to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### Standalone Web Version (Localhost)
Start a local HTTP server from the root projects directory:
```bash
python -m http.server 8080
```
Then navigate to:
**[http://localhost:8080/mini-project6/templates/index.html](http://localhost:8080/mini-project6/templates/index.html)**

*Alternatively, you can open `templates/index.html` directly in any web browser.*

## Files
| File | Description |
|------|-------------|
| `app.py` | Flask application (routes, JSON persistence) |
| `templates/index.html` | Modern web UI with glassmorphism design |
| `requirements.txt` | Python dependencies (`flask`) |
| `README.md` | Documentation |

## Concepts Used
- Flask (routes, Jinja2 templates, form handling, redirects)
- File I/O (JSON persistence for Flask backend)
- HTML5, CSS3 (glassmorphism, gradients, progress bar, animations)
- JavaScript (localStorage, DOM manipulation, filter logic, animations)
