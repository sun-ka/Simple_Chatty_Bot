# put your python code here
digit = int(input())
first_number = digit // 100
second_number = (digit - first_number * 100) // 10
third_number = digit % 10

print(first_number + second_number + third_number)
