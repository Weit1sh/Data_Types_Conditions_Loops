print("What is your gender: ")
gender = input(">>> ")
gender = gender.lower()
if gender == "girl":
    print("Hi, girl!")
elif gender == "boy":
    print("Hi, boy!")
else:
    print("There is no such gender!")
