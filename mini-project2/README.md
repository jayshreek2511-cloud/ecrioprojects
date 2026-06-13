# Mini Project 2 — Finance Tracker

A personal finance tracker built with Python (CLI) and a beautiful web interface.

## Features
- Add Income and Expense entries
- View all transactions
- Summary with total income, total expense, and balance
- **Data persistence** — transactions are saved and restored on restart
- Logging to `transactions.log`

### Web Interface (`index.html`)
- Dark **glassmorphism** theme with animated floating orbs
- **3 summary cards** — Total Income, Total Expense, Balance (with hover animations)
- **Category picker** with emojis (💼 Salary, 🍕 Food, 🛍️ Shopping, etc.)
- Income/Expense **toggle switch** and **filter pills**
- Delete transactions on hover with 🗑 button
- **localStorage persistence** — data survives page refresh

## How to Run

### CLI Version
```bash
python transactions.py
```

### Web Version
Open `index.html` in any browser — no server needed.

## Files
| File | Description |
|------|-------------|
| `transactions.py` | CLI finance tracker with OOP |
| `index.html` | Web-based finance tracker with modern UI |
| `transactions.log` | Log file for CLI transactions |

## Concepts Used
- Object-Oriented Programming (classes, inheritance) — Python
- File I/O (JSON persistence), Logging module — Python
- HTML5, CSS3 (glassmorphism, gradients, animations) — Web
- JavaScript (localStorage, DOM manipulation, state management) — Web
