from time import time
from time import sleep

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
            
def countdown():
    n = 15
    while n >= 1:
        print(n)
        sleep(1)
        n -= 1
        if n == 0:
            timer()
