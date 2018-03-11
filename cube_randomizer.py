from math import floor
from random import uniform

#Lists for the possible moves, and the generated moves.
moveset2x2 = ['R', '2R', 'L', '2L', 'U', '2U', 'D', '2D', 'B', '2B',
         "R' ", "2R' ", "L' ", "2L' ", "U' ", "2U' ", "D' ","2D' ", "B' ", "2B' "]
moveset3x3 = ['R', '2R', 'L', '2L', 'U', '2U', 'D', '2D', 'B', '2B',
         "R'", "2R'", "L'", "2L'", "U'", "2U'", "D'","2D'", "B'", "2B'",
         "M", "2M", "M'", "2M'"]

moves2x2 = []
moves3x3 = []

#Function for randomizing things.
def randomizer():
    
    #What cube the user is solving.
    cube = raw_input("What cube are you solving? Valid answers: 2x2, 3x3, quit  ")
    
    if cube == "quit" or cube == "q":
        return
    
    elif cube == "2x2" or cube == "2":
        for i in range(11):
            
            #Add all the moves to the list in the correct type.
            moves2x2.append(moveset2x2[int(floor(uniform(0, len(moveset2x2))))])
            
        #Prints the list with each moveset on a new line.
        n = 0
        while n <= 10:
            print(moves2x2[n])
            n += 1
        
        #Clear the list for the next scramble.
        for i in range(11):
            moves2x2.pop()
            
        randomizer()
        
    elif cube == "3x3" or cube == "3":
        for i in range(20):
            
            #Add all the moves to the list in the correct type.
            moves3x3.append(moveset3x3[int(floor(uniform(0, len(moveset3x3))))])
            
        #Prints the list with each moveset on a new line.
        n = 0
        while n <= 19:
            print(moves3x3[n])
            n += 1
        
        #Clear the list for the next scramble.
        for i in range(20):
            moves3x3.pop()
            
        randomizer()
            
    else:
        print("Invalid answer.")
        randomizer()
            
#Run the function.
randomizer()