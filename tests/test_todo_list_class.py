from lib.TodoList import *
from lib.Todo import *

"""
Given a todo list is created

The todos property should be an empty list
"""
def test_todo_list_no_tasks_added():
    todoList = TodoList()
    
    assert todoList.todos == []

"""
Given a todo list with one todo added

The todos property should only contain that todo
"""
def test_todo_list_single_todo_added():
    todoList = TodoList()
    todo = Todo("Vacuum room")

    todoList.addTodo(todo)

    assert todoList.todos == [todo]

"""
Given a todo list with the same todo added twice

The todos property should only contain that todo once
"""
def test_todo_list_same_todo_instance_added_does_not_add_duplicate():
    todoList = TodoList()
    todo = Todo("Go to the gym")
    
    todoList.addTodo(todo)
    todoList.addTodo(todo)

    assert todoList.todos == [todo]

"""
Given a todo list with three different todos added

The todos property should contain those three todos (order doesn't matter)
"""
def test_todo_list_multiple_tasks_added():
    todoList = TodoList()

    todo1 = Todo("Prepare for meeting")
    todo2 = Todo("Go gym")
    todo3 = Todo("Sketch character design")

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    # Shouldn't assume the tasks added will be stored in the same order, 
    # any ordering of the tasks should be acceptable so sort to ignore

    expectedTodos = [todo2, todo1, todo3]

    assert expectedTodos == sorted(todoList.todos, key=lambda todo:todo.task)
    
"""
Given a todo list with three different todos, each being added again multiple times

The todos property should contain those three todos (order doesn't matter)
"""
def test_todo_list_multiple_tasks_added_with_duplicates():
    todoList = TodoList()

    todo1 = Todo("Work on side project")
    todo2 = Todo("Read 20 pages of book")
    todo3 = Todo("Do grocery shopping")
    
    todoList.addTodo(todo1)
    todoList.addTodo(todo1)

    todoList.addTodo(todo2)
    todoList.addTodo(todo2)
    todoList.addTodo(todo2)
    todoList.addTodo(todo2)

    todoList.addTodo(todo3)
    todoList.addTodo(todo3)
    todoList.addTodo(todo3)

    # Shouldn't assume the tasks added will be stored in the same order, 
    # any ordering of the tasks should be acceptable so sort to ignore

    expectedTodos = [todo3, todo2, todo1]

    assert expectedTodos == sorted(todoList.todos, key=lambda todo:todo.task)

"""
Given a todo list is created

Calling getCompleteTodos should give an empty list
"""
def test_todo_list_all_completed_gives_empty_completed_list_for_no_tasks():
    todoList = TodoList()

    assert todoList.getCompleteTodos() == []

"""
Given a todo list is created

Calling getIncompleteTodos should give an empty list
"""
def test_todo_list_all_incomplete_gives_empty_incomplete_list_for_no_tasks():
    todoList = TodoList()

    assert todoList.getIncompleteTodos() == []

"""
Given a todo list is created and three todos are added, each being mark complete

Calling getCompleteTodos should give a list of all three todos (order doesn't matter)
"""
def test_todo_list_all_completed_gives_all_tasks_for_only_completed_tasks():
    todoList = TodoList()

    todo1 = Todo("Task 1")
    todo1.markComplete()

    todo2 = Todo("Task 2")
    todo2.markComplete()

    todo3 = Todo("Task 3")
    todo3.markComplete()

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    # Shouldn't assume the tasks added will be stored in the same order, 
    # any ordering of the tasks should be acceptable so sort to ignore

    expectedTodos = [todo1, todo2, todo3]

    assert expectedTodos == (sorted(todoList.getCompleteTodos(), 
                                    key=lambda todo:todo.task))
    

"""
Given a todo list is created and three todos are added, none marked complete

Calling getIncompleteTodos should give a list of all three todos (order doesn't matter)
"""
def test_todo_list_all_incomplete_gives_all_tasks_for_only_incomplete_tasks():
    todoList = TodoList()

    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo3 = Todo("Task 3")

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    # Shouldn't assume the tasks added will be stored in the same order, 
    # any ordering of the tasks should be acceptable so sort to ignore

    expectedTodos = [todo1, todo2, todo3]

    assert expectedTodos == (sorted(todoList.getIncompleteTodos(), 
                                    key=lambda todo:todo.task))

"""
Given a todo list with three todos added, with the last two being marked complete

Calling getCompleteTodos should give a list of the last two todos (order doesn't matter)
"""
def test_todo_list_all_completed_gives_only_completed_for_mixed_status_tasks():
    todoList = TodoList()

    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo3 = Todo("Task 3")

    todo2.markComplete()
    todo3.markComplete()

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    # Shouldn't assume the tasks added will be stored in the same order, 
    # any ordering of the tasks should be acceptable so sort to ignore

    expectedTodos = [todo2, todo3]

    assert expectedTodos == (sorted(todoList.getCompleteTodos(), 
                                    key=lambda todo:todo.task))


"""
Given a todo list with three todos added, with the last two being marked complete

Calling getIncompleteTodos should give a list of the first todo
"""
def test_todo_list_all_incomplete_gives_only_incomplete_for_mixed_status_tasks():
    todoList = TodoList()

    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo3 = Todo("Task 3")

    todo2.markComplete()
    todo3.markComplete()

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    expectedTodos = [todo1]

    assert expectedTodos == todoList.getIncompleteTodos()


"""
Given a todo list with three todos added and markAllTodosAsComplete called

The complete status of all three todos should be True
"""
def test_todo_list_mark_all_complete_marks_all_complete():
    todoList = TodoList()

    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo3 = Todo("Task 3")

    todoList.addTodo(todo1)
    todoList.addTodo(todo2)
    todoList.addTodo(todo3)

    todoList.markAllTodosAsComplete()

    assert todo1.complete == True
    assert todo2.complete == True
    assert todo3.complete == True


