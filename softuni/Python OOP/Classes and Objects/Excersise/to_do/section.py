class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if not self.contains_task(new_task.name):
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, check_task):
        task_exist = self.contains_task(check_task)
        if task_exist:
            task_exist.completed = True
            return f"Completed task {check_task}"
        return f"Could not find task with the name {check_task}"

    def clean_section(self):
        counter = 0
        for x in self.tasks:
            if x.completed:
                self.tasks.remove(x)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        return f'Section {self.name}:\n' + '\n'.join([x.details() for x in self.tasks])

    def contains_task(self, task: str):
        for x in self.tasks:
            if x.name == task:
                return x
        return False
