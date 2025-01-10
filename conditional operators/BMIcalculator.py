weight=float(input("Enter your EXACT weight in kg: "))
height=float(input("Enter your height in CM: "))

bmi= weight/(height/100)**2

print(f"Your BMI is {bmi}")

if bmi<=18.4:
    print("you are underweight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are overweight")
elif bmi<=34.9:
    print("you are sevearly overweight")
elif bmi<=39.9:
    print("you are obeese")
else:
    print("Go to gym RIGHT NOW.")