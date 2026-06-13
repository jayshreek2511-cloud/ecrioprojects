from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# File for persistence
DATA_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


# Save tasks to file
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# In-memory task list (loaded from file)
tasks = load_tasks()


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        save_tasks()
    return redirect('/')


@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)