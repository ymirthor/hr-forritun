m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for x in range(1,m+1):
     if m%x==0 and n%x==0:
          GCD=x
print(GCD)
