def check_age():
    try:
        # Get user input
        age = input("Enter your age: ")
        age = int(age)

    
        if age < 18 or age > 100:
            raise ValueError("Age must be between 18 and 100.")
        
    
        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

    except ValueError as e:
        print(f"Invalid input: {e}")


check_age()
