# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TodoList:
    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   None
        pass # No code here yet

    def addTask(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   True/False based on whether task successfully added
        # Side-effects:
        #   Saves the task in memory
        pass # No code here yet

    def listTasks(self):
        # Parameters:
        #   None
        # Returns:
        #   List of tasks
        # Side-effects:
        #   Nothing
        pass

    def markTaskAsComplete(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   True/False based on whether task successfully marked as complete
        # Side-effects:
        #   Deletes task from memory if it exists
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a task is added
The listTasks should give list with only that element and addTask should return True
"""

todoList = TodoList()
todoList.addTask("Go for walk") => True
todoList.listTasks() => ["Go for walk"]


"""
Given a task is added and added again
The listTasks should only contain the task once and the addTask should return False
"""

todoList = TodoList()
todoList.addTask("Clean dog")
todoList.addTask("Clean dog") => False
todoList.listTasks() => ["Clean dog"]


"""
Given no tasks are added
Calling listTasks should return an empty list
"""

todoList = TodoList()
todoList.listTasks() => []



"""
Given the following tasks are added: "Go gym", "Prepare for meeting" and "Sketch character design"
Calling listTasks should return any permutation of ["Go gym", "Prepare for meeting", "Sketch character design"]
"""

todoList = TodoList()
todoList.addTask("Go gym")
todoList.addTask("Prepare for meeting")
todoList.addTask("Sketch character design")

# Or any permutation
todoList.listTasks() => ["Go gym", "Prepare for meeting", "Sketch character design"]

"""
Given the following tasks are added: "Go gym", "Go gym" and "Sketch character"
Calling listTasks should return any permutation of ["Go gym", "Sketch character"]
"""

todoList = TodoList()
todoList.addTask("Go gym")
todoList.addTask("Go gym")
todoList.addTask("Sketch character")

# Or any permutation
todoList.listTasks() == ["Go gym", "Sketch character"]


"""
Given a task is added 
Calling markTaskAsComplete for a different task should return False and the list
should be any permutation of the list before the call
"""

todoList = TodoList()
todoList.addTask("Clean dishes")

listBefore = todoList.listTasks()

todoList.markTaskAsComplete("Walk dog") => False
todoList.listTasks() == listBefore # Or any permutation


"""
Given the following tasks added: "Task one", "Task two", "Task three", "Task four", 
"Task five"
Calling markTaskAsComplete for "Task one", "Task four" and "Task eight" and 
then calling listTasks should give any permutation of ["Task two", "Task three", 
"Task five"]
"""

todoList = TodoList()
todoList.addTask("Task one")
todoList.addTask("Task two")
todoList.addTask("Task three")
todoList.addTask("Task four")
todoList.addTask("Task five")

todoList.markTaskAsComplete("Task one") => True
todoList.markTaskAsComplete("Task four") => True
todoList.markTaskAsComplete("Task eight")

# Or any permutation
todoList.listTasks() => ["Task two", "Task three", "Task five"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
from lib.todo import *

def test_todo_add_one_task():
    todoList = TodoList()
    assert todoList.addTask("Go for walk") == True
    assert todoList.listTasks() == ["Go for walk"]

def test_todo_same_task_added():
    todoList = TodoList()
    todoList.addTask("Clean dog")
    
    assert todoList.addTask("Clean dog") == False
    assert todoList.listTasks() == ["Clean dog"]


def test_todo_no_tasks_added():
    todoList = TodoList()
    
    assert todoList.listTasks() == []

def test_todo_multiple_tasks_added():
    todoList = TodoList()

    todoList.addTask("Go gym")
    todoList.addTask("Prepare for meeting")
    todoList.addTask("Sketch character design")

    assert (sorted(todoList.listTasks()) == sorted(["Go gym", "Prepare for meeting", 
                                             "Sketch character design"]))


def test_todo_multiple_tasks_added_with_duplicates():
    todoList = TodoList()

    todoList.addTask("Go gym")
    todoList.addTask("Go gym")
    todoList.addTask("Sketch character")

    assert sorted(todoList.listTasks()) == sorted(["Go gym", "Sketch character"])


def test_todo_task_added_but_fake_task_marked_complete():
    todoList = TodoList()
    todoList.addTask("Clean dishes")

    listBefore = todoList.listTasks()

    assert todoList.markTaskAsComplete("Walk dog") == False
    assert sorted(todoList.listTasks()) == sorted(listBefore)


def test_todo_multiple_tasks_added_both_valid_and_invalid_completions():
    todoList = TodoList()

    todoList.addTask("Task one")
    todoList.addTask("Task two")
    todoList.addTask("Task three")
    todoList.addTask("Task four")
    todoList.addTask("Task five")

    assert todoList.markTaskAsComplete("Task one") == True
    assert todoList.markTaskAsComplete("Task four") == True
    todoList.markTaskAsComplete("Task eight")

    assert (sorted(todoList.listTasks()) == 
            sorted(["Task two", "Task three", "Task five"]))


```
