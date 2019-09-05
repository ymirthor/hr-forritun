#variable
n=int(input("Number of stars: "))
#input needs to be greater than zero
if n>=0:
     #for this problem, nested loops are perfect
     for i in range(1,n+1):#this loop prints from 1 to n
          for stars in range(1,i+1):#this loop runs for i times
               print("*",end="")#this prints out the stars
          print()#this seperates the stars into lines
#if the input is less or equal to zero the code doesn't run
else:
     print("Invalid input")
