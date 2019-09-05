#Höfundur: Ýmir Þórleifsson

#my variables
population_usa=307357870
year=31536000 #(60*60*24*365)

birth_rate=year/7 #convert from every x sec to x per year
death_rate=year/13 #convert from every x sec to x per year
immigration_rate=year/35 #convert from every x sec to x per year

#change in a year
change=birth_rate+immigration_rate-death_rate



years=int(input("Years: "))
#formula (I also convert to intiger)
new_population=int(population_usa+years*change)

#years variable needs to be positive and can also be 0
if years>=0:
     print("New population after",years,"years is",new_population)
else:
     print("Invalid input!")
