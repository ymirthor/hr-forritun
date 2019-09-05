
#Creator: Ýmir Þórleifsson

#algorith to find special numbers:
for x in range(10,100):#tests all 2 digit numbers (start with 10 and end with 99)
     first=x//10#puts first diget into a variable
     second=x%10#puts second diget into a variable
     bool_special_number=((first+second)**2==x)#checks to see if number is special diget
     if bool_special_number:#if number is special_number
          print(x)#print (special) number

n=1#counter
while n<100:#test all numbers up to 100
     divisor_int=1#counter for divisor checker
     divisors=[]#list with divisors for n
     while divisor_int <= n:#tests all number up to n
          if n%divisor_int==0:#this checks if divisor_int (counter) is a divisor for n
               divisors.append(divisor_int)#this appends the divisor into the list
          divisor_int+=1#counter+=1
     bool_10_divisors=(len(divisors)==10)#if n has 10 divisor this bool becomes true
     if bool_10_divisors:#if number has 10 divisors
          print(n)#prints all numbers from 1-99 that have 10 divisors
     n+=1#counter+=1

