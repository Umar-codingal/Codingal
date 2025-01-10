import os
n=input("Are you sure you want to shut down . (Y)/(N)")

if n.upper() == "N":
    exit()
else:
    os.system("shutdown /s /t 1")
