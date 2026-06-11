from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Invalid title"

    title = title.strip()

    if len(title) == 0:
        return False, "Title cannot be empty"

    if len(title) < 3:
        return False, "Title must be at least 3 characters"

    return True, "Valid"


def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Invalid description"

    description = description.strip()

    if len(description) == 0:
        return False, "Description cannot be empty"

    if len(description) < 5:
        return False, "Description must be at least 5 characters"

    return True, "Valid"


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, "Valid"
    except ValueError:
        return False, "Invalid date format"