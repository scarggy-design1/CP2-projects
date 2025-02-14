import os
from time import sleep
def cs(): # Clear Screen
    print("\033c",end="")
# some text
print("a")
print("b")
print("c")
print("d")
print("e")
print("Screen will now be cleared in 5 Seconds")

# Waiting for 5 seconds to clear the screen
sleep(2)

# Clearing the Screen
cs()