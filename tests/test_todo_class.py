from lib.Todo import *
import pytest

"""
Given a todo is created with a blank task name

Exception should be thrown
"""
def test_todo_does_not_allow_empty_task_name():
    with pytest.raises(Exception) as exception:
        Todo("")
    
    assert str(exception.value) == "Task name cannot be empty"


"""
Given a todo is created

The complete property of the todo object should be False
"""
def test_todo_correctly_stores_task_name_with_complete_set_to_false():
    todo = Todo("Go for walk")
    assert todo.task == "Go for walk"
    assert todo.complete == False


"""
Given a todo is created and the markComplete is called

The complete property of the todo should be True
"""
def test_todo_marks_incomplete_task_as_complete():
    todo = Todo("Complete Golden Squares Unit 5")
    todo.markComplete()

    assert todo.complete == True

"""
Given a todo is created and markComplete is called twice

The complete property after the first call and after the second call 
should be the same (i.e. nothing should change)
"""
def test_todo_does_nothing_when_marking_a_complete_task_as_complete():
    todo = Todo("Clean dishes")
    todo.markComplete()
    taskCompletedBefore = todo.complete
    todo.markComplete()
    taskCompletedAfter = todo.complete

    assert taskCompletedBefore == taskCompletedAfter



