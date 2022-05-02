#!/usr/bin/python3

import getch
import time
import colorama

text = "Hello world!" 

print(text,end='\r')

lenght = len(text)
mistake = 0
right = 0

for x in range(lenght):
    char = getch.getch()

    if x  == 0:
        start = time.time()
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

mistakePercent = mistake/lenght*100
mistakePercent = round(mistakePercent,2)

print(colorama.Style.RESET_ALL)

print(f"\n\nmistake {mistakePercent}%")
print(f"speed (char/min) {speed}")
print(f"time {finish}s")
