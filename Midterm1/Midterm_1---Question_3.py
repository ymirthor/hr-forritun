#I put in the variables
first=int(input("First: "))
step=int(input("Step: "))
the_sum=0
#this step is nessasary because if the step is zero,
#it can not go into the range
#so when the step is 0 I print the first integer and add
#up untill the sum is 100 or more
if step==0:
     while the_sum<100:
          print(first,end=" ")
          the_sum+=first
          if the_sum>=100:
               print()
               break
#if the step is more than 0 this code runs
else:
     for number in range(first,999,step):
          print(number,end=" ")
          the_sum+=number
          if the_sum>=100:
               print()
               break
#I print the sum
print("Sum of series:",the_sum)
