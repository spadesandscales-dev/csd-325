#Austin Lineberry
#June , 2026
#Written for Bellevue University CSD325
#Assignment 1.3

#This is some code to take input and recite the "beer on the wall" song

#Get number of bottles from user, save to bottles variable
bottles = int(input("Enter number of bottles: "))

#Determine if a positive number was used, end early if 0 or less than zero
if bottles <= 0:

#use input() to prevent quit() until input is recieved
    input("Time to buy more bottles of beer")
    quit()
else:
#Begin a loop to recite the song for each bottle 
    while bottles != 0 :
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("")

        #decrement by one before continuing the loop and song
        bottles = bottles - 1
        print(f"Take one down, pass it around, {bottles} bottle(s) of beer on the wall.")

#use input() to prevent quit() until input is recieved
input("Time to buy more bottles of beer.")
quit()
        
