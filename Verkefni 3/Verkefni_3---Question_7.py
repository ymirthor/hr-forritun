holes=18
current_hole=1

while current_hole<=18:

     par=int(input())
     score=int(input())
     print("Par of hole",current_hole,":""Score on hole",current_hole,":")

     if score+3<par:
          print("invalid score")
     elif score+3==par:
          print("albatross")
     elif score+2==par:
          print("eagle")
     elif score+1==par:
          print("birdy")
     elif score==par:
          print("par")
     elif score-1==par:
          print("bogey")
     elif score-2==par:
          print("double boogey")
     elif score-3==par:
          print("triple boogey")
     else:
          print("bad hole")
     
