todos = []
user_action = input('Enter the word: add or show: ')
match user_action:
    case 'add':
        print('To finish press x ')
        todo = ''
        while todo != 'x':
            todo = input('Enter a todo: ')

            1
            todos.append(todo.capitalize() + '\n')
        file = open('todos.txt', 'a')
        file.writelines(todos)
        print(todos.replace('\n',' '))
    case 'show':
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        for index, item in enumerate(todos):
            print(f"{index}-{item}")


