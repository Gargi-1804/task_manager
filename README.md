# task_manager
# Task Manager – Python CLI App

A simple command-line task manager I built in Python. It lets you create, view, update, delete, and search tasks — and everything gets saved to a file so your data sticks around between sessions.

---

## What it does

- Add new tasks with a title and description
- View all your current tasks
- Update any task (title, description, or status)
- Delete tasks you no longer need
- Search tasks by keyword
- Mark tasks as completed
- Auto-saves everything to `tasks.txt` so nothing gets lost when you close the app

---

## How to run it

Make sure you have Python installed (3.x should work fine), then just run:

```bash
python task_manager.py
```

No external libraries needed — it uses only built-in Python stuff.

---

## Usage

When you run the app, you'll see a menu like this:

```
--- Task Manager ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Search Task
6. Mark Task Completed
7. Exit
```

Just enter the number for whatever you want to do and follow the prompts. Pretty straightforward.

---

## File storage

Tasks are saved in a file called `tasks.txt` in the same folder as the script. Each task is stored on its own line in this format:

```
id|title|description|status
```

The file gets created automatically on first run, so you don't need to set anything up manually.

---

## Project structure

```
task_manager.py   # main script with all the logic
tasks.txt         # auto-generated file where tasks are stored
```

---

## Future ideas

A few things I'd like to add eventually:

- Due dates for tasks
- Priority levels (High / Medium / Low)
- Filter tasks by status
- A proper database instead of a flat text file

---

## Requirements

- Python 3.x
- That's it

---

Feel free to fork it, mess around with it, or suggest improvements!
