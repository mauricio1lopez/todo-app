import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
label2 = sg.Text("Enter inches: ")
input1=sg.InputText(tooltip="Enter feet: ")
input2=sg.InputText(tooltip="Enter inches: ")
add_button = sg.Button("Convert")

window = sg.Window('Convertor', layout = [[label1, input1],[label2, input2],[add_button]])
window.read()
window.close()

