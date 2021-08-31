number = int(input()) + 1
factorial = 1
counter = 1

while counter < number:
    factorial *= counter
    counter += 1

print(factorial)
