# File: lib/Todo.py

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property if non-empty, otherwise throws Exception
        #   Sets the complete property to False

        if task == "":
            raise Exception("Task name cannot be empty")
        
        self.task = task
        self.complete = False
    
    def markComplete(self):
        # Side-effects:
        #   Sets the complete property to True

        self.complete = True

