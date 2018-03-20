#Importing randrange to get pseudorandom numbers.
from random import randrange

#Creating the lists that we need.
count = ["","2"]
moves = ["R", "L", "U", "F"]
prime = ["", "'"]

moves2x2 = []
moves3x3 = []

#The function to create the moves.
def randomizer():
    #Ask for user input. Start of the loop.
    cube = raw_input("What cube are you solving? Valid answers: 2x2 or 2, quit  ")
    
    #Stops the program.
    if cube == "quit" or cube == "q":
        return
    
    #For 2x2.
    if cube == "2x2" or cube == "2":
        #Adds letters to moves2x2 from moves.
        for i in range(11):
            moves2x2.append(moves[randrange(4)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 10:
            if moves2x2[n-1] == moves2x2[n]:
                moves2x2.pop(n)
                moves2x2.append(moves[randrange(4)])
                n -= 1
            n += 1
    
    #Adds together the number of moves, the move itself, and if it's prime.
    #Creates a list into which those get added.
    m = 0
    moveset2x2 = []
    while m <= 10:
        move = count[randrange(2)] + moves2x2[m] + prime[randrange(2)]
        moveset2x2.append(move)
        m += 1
    
    #Prints the list with each input in a new row.
    b = 0
    while b <= 10:
        print(moveset2x2[b])
        b += 1
    
    #Calls the function again.
    randomizer()
    
    #For 3x3
    if cube == "3x3" or cube == "3":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("D")
        moves.append("M")
        #Adds letters to moves3x3 from moves.
        for i in range(20):
            moves3x3.append(moves[randrange(7)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 19:
            if moves3x3[n-1] == moves3x3[n]:
                moves3x3.pop(n)
                moves3x3.append(moves[randrange(7)])
                n -= 1
            n += 1
    
    #Adds together the number of moves, the move itself, and if it's prime.
    #Creates a list into which those get added.
    m = 0
    moveset3x3 = []
    while m <= 19:
        move = count[randrange(2)] + moves3x3[m] + prime[randrange(2)]
        moveset3x3.append(move)
        m += 1
    
    #Prints the list with each input in a new row.
    b = 0
    while b <= 19:
        print(moveset3x3[b])
        b += 1
    
    #Calls the function again.
    randomizer()
    
#Calls the function.
randomizer()
