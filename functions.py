def getTodos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos

def writeTodos(todo):
    with open('todos.txt', 'w') as file:
        file.writelines(todo)



