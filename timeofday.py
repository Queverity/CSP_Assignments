import datetime

currenttime = datetime.datetime.now()

print("Note: This program is written for Mountain Daylight Time. Adjustments are made accordingly.")
print("The current hour is:" + str(currenttime.hour - 6))
print("The current date and time (UTC) is:" + str(currenttime))

if currenttime.hour - 6 <= 12:
    print("Good morning!")
elif currenttime.hour - 6 <= 18:
    print("Good afternoon!")
elif currenttime.hour - 6 <= 24:
    print("Good evening!")
else:
    print("That's not a time.")



