try:

    number = int(input("Enter a number!: "))

    if number % 2 == 0:
        print("This is an even number!")

    else:
        print("this is an odd number")
except ValueError:
    print("This is not a number. You must enter a number!")
