#varialbe
age=int(input("Enter your age: "))
#main program
#if age is from 0 to 34
if 0<=age<=34:
     print("Young")
#else if age is from 35 to 50
elif 35<=age<=50:
     print("Mature")
#else if age is from 51 to 69
elif 51<=age<=69:
     print("Middle-aged")
#else if age is more than 70
elif 70<=age:
     print("Old")
#else, age cannot be less than 0
else:
     print("Invalid age")
