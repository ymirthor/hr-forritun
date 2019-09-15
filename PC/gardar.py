number_int = int(input("Enter an integer: ")) #Forritið biður notandan um input

the_sum = 0 #Breyta sem verður notið til þess að summa tölur
odd_number = 0 #Breyta sem verður notuð til þess að finna oddatölur
even_number = 0 #Breyta sem verður notuð til þess að finna sléttar tölur
largest_int = 0 #Breyta sem verður notið til þess að finna stærstu töluna

Cumlative_total = the_sum + number_int #Breyta sem verður notuð til að summa tölur

while number_int > 0: #Lykkjan heldur áfram svo lengi sem að talan er stærri en 0
    if number_int % 2 == 1: #Ef remainder af inputi er 1 þá er talan oddatala
        odd_number += 1 #Counter sem er notaður til þess að telja allar oddatölur
    if number_int % 2 == 0: #Ef remainder af inputi er 0 þá er talan slétt tala
        even_number += 1 
    if number_int > largest_int:
        largest_int = number_int
    print ("Cumulative total:", Cumlative_total)
    number_int = int(input("Enter an integer: "))
    the_sum += number_int
    Cumlative_total +=  number_int


if Cumlative_total != 0:
    print ("Largest number:",(largest_int))
    print ("Count of even numbers:", even_number)
    print ("Count of odd numbers:", odd_number)
