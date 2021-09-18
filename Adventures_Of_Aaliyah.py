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
    print("")
    faketype("Do you A) " + x + " or B) " + y + "?")

def next_room(z, pretext, object1, object2):
    if "A" in z:
        faketype("You entered the next room, in front of you "+ pretext + object1 + " and a " + object2)
        faketype("You can only choose one to equip do you equip the " + object1 + " Or the " + object2) 
        options(object1, object2)

faketype("Adventures Of Aaliyaah\n")
faketype("\n \n \n \n")
faketype("You are alone in a dark room.\nOn your left is a wooden door.\nOn your right is a metal door.")
print("\n")
faketype("")
def start():
    print("\n")
    # faketype("Do you A) Scream or B) Breathe and attempt to retrace your steps")
    options("choose the wooden door", "chooose the metal door")
    print("\n")
    answer = input(">").upper()

    next_room(answer, "lies a ", "sword", "shield")
    # if 'A' in answer: # Create a 'next_room function here
    #     faketype("You walked into the next room, in which a sign reads: 'you may equip one of the following: A) a sword or b) dual daggers ")
    #     faketype("")
            

    # elif "B" in answer: # and here
    #     faketype("Good job! You stayed calm and you found some footprints.")

start()