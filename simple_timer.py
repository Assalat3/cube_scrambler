import time

def timer():
    try:
        input("Press enter to start the timer")
    except SyntaxError:
        pass
        t0 = time.time()
        try:
            input("Press enter to stop the timer")
        except SyntaxError:
            pass
            t1 = time.time()
            tfinal = str(t1 - t0)
            print("Your time was: " + tfinal)
