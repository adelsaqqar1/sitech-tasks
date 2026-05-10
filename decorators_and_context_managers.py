from time import time

 # Decorator to measure the time taken by a function
def timer(func): 
    def wrapper(*args, **kwargs):
        start_time = time()
        
        result = func(*args, **kwargs)  

        end_time = time()  

        print(f"Function running time is: {end_time - start_time} ")
        return result
    return wrapper


 # Apply the timer decorator
@timer 
def tistloop():
    for i in range(200):
        print(i)


print(tistloop())

 # Decorator to log function name and arguments
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments:")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        return func(*args, **kwargs)  
 
    return wrapper

# Class to represent a User
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

# Class to represent a Task
class Task:
    task_count = 0  

    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.status = "open"
        self.owner = owner
        Task.task_count += 1

# Function to assign a task owner
    @log_call 
    def assign(self, user):

        if user is None:
         print("Error: Cannot assign task to None.")
         return  

        self.owner = user

# Function to change the task status to "done"
    @log_call
    def complete(self):
        self.status = "done"

#Function to display task details
    @log_call
    def display(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Owner: {self.owner.name}")
        print("-" * 30)

#Comparing tasks by title.
    def __eq__(self, other):
        return self.title == other.title
#Returns a textual representation of the task with the title and status.
    def __str__(self):
        return f"{self.title} ({self.status})"


# Function to get incomplete tasks
def get_incomplete_tasks(tasks):
        return [task for task in tasks
          if task.status != "done"]


# Definition of Context Manager for measuring time using __enter__ and __exit__
class Timer:
    def __enter__(self):
        self.start_time = time.time()  
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  
        self.duration = self.end_time - self.start_time  
        print(f"Execution took {self.duration:.4f} seconds")



with Timer():

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


# Function to filter tasks by status or owner
    def filter_tasks(tasks, **kwargs):
        result = [] 

    
        for task in tasks:
        
            if "status" in kwargs and task.status != kwargs["status"]:
                continue  

            
            if "owner" in kwargs and task.owner != kwargs["owner"]:
                continue  

        
            result.append(task)

        return result  



    print("Filter by status='open':")
    filtered_by_status = filter_tasks([task1, task2, task3], status="open")
    for task in filtered_by_status:
        task.display()



    print("\nFilter by owner='Ahmad':")
    filtered_by_owner = filter_tasks([task1, task2, task3], owner=user2)
    for task in filtered_by_owner:
        task.display()



    print("\nFilter by status='open' and owner='Ahmad':")
    filtered_by_status_owner = filter_tasks([task1, task2, task3], status="open", owner=user2)
    for task in filtered_by_status_owner:
        task.display()



    task_dict = {task.title: task.status for task in tasks}

    print(task_dict) 