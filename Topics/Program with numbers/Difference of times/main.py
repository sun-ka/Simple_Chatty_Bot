hour_walk = int(input())
minutes_walk = int(input())
seconds_walk = int(input())

hour_rain = int(input())
minutes_rain = int(input())
seconds_rain = int(input())

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

hour_difference = hour_rain - hour_walk
minutes_difference = minutes_rain - minutes_walk
seconds_difference = seconds_rain - seconds_walk

seconds_difference = hour_difference * SECONDS_IN_HOUR + minutes_difference * SECONDS_IN_MINUTE + seconds_difference
print(seconds_difference)
