start = int(input())
end = int(input())
period_days = 12
iterations = 0

while start > end:
    start //= 2
    iterations += 1

print(iterations * period_days)
