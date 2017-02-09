day = int(raw_input('Day (0-6)? '))

if day == 0:
    day = "Sunday"
elif day == 1:
    day = "Monday"
elif day == 2:
    day = "Tuesday"
elif day == 3:
    day = "Wednesday"
elif day == 4:
    day = "Thursday"
elif day == 5:
    day = "Friday"
elif day == 6:
    day = "Saturday"

print day
