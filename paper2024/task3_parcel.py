# The parcel is:
# large - if the length, width and depth are all greater than 50
# medium - if the length and width are greater than 50, but the depth is 50 or less
# small - if either the length or the width is 50 or less

flag = True 
parcel_size = ""
while flag:
    length = float(input("What is the length of the parcel? "))
    width = float(input("What is the width of the parcel? "))
    depth = float(input("What is the depth of the parcel? "))

    # large
    if length>50 and width>50:
        if depth>50:
            parcel_size = "large"
        else:
            parcel_size = "medium"
    else:
        parcel_size = "small"
    # output the result
    print(f"The size of your parcel is: {parcel_size}")

    # ask if user wants more input
    more_parcels = input("Do you want to enter another parcel? (Y or N) ")
    more_parcels = more_parcels.upper() # case_insensitive
    if more_parcels == "N":
        flag = False
    