f = open('flights.txt', 'r')
mary=[]
phil=[]
john[]
for line in f:
    x=line.split()
    if x[0]=="John":
        john.append(x[0])
    elif x[0]=="Mary":
        mary.append(x[0])
    else:
        phil.append(x[0])
f.close()

mary