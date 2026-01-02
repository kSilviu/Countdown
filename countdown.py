import time

def countdown():
    seconds = 0
    seconds = int(input("Enter time needed in seconds"))

    if seconds == 0:
        print("Countdown is over")

    while seconds != 0:
        time.sleep(1)
        seconds -= 1
        time.sleep(1)
        print(seconds+1, "seconds left!")

countdown()
