employee_file = open("index.html", "w")

# for employee in employee_file.readlines():
# print(employee)

# print(employee_file.read())

employee_file.write("<h1>Hello World!</h1>")

employee_file.close()
