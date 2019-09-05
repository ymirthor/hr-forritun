AB=1 #Starting number
CAB=AB*AB #formula where last two digets in CAB is the same as AB
last2=int(str(CAB)[-2:]) #check what the last two digets are, important for later
while len(str(CAB))!=3: #I know that CAB has length of 3 digets so I test for that
     AB+=1 #it din't work so I test next number
     CAB=AB*AB #updating variable
while AB!=last2:#if the last two digets of CAB is not the same as AB I keep testing the next diget
     AB+=1 #testing next diget
     CAB=AB*AB #updating variable
     last2=int(str(CAB)[-2:])#updating variable
#if number completed all the previous steps, it is the correct number
print(AB)#this prints 25, 25*25=625
