def factor_check(number):
    factor=1
    factors=[]
    while factor<=number:
        if number%factor==0:
            factors.append(factor)
        factor+=1
    return factors

def prime_check(number):
    
    factor=1
    primes=[]
    
    while factor<=number:
        
        prime_factor=1
        prime=[]
        
        while prime_factor<=factor:
            
            if factor%prime_factor==0:
                prime.append(prime_factor)
                print(prime_factor)
                if len(prime)==2:
                    primes.append(prime_factor)
                
            prime_factor+=1
            
        factor+=1
    print(primes)    
    return primes

def print_list_nicely(message,a_list):
    print(message)
    for stack in a_list:
        print(stack, end=" ")
    print()

#program starts here


number=1
while number>=0:
    #gets input
    number=int(input("Input number: "))
    
    #prints out all factors in number
    print_list_nicely("Factors:",factor_check(number))
    
    #finds all primefactors in number
    primes=[]
    for i in factor_check(number):
        if prime_check(i):
            primes.append(i)

    #prints all primefactors in number
    print_list_nicely("Prime Factors:",primes)
