class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i+1}. {task.description} - {status}")
