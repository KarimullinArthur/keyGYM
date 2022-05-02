#!/usr/bin/python3

import getch
import time
import colorama

text = "Hello world!" 

print(text,end='\r')

mistake = 0
right = 0

start = time.time()
for x in range(len(text)):
    char = getch.getch()

    if char == text[x]:
        print(colorama.Fore.GREEN,char, sep='', end='', flush=True)
        right += 1
    else:
        print(colorama.Fore.RED,char,   sep='', end='', flush=True )
        mistake += 1

finish = time.time()-start
finish = round(finish,2)

speed = right/(finish/60)
speed = round(speed,2)

mistakePercent = mistake/len(text)*100
mistakePercent = round(mistakePercent,2)

print(colorama.Style.RESET_ALL)

print(f"\n\nmistake {mistakePercent}%")
print(f"speed (char/min) {speed}")
print(f"time {finish}s")
