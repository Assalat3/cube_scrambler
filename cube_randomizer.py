from math import floor
from random import uniform

moveset2x2 = ['R', '2R', 'L', '2L', 'U', '2U', 'D', '2D', 'B', '2B',
         "R'", "2R'", "L'", "2L'", "U'", "2U'", "D'","2D'", "B'", "2B'"]
moveset3x3 = ['R', '2R', 'L', '2L', 'U', '2U', 'D', '2D', 'B', '2B',
         "R'", "2R'", "L'", "2L'", "U'", "2U'", "D'","2D'", "B'", "2B'",
         "M", "2M", "M'", "2M'"]

cube = raw_input("What cube are you solving? Valid answers: 2x2, 3x3, quit.")

def randomizer():
    
    if cube == "quit":
        return
    
    elif cube == "2x2":
        for i in range(11):
            print(moveset2x2[int(floor(uniform(0, len(moveset2x2))))])
            
    elif cube == "3x3":
        for i in range(20):
            print(moveset3x3[int(floor(uniform(0, len(moveset3x3))))])
            
    else:
        print("Invalid answer.")
            
randomizer()