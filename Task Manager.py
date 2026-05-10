# Class to represent a User
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

# Class to represent a Task
class Task:
    task_count = 0  
 # Initialize the Task with title, description, and owner
    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.status = "open"
        self.owner = owner
        Task.task_count += 1

 # Assign a new user as the owner of the task
    def assign(self, user):
        self.owner = user

# Mark the task as completed by changing its status to "done"
    def complete(self):
        self.status = "done"

  # Display the task details: title, description, status, and owner
    def display(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Owner: {self.owner.name}")
        print("-" * 30)

  # Compare two tasks by their title to check if they are the same
    def __eq__(self, other):
        return self.title == other.title

 # Return a string representation of the task with title and status
    def __str__(self):
        return f"{self.title} ({self.status})"


# Function to get the tasks that are not completed (status is not "done")
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





