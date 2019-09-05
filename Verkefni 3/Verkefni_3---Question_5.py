n = int(input("Input a natural number: ")) # Do not change this line
tester=1
factors=[] #this is all the factors of the number

# Fill in the missing code below
while tester<=n: #tester tests all numbers from 1 to n
     if n%tester==0: #if it is a factor I move on to next step
          factors.append(tester) #I append factors to factor list
     tester+=1 #try next positive natural number

prime=False #I assume all numbers are not prime
#unless the complete the following step
if len(factors)==2:#if the number has two factors, it is a prime
     prime=True
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")
