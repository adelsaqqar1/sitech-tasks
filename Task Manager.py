class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"


class Task:
    task_count = 0  

    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.status = "open"
        self.owner = owner
        Task.task_count += 1

    def assign(self, user):
        self.owner = user

    def complete(self):
        self.status = "done"

    def display(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Owner: {self.owner.name}")
        print("-" * 30)

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f"{self.title} ({self.status})"



def get_incomplete_tasks(tasks):
    return [task for task in tasks
             if task.status != "done"]




user1 = User("Adel")
user2 = User("Ahmad")


task1 = Task("Study", "Finish OOP", user1)
task2 = Task("Gym", "Workout session", user1)
task3 = Task("Project", "Build API", user2)


task1.display()

task1.complete()
task1.display()

task2.assign(user2)
task2.display()


tasks = [task1, task2, task3]


incomplete = get_incomplete_tasks(tasks)

print("Incomplete Tasks:")
for task in incomplete:
    print(task)


print("\nTotal Tasks Created:", Task.task_count)