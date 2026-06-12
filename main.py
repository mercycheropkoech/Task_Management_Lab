try:
    from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ModuleNotFoundError:
    from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
    from validation import validate_task_title, validate_task_description, validate_due_date

def main():
    tasks = []

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            if not validate_task_title(title):
                print("Title cannot be empty")
                continue

            description = input("Enter task description: ")
            if not validate_task_description(description):
                print("Description cannot be empty")
                continue

            due_date = input("Enter due date (YYYY-MM-DD): ")
            if not validate_due_date(due_date):
                print("Invalid due date format or date is in the past")
                continue

            task = add_task(title, description, due_date)
            if task is not None:
                tasks.append(task)

        elif choice == "2":
            if not tasks:
                print("No tasks to mark complete")
                continue
            view_pending_tasks(tasks)
            index = input("Enter task number to mark complete: ")
            mark_task_as_complete(index, tasks)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            if not tasks:
                print("No tasks yet!")
            else:
                progress = calculate_progress(tasks)
                print(progress)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()