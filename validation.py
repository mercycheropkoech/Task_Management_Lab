from datetime import datetime

def validate_task_title(title):
    """Validate the task title is not empty."""
    if not isinstance(title, str):
        return False
    if len(title.strip()) == 0:
        return False
    return True


def validate_task_description(description):
    """Validate the task description is not empty."""
    if not isinstance(description, str):
        return False
    if len(description.strip()) == 0:
        return False
    return True


def validate_due_date(due_date):
    """Validate the due date format is YYYY-MM-DD."""
    if not isinstance(due_date, str):
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False