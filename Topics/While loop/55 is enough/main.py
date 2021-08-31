# put your code here

goal = 55
number = int(input())
sum_of_numbers = 0
average = 0
counter = 0

while number != goal:
    counter += 1
    sum_of_numbers += number
    average = round(sum_of_numbers / counter)
    number = int(input())

print(counter)
print(sum_of_numbers)
print(average)
