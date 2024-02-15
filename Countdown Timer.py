# import thr time module
import time

# define the countdown function.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

        print('Hello, How are you?')

# input time in second
t = input("Enter the time in seconds:")

# function call
countdown(int(t))
