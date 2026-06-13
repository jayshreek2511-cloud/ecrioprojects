# Mini Project 1 — Smart Calculator

A calculator application built with Python (CLI) and a beautiful web interface.

## Features
- Addition, Subtraction, Multiplication, Division
- Division-by-zero handling
- Input validation for non-numeric values

### Web Interface (`index.html`)
- Dark **glassmorphism** design with animated gradient background
- Full **keyboard support** (type numbers, operators, Enter, Escape, Backspace)
- **History panel** showing past calculations — click any to reuse the result
- Smooth micro-animations on button press and results
- Percentage and sign toggle (±) functions

## How to Run

### CLI Version (Terminal)
```bash
python calculator.py
```

### Web Version (Localhost)
Start a local HTTP server from the root projects directory:
```bash
python -m http.server 8080
```
Then navigate to:
**[http://localhost:8080/mini-project1/index.html](http://localhost:8080/mini-project1/index.html)**

*Alternatively, you can open `index.html` directly in any web browser.*

## Files
| File | Description |
|------|-------------|
| `calculator.py` | CLI calculator (menu-driven) |
| `index.html` | Web-based calculator with modern UI |
| `README.md` | Documentation |

## Concepts Used
- Functions, control flow, loops, exception handling (Python)
- HTML5, CSS3 (glassmorphism, gradients, animations)
- JavaScript (DOM manipulation, keyboard events, state management)
