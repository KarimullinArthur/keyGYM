#!/usr/bin/python3

import getch
import time
import colorama

text = '''My notion was that you had been (Before she had this fit) An obstacle that
came between Him, and ourselves, and it. Don't let him know she liked them''' 
# some text

print(text,end='\r')

# main vars
lenght = len(text)
mistake = 0
right = 0

for x in range(lenght):
    char = getch.getch()

    if char == text[x]:

        if x == 0:
            start = time.time()

        print(colorama.Fore.GREEN,char, sep='', end='', flush=True)
        right += 1

    else:
        print(colorama.Fore.RED,char,   sep='', end='', flush=True )
        mistake += 1

# calc
finish = time.time()-start
finish = round(finish,2)

speed = right/(finish/60)
speed = round(speed,2)

mistakePercent = mistake/lenght*100
mistakePercent = round(mistakePercent,2)

# prints
print(colorama.Style.RESET_ALL)

print(f"\n\nmistake {mistakePercent}%")
print(f"speed (char/min) {speed}")
print(f"time {finish}s")
