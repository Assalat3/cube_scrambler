import math
import random
moves = ['R', '2R', 'L', '2L', 'U', '2U', 'D', '2D', 'B', '2B',
         "R'", "2R'", "L'", "2L'", "U'", "2U'", "D'","2D'", "B'", "2B'"]

cube = raw_input("Which cube are you solving? Valid answers: 2x2, 3x3.")

if cube == "2x2":
    for i in range(11):
        print(moves[int(math.floor(random.uniform(0, len(moves))))])