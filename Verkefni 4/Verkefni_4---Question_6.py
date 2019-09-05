#program will work for numbers up to 2305843008139952128, which is rank 8 of 51

top_num = int(input("Upper number for the range: ")) # Do not change this line

for p in range(2,top_num):
     if p==4 or p==6 or 7<p<13 or 17<p<19 or 19<p<31: #These are not perfect numbers
          continue
     perfect_number= 2**(p-1)*((2**p)-1)#formula
     if perfect_number>top_num:#stops when highest perfect number is reached
          break
     print(perfect_number)
