print ("Enter the number from 1 to 100: ")
number = int(input(">>> " ))
if number >= 1 and number <= 10:
    print("Loser")
elif number > 10 and number <= 30:
    print("Not bad!")
elif number > 30 and number <= 60:
    print("Better")
elif number > 60 and number <= 85:
    print("Good")
elif number > 85 and number <= 99:
    print("Great")
elif number == 100:
    print("Perfect")
