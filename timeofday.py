import datetime

currenttime = datetime.datetime.now()

print(currenttime.hour)

if currenttime.hour <= 12:
    print("Good morning!")
elif currenttime.hour <= 18:
    print("Good afternoon!")
elif currenttime.hour <= 24:
    print("Good evening!")
else:
    print("That's not a time.")



