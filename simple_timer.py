from time import time

def timer():
    try:
        input("Press enter to start the timer")
    except SyntaxError:
        pass
        t0 = time()
        try:
            input("Press enter to stop the timer")
        except SyntaxError:
            pass
            t1 = time()
            tfinal = (t1 - t0)
            print("Your time was:  {0: .3f}").format(tfinal)
