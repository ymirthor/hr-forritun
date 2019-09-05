#Höfundur: Ýmir Þórleifsson
secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = secs_int//3600
hours_leftover = secs_int%3600
minutes = hours_leftover//60
minutes_leftover = hours_leftover%60
seconds = minutes_leftover
print(hours,":",minutes,":",seconds) # do not change this line
