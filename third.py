def get_average_tem():
    with open('todos.txt','r') as file:
        todos = file.readlines()
        values = todos[1:]
        values = [float(i) for i in values]
        print(values)
        return(sum(values)/len(values))


x = get_average_tem()
print(x)

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])



