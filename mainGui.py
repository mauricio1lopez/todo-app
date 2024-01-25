import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
todos = functions.getTodos()
ListBox = sg.Listbox(values=todos, key="todos",
                     enable_events=True, size=[45, 10])
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("Exit")

window = sg.Window("My To-Do App",[[clock],
                                   [label],
                                   [inputBox, addButton],
                                   [ListBox, editButton, completeButton],
                                   [exitButton]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos.append(values['todo'] + '\n')
            print(todos)
            functions.writeTodos(todos)
            window['todo'].update(value='')
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.writeTodos(todos)
                window['todo'].update(value='')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                functions.writeTodos(todos)
                window['todo'].update(value='')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()





