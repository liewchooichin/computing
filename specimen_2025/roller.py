# Task 4

# Who can ride the roller coaster

# - age over 7
# - age not more than 70
# - height greater than 1.3 m

# global variables
age = 0
height = float(0)
rejected = 0
rider = 0

# get input from user
def get_input():
    input_valid = False
    while not input_valid:
        try:
            age_input = input("Please enter your age, or enter 0 to quit: ")
            age_input= int(age_input)
            input_valid = True
        except ValueError:
            print("Input a valid age. Numbers only from 0 to 9")
            input_valid = False
    # reset flag
    input_valid = False
    # input 
    while not input_valid:
        try:
            height_input = input("Please enter your height: ")
            height_input = float(height_input)
            input_valid = True
        except ValueError:
            print("Input a valid height. For example, 0.9, 1.2 or 1.6")
            input_valid = False
    # return the value
    return age_input, height_input

# main
# loop for input until age=0 or height=0
age, height = get_input()
while (age != 0) and (height != 0):
    # age over 7 and less than 70
    if age < 7:
        rejected += 1
        print("You are too young to ride")
    elif age > 70:
        rejected += 1
        print("You are too old to ride")
    # age can pass, now check height
    else:
        # height greater than 1.3
        if height <= 1.3:
            rejected += 1
            print("You are too short to ride")
        else:
            rider += 1
            print("You can ride the Roller Coaster")
    
    # get input again
    age, height = get_input()

# print the number of riders and rejected
if (age == 0) or (height == 0):
    print(f"Program ended")
    print(f"Number of people rejected: {rejected}")
    print(f"Number of riders: {rider}")
