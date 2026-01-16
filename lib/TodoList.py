# File: lib/TodoList.py

from lib.Todo import *

class TodoList:
    # Public Properties:
    #   todos: a list of Todo objects 

    def __init__(self):
        self.todos = []

    def addTodo(self, todo):
        # Parameters:
        #   todo: an instance of Todo

        # Side-effects:
        #   Adds the todo to the list of Todo objects
        
        if todo in self.todos:
            return

        self.todos.append(todo)

    def getIncompleteTodos(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        
        return list(filter(lambda todoObject: not todoObject.complete, self.todos))

    def getCompleteTodos(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        
        return list(filter(lambda todoObject: todoObject.complete, self.todos))

    def markAllTodosAsComplete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        
        for todoObject in self.todos:
            todoObject.markComplete()

    