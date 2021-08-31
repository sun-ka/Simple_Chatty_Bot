days = int(input())
food_cost_per_day = int(input())
flight_cost = int(input())
one_night_cost = int(input())

print((days * food_cost_per_day) + (flight_cost * 2) + one_night_cost * (days - 1))
