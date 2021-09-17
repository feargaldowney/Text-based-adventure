"""
Text-based adventure by Feargal Downey
Adventures Of Aaliyah
Created in Python 3.7.9
Date 17/09/21
"""



import time
import random
import sys
words = " "

def faketype(words):
  words
  for char in words:
    time.sleep(random.choice([0.001, 0.3, 0.04, 0.07,   0.07, 0.04, 0.06, 0.06, 0.05]))
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(1)

def options(x, y):
    faketype("Do you A) " + x + " or B " + y)

faketype("Adventures Of Aaliyaah\n")
faketype("\n \n \n \n")
faketype("You are in the woods with your friends\nYou have been walking in front for a while\nwhen you realise no-one has spoken in a long time...")
print("\n")
faketype("You turn around and your heart sinks...\nYou're friends are nowhere to be seen, the sun is beginning to fall and panic is about to set in...")
def start():
    print("\n")
    # faketype("Do you A) Scream or B) Breathe and attempt to retrace your steps")
    options("Scream", "Breathe and attempt to retrace your steps")
    print("\n")
    answer = input(">").upper()

    if 'A' in answer:
        faketype("You woke a sleeping bear...\nYou die")

    elif "B" in answer:
        faketype("Good job! You stayed cam and you found some footprints.")

start()



