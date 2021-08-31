money = int(input())
interest = 1.071
guaranteed_return = 700000

years = 0
while money < guaranteed_return:
    money *= interest
    years += 1

print(years)
