try:
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ModuleNotFoundError:
    from validation import validate_task_title, validate_task_description, validate_due_date

def add_task(title, description, due_date):
    """Create a validated task dictionary."""
    if not validate_task_title(title):
        print("Task title is required.")
        return None
    if not validate_task_description(description):
        print("Task description is required.")
        return None
    if not validate_due_date(due_date):
        print("Task due date must be in YYYY-MM-DD format.")
        return None

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    print("Task added successfully!")
    return task


def mark_task_as_complete(selection, tasks):
    """Mark a pending task as complete by its displayed number."""
    try:
        selection = int(selection)
    except ValueError:
        print("Please enter a valid number")
        return False

    pending_indices = [i for i, task in enumerate(tasks) if not task["completed"]]
    if 1 <= selection <= len(pending_indices):
        task_index = pending_indices[selection - 1]
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
        return True

    print("Invalid task number")
    return False


def view_pending_tasks(tasks):
    """Display all pending tasks."""
    pending_indices = [i for i, task in enumerate(tasks) if not task["completed"]]
    if not pending_indices:
        print("No pending tasks!")
        return pending_indices

    for number, task_index in enumerate(pending_indices, start=1):
        task = tasks[task_index]
        print(f"{number}. {task['title']} | Due: {task['due_date']}")
        if task["description"]:
            print(f"  {task['description']}")
    return pending_indices


def calculate_progress(tasks):
    """Calculate and return the completed task progress as a float."""
    if not tasks:
        return 0.0
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    return (completed / total) * 100.0