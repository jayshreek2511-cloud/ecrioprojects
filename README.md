# ✨ Ecrio Mini-Projects Portfolio

Welcome to the **Ecrio Projects Portfolio**! This repository compiles and modernizes six high-quality, professional mini-projects covering Python CLI tools, Web App development, Data Preprocessing/Analysis (Pandas & Chart.js), and IoT Communication (MQTT). 

Each project has been enhanced with **premium dark glassmorphism web interfaces**, robust **data persistence** (JSON & localStorage), and modern clean code standards.

---

## 📂 Repository Structure

```text
ecrio-projects/
├── README.md                  # Main entry point (this file)
├── mini-project1/             # Smart Calculator (Python & Web UI)
│   ├── calculator.py          # Python CLI
│   ├── index.html             # Glassmorphic Calculator Web UI
│   └── README.md              # Project Docs
├── mini-project2/             # Finance Transaction Tracker (Python & Web UI)
│   ├── transactions.py        # Python CLI (JSON persistent)
│   ├── index.html             # Transaction Dashboard Web UI
│   ├── transactions.json      # Persistent CLI transactions
│   └── README.md              # Project Docs
├── mini-project3/             # Titanic Data Analytics (Pandas & Chart.js)
│   ├── titanic.py             # Data Analysis Script
│   ├── index.html             # Interactive Charts Dashboard
│   └── README.md              # Project Docs
├── mini-project5/             # Titanic Preprocessing & Normalization (Pandas & Simulator)
│   ├── Titanic.py             # DataFrame Processing Script
│   ├── index.html             # Interactive Normalization & Insights Web UI
│   └── README.md              # Project Docs
├── mini-project6/             # Flask To-Do Web App (Flask & Web UI)
│   ├── app.py                 # Flask server (JSON persistent)
│   ├── requirements.txt       # Flask dependencies
│   ├── templates/
│   │   └── index.html         # Premium To-Do interface
│   └── README.md              # Project Docs
└── mini-project7/             # MQTT Pub/Sub IoT Console (Paho MQTT & Web UI)
    ├── publisher.py           # Publisher Client script
    ├── subscriber.py          # Subscriber Client script
    ├── requirements.txt       # Paho dependencies
    ├── index.html             # Live Web MQTT Publisher/Subscriber Console
    └── README.md              # Project Docs
```

---

## 🚀 How to Run the Web Dashboard Locally

You can serve and run all web projects simultaneously using a single local server:

1. **Start the local HTTP server** from the root folder:
   ```bash
   python -m http.server 8080
   ```
2. **Access the projects in your browser:**
   * **Project 1 (Calculator):** [http://localhost:8080/mini-project1/index.html](http://localhost:8080/mini-project1/index.html)
   * **Project 2 (Finance Tracker):** [http://localhost:8080/mini-project2/index.html](http://localhost:8080/mini-project2/index.html)
   * **Project 3 (Titanic Charts):** [http://localhost:8080/mini-project3/index.html](http://localhost:8080/mini-project3/index.html)
   * **Project 5 (Normalization Tool):** [http://localhost:8080/mini-project5/index.html](http://localhost:8080/mini-project5/index.html)
   * **Project 6 (To-Do App - HTML Version):** [http://localhost:8080/mini-project6/templates/index.html](http://localhost:8080/mini-project6/templates/index.html)
   * **Project 7 (MQTT Dashboard):** [http://localhost:8080/mini-project7/index.html](http://localhost:8080/mini-project7/index.html)

---

## 🛠️ Project Summaries & Features

### 🧮 Mini-Project 1: Smart Calculator
* **CLI:** Menu-driven terminal calculator with error-handling (division by zero, validation).
* **Web UI:** Dark glassmorphism layout, **animated gradient background**, **full keyboard support** (numbers, operators, Enter/Esc), and an **interactive history panel** (click to reuse past values).
* **Location:** `mini-project1/`

### 💰 Mini-Project 2: Finance Transaction Tracker
* **CLI:** Command-line OOP transaction tracker featuring file-based **JSON persistence** (`transactions.json`) and activity logging.
* **Web UI:** Three live **summary cards** (Income, Expense, Balance) with micro-animations, emoji category picker (Salary 💼, Food 🍕, etc.), and **localStorage persistence**.
* **Location:** `mini-project2/`

### 📊 Mini-Project 3: Titanic Data Analysis
* **CLI:** Pandas script cleaning the Titanic passenger dataset and exporting cleaned data.
* **Web UI:** Analytical dashboard leveraging **Chart.js** to display survival rate by gender, average age per class (Doughnut), and survival age comparison.
* **Location:** `mini-project3/`

### ⚙️ Mini-Project 5: Titanic Preprocessing & Normalization
* **CLI:** Advanced preprocessing pipeline (imputation, mapping, pivot tables, Min-Max, and Z-score transforms).
* **Web UI:** **Interactive Normalization Simulator** that scales custom ages and dynamically retrieves passenger class statistics (age comparisons, gendered survival rates) based on selection.
* **Location:** `mini-project5/`

### 📝 Mini-Project 6: Flask To-Do App
* **Server:** Flask backend preserving user tasks inside `tasks.json` across server resets.
* **Web UI:** Dashboard tracking **Total / Pending / Done counters**, an **animated completion progress bar**, filter pills (All / Pending / Completed), and slide-out delete animations.
* **Location:** `mini-project6/`

### 📡 Mini-Project 7: MQTT Pub/Sub Communication
* **CLI:** Concurrent MQTT publisher (sending random values) and subscriber nodes connected to a public broker.
* **Web UI:** **Live Web Client Console** using Paho MQTT JS over WebSockets. Allows users to connect, subscribe to custom topics, publish test messages, and monitor live traffic with a colored console log.
* **Location:** `mini-project7/`

---

## 👥 Repository & Author Information
* **Git Repository:** [https://github.com/jayshreek2511-cloud/ecrioprojects.git](https://github.com/jayshreek2511-cloud/ecrioprojects.git)
* **Branch:** `main`
* **Author:** Jayshree
