
# Task 4
# Prime

# Given

# The result is the quotient integer
def div_2(number):
    halved = int(number / 2)
    return halved

# test
print(div_2(4))
print(div_2(5))

# odd_or_even()
# return "Even" or "Odd"

def my_odd_or_even(number):
    result = "Odd" if (number % 2 == 1) else "Even"
    return result

# test
print(my_odd_or_even(4))
print(my_odd_or_even(5))


# Task 9
# Extend the given div_2() to check even or odd
# 

def odd_or_even(number):
    # return the quotient
    halved = int(number / 2)
    # if (quotient * 2) + 1 == number, then Odd
    # else if (quotient * 2) == number, then Even
    check_num = (halved * 2) + 1
    result = "Odd" if check_num==number else "Even"
    return result

# test
print(odd_or_even(0))
print(odd_or_even(1))
print(odd_or_even(4))
print(odd_or_even(5))


# Task 10
# prime number
# IMPORTANT: 1 is NOT a prime. 
# Because 1 can only be divided by 1. 
# Only divisible by 1 number, so it is NOT a prime.abs

# 2 and 3 are prime.

# Only need to check a number starting from 3
# Check up to half of the number by using div_2()

def prime(number):
    # check for even number
    if odd_or_even(number) == "Even":
        return "Not prime"
    # check for 1, 2, 3
    match (number):
        case 1:
            return "Not prime"
        case 2, 3:
            return "Prime"
    # Now, it should be just odd number here
    halved = div_2(number)
    # check from or equal to 4 onwards,
    # up to halved
    flag_prime = True
    for i in range(3, halved):
        if (number%i == 0):
            flag_prime = False
            break
    result = "Not prime" if flag_prime == False else "Prime"
    return result

# test
print(f"1: {prime(1)}")
print(f"2: {prime(2)}")
print(f"3: {prime(3)}")
print(f"4: {prime(4)}")
print(f"5: {prime(5)}")
print(f"7: {prime(7)}")
print(f"9: {prime(9)}")
print(f"15: {prime(15)}")
print(f"17: {prime(17)}")


# Task 11
# ask for input of whole number
# output: prime or not

def get_input():
    print("Check if a number is prime or not")
    user_number = input("Enter a whole number: ")
    # check if it is a whole number or not
    # keep asking for whole number
    while not user_number.isdigit():
        user_number = input("Enter a whole number: ")
    # now it is a digit only number
    number = int(user_number)
    print(f"{number}: {prime(number)}")

# test
get_input()
