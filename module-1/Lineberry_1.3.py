#Austin Lineberry
#June , 2026
#Written for Bellevue University CSD325
#Assignment 1.3

#This is some code to take input and recite the "beer on the wall" song

bottles = int(input("Enter number of bottles: "))

if bottles <= 0:
    input("Time to buy more bottles of beer")
    quit()
else:
    while bottles != 0 :
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("")
        bottles = bottles - 1
        print(f"Take one down, pass it around, {bottles} bottle(s) of beer on the wall.")
        
input("Time to buy more bottles of beer.")
quit()
        
