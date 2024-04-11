def filter_employees(employee_list, min_salary, max_salary):
    matching_employees = []
    for employee in employee_list:
        salary = employee[2]
        if salary >= min_salary and salary <= max_salary:
            matching_employees.append(employee)
    if matching_employees:
        matching_employees.sort(key=lambda x: x[2], reverse=True)
        print("{:<20} {:<20}".format("Name", "Job Title"))
        print("-" * 40)
        for employee in matching_employees:
            print("{:<20} {:<20}".format(employee[0], employee[1]))
    else:
        print("No matching employees found.")


file_name = input("Enter file name: ")
while True:
    try:
        with open(file_name, 'r') as file:
            employees = []
            for line in file:
                name, job_title, salary = line.strip().split(',')
                employees.append((name, job_title, int(salary)))
            print(employees)
            while True:
                min_salary = int(input("Enter minimum salary: "))
                max_salary = int(input("Enter maximum salary: "))
                filter_employees(employees, min_salary, max_salary)
                choice = input("Enter Q to quit or any other key to continue: ")
                if choice.lower() == 'q':
                    exit()
    except FileNotFoundError:
        file_name = input("File not found. Enter another file name: ")
