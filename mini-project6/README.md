# Mini Project 6 — Flask To-Do Web App

A web-based To-Do list application built with Flask.

## Features
- Add new tasks via a form
- Mark tasks as complete (client-side toggle)
- Delete tasks
- **Data persistence** — tasks are saved to `tasks.json` and restored on server restart
- Gradient UI with styled cards

## How to Run
```bash
pip install -r requirements.txt
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

## Files
| File | Description |
|------|-------------|
| `app.py` | Flask application (routes and logic) |
| `templates/index.html` | HTML template with embedded CSS and JS |
| `requirements.txt` | Python dependencies |

## Concepts Used
- Flask (routes, templates, form handling, redirects)
- Jinja2 templating
- HTML/CSS (gradients, flexbox, hover effects)
- JavaScript (DOM manipulation)
- File I/O (JSON persistence)
