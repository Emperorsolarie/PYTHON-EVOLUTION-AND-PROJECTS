full_name = input("Enter your name!: ")
name_parts = full_name.strip().split()

if len(name_parts)>=2:
    first_name = name_parts[0]
    last_name = name_parts[-1]

    print(f"First_name: {first_name.upper()}")
    print(f"Last_name: {last_name.upper()}")

else:
    print("Enter at least two names")