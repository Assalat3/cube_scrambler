#Importing randrange to get pseudorandom numbers and my timer.
from random import randrange

#Creating the lists that we need.
movesAddition = ["", "'", "2"]
moves = ["R", "L", "U", "F"]


moves2x2 = []
moves3x3 = []
moves4x4 = []
moves5x5 = []
moves6x6 = []
moves7x7 = []

#The function to create the moves.
def randomizer():
    #Ask for user input. Start of the loop.
    cube = str(input("What cube are you solving? Valid answers: 2x2 or 2, 3x3 or 3, 4x4 or 4, 5x5 or 5, 6x6 or 6, 7x7 or 7, and 1 for exit"))
    
    #Stops the program.
    if cube == "1":
        return
    
    #For 2x2.
    elif cube == "2x2" or cube == "2":
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
            move = moves2x2[m] + movesAddition[randrange(3)]
            moveset2x2.append(move)
            m += 1
        
        #Prints the list, with some formatting
        b = 0
        while b <= 9:
            print("{2}:{3}: {0:4}{1}").format(moveset2x2[b], moveset2x2[b+1], "Line", (b+1)/2)
            b += 2
            if b == 10:
                print("Line:5: " + moveset2x2[-1])
                
        #Clear the moves-list for next run
        for i in range(11):
            moves2x2.pop()
          
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()
    
    #For 3x3
    elif cube == "3x3" or cube == "3":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("D")
        #Adds letters to moves3x3 from moves.
        for i in range(20):
            moves3x3.append(moves[randrange(6)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 19:
            if moves3x3[n-1] == moves3x3[n]:
                moves3x3.pop(n)
                moves3x3.append(moves[randrange(6)])
                n -= 1
            n += 1
    
        #Adds together the number of moves, the move itself, and if it's prime.
        #Creates a list into which those get added.
        m = 0
        moveset3x3 = []
        while m <= 19:
            move = moves3x3[m] + movesAddition[randrange(3)]
            moveset3x3.append(move)
            m += 1
    
        #Prints the list, with some formatting
        b = 0
        while b <= 19:
            print("{4}:{5}: {0:4}{1:4}{2:4}{3}").format(moveset3x3[b], moveset3x3[b+1], moveset3x3[b+2], moveset3x3[b+3], "Line", (b+1)/4)
            b += 4
            
        #Removes the appended letters.
        for i in range(2):
            moves.pop()
            
        #Clear the moves-list for next run
        for i in range(20):
            moves3x3.pop()

            
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()
        
    #For 4x4
    elif cube == "4x4" or cube == "4":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("b")
        moves.append("D")
        moves.append("d")
        moves.append("f")
        moves.append("u")
        moves.append("r")
        moves.append("l")
        #Adds letters to moves4x4 from moves.
        for i in range(40):
            moves4x4.append(moves[randrange(12)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 39:
            if moves4x4[n-1] == moves4x4[n]:
                moves4x4.pop(n)
                moves4x4.append(moves[randrange(12)])
                n -= 1
            n += 1
    
        #Adds together the number of moves, the move itself, and if it's prime.
        #Creates a list into which those get added.
        m = 0
        moveset4x4 = []
        while m <= 39:
            move = moves4x4[m] + movesAddition[randrange(3)]
            moveset4x4.append(move)
            m += 1
    
        #Prints the list, with some formatting
        b = 0
        while b <= 39:
            print("{4}:{5}: {0:4}{1:4}{2:4}{3}").format(moveset4x4[b], moveset4x4[b+1], moveset4x4[b+2], moveset4x4[b+3], "Line", (b+1)/4)
            b += 4
            
        #Removes the appended letters.
        for i in range(8):
            moves.pop()
            
        #Clear the moves-list for next run
        for i in range(40):
            moves4x4.pop()


        
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()

    #For 5x5
    elif cube == "5x5" or cube == "5":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("b")
        moves.append("D")
        moves.append("d")
        moves.append("f")
        moves.append("u")
        moves.append("r")
        moves.append("l")
        #Adds letters to moves5x5 from moves.
        for i in range(60):
            moves5x5.append(moves[randrange(12)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 59:
            if moves5x5[n-1] == moves5x5[n]:
                moves5x5.pop(n)
                moves5x5.append(moves[randrange(12)])
                n -= 1
            n += 1
    
        #Adds together the number of moves, the move itself, and if it's prime.
        #Creates a list into which those get added.
        m = 0
        moveset5x5 = []
        while m <= 59:
            move = moves5x5[m] + movesAddition[randrange(3)]
            moveset5x5.append(move)
            m += 1
    
        #Prints the list, with some formatting
        b = 0
        while b <= 59:
            print("{4}:{5}: {0:4}{1:4}{2:4}{3}").format(moveset5x5[b], moveset5x5[b+1], moveset5x5[b+2], moveset5x5[b+3], "Line", (b+1)/4)
            b += 4
        
        #Removes the appended letters.
        for i in range(8):
            moves.pop()
            
        #Clear the moves-list for next run
        for i in range(60):
            moves5x5.pop()


        
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()

    #For 6x6
    elif cube == "6x6" or cube == "6":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("b")
        moves.append("3b")
        moves.append("D")
        moves.append("d")
        moves.append("3d")
        moves.append("f")
        moves.append("3f")
        moves.append("u")
        moves.append("3u")
        moves.append("r")
        moves.append("3r")
        moves.append("l")
        moves.append("3l")
        #Adds letters to moves6x6 from moves.
        for i in range(80):
            moves6x6.append(moves[randrange(18)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 79:
            if moves6x6[n-1] == moves6x6[n]:
                moves6x6.pop(n)
                moves6x6.append(moves[randrange(18)])
                n -= 1
            n += 1
    
        #Adds together the number of moves, the move itself, and if it's prime.
        #Creates a list into which those get added.
        m = 0
        moveset6x6 = []
        while m <= 79:
            move = moves6x6[m] + movesAddition[randrange(3)]
            moveset6x6.append(move)
            m += 1
    
        #Prints the list, with some formatting
        b = 0
        while b <= 79:
            print("{4}:{5}: {0:4}{1:4}{2:4}{3}").format(moveset6x6[b], moveset6x6[b+1], moveset6x6[b+2], moveset6x6[b+3], "Line", (b+1)/4)
            b += 4

        #Removes the appended letters.
        for i in range(14):
            moves.pop()
            
        #Clear the moves-list for next run
        for i in range(80):
            moves6x6.pop()


            
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()

    #For 7x7
    elif cube == "7x7" or cube == "7":
        #Adding some letters for scrambles to moves - list.
        moves.append("B")
        moves.append("b")
        moves.append("3b")
        moves.append("D")
        moves.append("d")
        moves.append("3d")
        moves.append("f")
        moves.append("3f")
        moves.append("u")
        moves.append("3u")
        moves.append("r")
        moves.append("3r")
        moves.append("l")
        moves.append("3l")
        #Adds letters to moves6x6 from moves.
        for i in range(100):
            moves7x7.append(moves[randrange(18)])

        #Removes back to back letters that are the same.
        n = 1
        while n <= 99:
            if moves7x7[n-1] == moves7x7[n]:
                moves7x7.pop(n)
                moves7x7.append(moves[randrange(18)])
                n -= 1
            n += 1
    
        #Adds together the number of moves, the move itself, and if it's prime.
        #Creates a list into which those get added.
        m = 0
        moveset7x7 = []
        while m <= 99:
            move = moves7x7[m] + movesAddition[randrange(3)]
            moveset7x7.append(move)
            m += 1
    
        #Prints the list, with some formatting
        b = 0
        while b <= 99:
            print("{4}:{5}: {0:4}{1:4}{2:4}{3}").format(moveset7x7[b], moveset7x7[b+1], moveset7x7[b+2], moveset7x7[b+3], "Line", (b+1)/4)
            b += 4

        #Removes the appended letters.
        for i in range(14):
            moves.pop()
            
        #Clear the moves-list for next run
        for i in range(100):
            moves7x7.pop()


            
        #Calls the timer function.
        #timer()
    
        #Calls the function again.
        randomizer()

        
    else:
        print("Invalid input.")
        randomizer()
    
#Calls the function.
randomizer()
