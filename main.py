from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

while True:
    choice = input()

    if choice == "1":
        title = input()
        description = input()
        due_date = input()
        add_task(title, description, due_date)

    elif choice == "2":
        index = int(input())
        mark_task_as_complete(index)

    elif choice == "3":
        view_pending_tasks()

    elif choice == "4":
        calculate_progress()

    elif choice == "5":
        break