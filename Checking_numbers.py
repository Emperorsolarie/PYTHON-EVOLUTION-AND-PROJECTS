
try:
    num = int(input("Enter a number! "))
    number = num

    if number >=1:
        print("This is a positive number!")

    elif number < 0:
        print("This is a negative number!")

    else:
        print("this is zero")
except ValueError:
    print("This is not a number")



