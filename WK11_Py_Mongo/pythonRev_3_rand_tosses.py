import random

#Constants:

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        #simulation of coin tosses *10:
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")

main()
    
    