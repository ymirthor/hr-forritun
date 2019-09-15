low = int(input("Enter low: "))
high= int(input("Enter high: "))

the_sum = 0

for i in range(low, high+1,2):
        the_sum += i

print(the_sum)
