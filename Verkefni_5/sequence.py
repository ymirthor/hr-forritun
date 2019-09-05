#Creator: Ýmir Þórleifsson
"""
Design an algorithm that generates the first n numbers in the following sequence:
1,2,3,6,11,20,37,___,___,___,...
"""
n=int(input("Enter the length of the sequence: "))

n_sum=0
my_list=[]
     
for i in range(1,n+1):
     if i<=3:
          n_sum=i
          my_list.append(i)
     else:
          #use list to find next numbers
          #calculate next number to list
          next_n=(my_list[i-2]+my_list[i-3]+my_list[i-4])
          my_list.append(next_n)
for x in range(len(my_list)):
     print(my_list[x])
