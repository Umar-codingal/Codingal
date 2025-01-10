try:
    num1, num2 =eval(input("Enter 2 numbers seperated by commas: "))
    result=num1/num2
    print("Result:",result)

except ZeroDivisionError as ex:
    print("Error:",ex)

except SyntaxError as y:
    print("Error:",y)

except :
    print("Error")

else:
    print("No error")

finally:
    print("hello")