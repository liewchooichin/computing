# Task 2

list_username = ["StudentNo1", "JaneJones", "ABC123"]
#username = input("Please enter a username: ")
#password = input("Please enter a password: ")

# Q6
# add usernames if they do not exist in the list
test_username = ["StudentNo2", "GIJane", "JaneJones", "ABC123", "FrenchFriedFriday"]

# check username
def check_username(uname):
    if uname in list_username:
        print(f"{uname} exists in the list of usernames")
    else:
        list_username.append(uname)
        print(f"{uname} is added to the list of usernames")

# print the new list of usernames
# test username
for x in test_username:
    check_username(x)
print("Updated usernames:")
for x in list_username:
    print(x)

# notes for strings to elements
# >>> s
# ['abc']
# >>> s1 = list(s)
# >>> s1
# ['abc']
# # >>> s1 = list(s[0])
# >>> s1
# ['a', 'b', 'c']

# Q7
# Check for password
# contains at least one numeric character
# contains at least one special character @ ! / ?
# at least 8 characters long
test_password = ["1234567", "123ABC@/", "ABCDEFGH", "ABCDEFG!", "ABCD1234A", "ABCD1234!"]
numeric_char = [chr(i) for i in range(ord('0'), ord('9'))]
print(f"numeric: {numeric_char}")
special_char = ['@', '!', '/', '?']
print(f"special: {special_char}") 

# check password requirement
def check_password_requirement(pwd):
    flag_password_ok = False

    flag_length = False
    flag_numeric = False
    flag_special = False

    print(f"Checking .... {pwd}")
    # check for length
    if len(pwd) >= 8:
        flag_length = True
    # contains at least one numeric 
    # if cannot str.find(), return -1
    for ch in numeric_char:
        if pwd.find(ch) > -1:
            flag_numeric = True
    # contains at least one special character
    for ch in special_char:
        if pwd.find(ch) > -1:
            flag_special = True

    # is password requirement met?
    if flag_length and flag_numeric and flag_special:
        flag_password_ok = True
    else:
        flag_password_ok = False

    return flag_password_ok

# test password
for x in test_password:
    password_ok = check_password_requirement(x)
    result = "Ok" if password_ok else "Not valid"
    print(f"{x}: {result}")

# ask for input

# username
username = input("Please enter a username: ")
check_username(username)

# password
print("Password must be at least 8 characters, ")
print("contains 1 numeric and 1 special characters from @ ! / ?")
password = input("Please enter a password: ")
password_ok = check_password_requirement(password)
while not password_ok:
    password = input("Please enter a password: ")
    password_ok = check_password_requirement(password)
