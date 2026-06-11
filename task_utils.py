from datetime import datetime

# Import validation functions
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)
tasks = []

def add_task(title, description, due_date):
    valid_title, msg1 = validate_task_title(title)
    valid_desc, msg2 = validate_task_description(description)
    valid_date, msg3 = validate_due_date(due_date)

    if not valid_title:
        print(msg1)
        return

    if not valid_desc:
        print(msg2)
        return

    if not valid_date:
        print(msg3)
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "pending"
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index")
        return

    tasks[index]["status"] = "completed"
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if t["status"] == "pending"]

    if len(pending) == 0:
        print("No pending tasks")
        return

    for i, task in enumerate(pending):
        print(f"{i}. {task['title']} - {task['due_date']}")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = len([t for t in tasks if t["status"] == "completed"])
    progress = (completed / len(tasks)) * 100
    return progress