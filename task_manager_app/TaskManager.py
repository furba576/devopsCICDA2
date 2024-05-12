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
            raise IndexError("Invalid task index.")


    def list_tasks(self):
        task_list = ""
        if not self.tasks:
            task_list += "No tasks."
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Not Completed"
                task_list += f"{i}. {task.description} - {status}\n"
        return task_list
