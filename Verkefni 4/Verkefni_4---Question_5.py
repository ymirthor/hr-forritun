num = int(input("Input an int: ")) # Do not change this line
sum_num=0
for x in range(1,num+1):
     for y in range(1,x):
          #print(y,end=" + ")
          sum_num+=y
     sum_num+=x
     #print(x,end=" = ")
     print(sum_num)
     sum_num=0
