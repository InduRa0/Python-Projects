import numpy as np


# function to calculate grade
def calculate_grade(overall_mark):
    if overall_mark >= 70:
        return "1st"
    elif overall_mark >=50 and overall_mark <= 69:
        return "2nd"
    elif overall_mark >= 30:
        return "3rd"
    else:
        return "Fail"


# get input file name from user
while True:
    try:
        file_name = input("Please enter the name of the input file: ")
        with open(file_name) as f:
            # read the first line to get number of students and weighting
            num_students, weighting = map(int, f.readline().split())

            # create the first array with n rows and 4 columns
            marks_array = np.array([[0, 0.0, 0.0, 0.0]] * num_students)

            # read each remaining line and store the marks in the first array
            for i in range(num_students):
                reg_num, exam_mark, coursework_mark = map(float, f.readline().split())
                overall_mark = round((1 - weighting / 100) * exam_mark + (weighting / 100) * coursework_mark)
                marks_array[i] = [reg_num, exam_mark, coursework_mark, overall_mark]

            # define the named data type and create the second array
            student_dtype = np.dtype([('reg_num', int), ('exam_mark', int), ('coursework_mark', int),
                                      ('overall_mark', int), ('grade', 'U10')])
            students_array = np.array([(0, 0, 0, 0, '')] * num_students, dtype=student_dtype)

            # calculate grade and store in second array
            for i in range(num_students):
                reg_num, exam_mark, coursework_mark, overall_mark = marks_array[i]
                grade = calculate_grade(overall_mark)
                students_array[i] = (int(reg_num), int(exam_mark), int(coursework_mark), int(overall_mark), grade)

            # sort second array by overall mark
            students_array = np.sort(students_array, order='overall_mark')[::-1]

            # output second array to file
            output_file_name = file_name.split('.')[0] + '_output.txt'
            with open(output_file_name, 'w') as f:
                print(students_array, file=f)

            # output number of students with each grade and registration numbers of failures
            num_first = num_second = num_third = num_fail = 0
            fail_reg_nums = []
            for student in students_array:
                if student['grade'] == '1st':
                    num_first += 1
                elif student['grade'] == '2nd':
                    num_second += 1
                elif student['grade'] == 'Fail':
                    num_fail += 1
                    fail_reg_nums.append(str(student['reg_num']))

            print(f"Number of students with 1st class: {num_first}")
            print(f"Number of students with 2nd class: {num_second}")
            print(f"number of students with 3rd class: {num_third}")
            print(f"Number of students who failed: {num_fail}")
            print(f"Registration numbers of students who failed: {', '.join(fail_reg_nums)}")

        break

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
