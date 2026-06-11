from datetime import datetime

from task_manager.validation import (
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
        return msg1

    if not valid_desc:
        return msg2

    if not valid_date:
        return msg3

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "pending"
    }

    tasks.append(task)
    return "Task added successfully!"


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        return "Invalid task index"

    tasks[index]["status"] = "completed"
    return "Task marked as complete!"


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if t["status"] == "pending"]

    if len(pending) == 0:
        return []

    return pending


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = len([t for t in tasks if t["status"] == "completed"])
    return (completed / len(tasks)) * 100