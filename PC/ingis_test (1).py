def factor_check(number,factor):
    if factor == 1:
        return False
    elif number%factor==0:
        return True
    else:
        return False
ingi=1
while ingi>=0:
    ingi=int(input("Input number: "))

    counter=1
    factors=[]
    #finna factors
    while counter<=ingi:
        if factor_check(ingi,counter):
            factors.append(counter)
        counter+=1
    print("Factors:")
    for i in factors:
        print(i,end=" ")



    primes=[]
    for i in factors:
        prime=[]
        if i==1:
            primes.append(i)
        else:
            x=1
            while x<=i:
                if i%x==0:
                    prime.append(i)
                x+=1
            if len(prime)==2:
                primes.append(i)
    print()
    print("Prime Factors:")
    for x in primes:
        print(x,end=" ")
    print()
    print()
