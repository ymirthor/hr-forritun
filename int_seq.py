#Creator: Ýmir Þórleifsson
#Date: 20/8/2019

#creating lists for all inputed numbers and for odd and even numbers
numbers=[]
odd=[]
even=[]

#Start of program, this keeps the program going for ever unless
#a specific action takes place that is if user inputs a number less or equal to 0
while True:
     num=int(input("Enter an integer: ")) #input
     if num<=0:
          break#closes while loop
     numbers.append(num)#all inputed numbers get put in here
     if num%2==0:#finds even numbers
          even.append(num)#even numbers go here
     else:#all numbers that are not even are odd
          odd.append(num)#odd numbers go here
     print("Cumulative total:",sum(numbers))
#the following lines are self explanatory
print("Largest number:",max(numbers))
print("Count of even numbers:",len(even))
print("Count of odd numbers:",len(odd))
