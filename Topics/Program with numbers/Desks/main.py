students_first_group = int(input())
students_second_group = int(input())
students_third_group = int(input())


desks_first_class = students_first_group // 2 + students_first_group % 2
desks_second_class = students_second_group // 2 + students_second_group % 2
desks_third_class = students_third_group // 2 + students_third_group % 2

desks = desks_first_class + desks_second_class + desks_third_class

print(desks)
