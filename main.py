#!/usr/bin/python3

import getch
import time
import colorama

text = '''Mahomet was born at Mecca in Arabia, in the year of our Lord 571. He was of the tribe of the Korashites, esteemed the noblest in all that country, and was descended in a direct line, from Pher Koraish, the first founder of it.''' 
# some text

#print(text,end='\r')

# main vars
lenght = len(text)
mistake = 0
right = 0

text1 = text.split(', ')

a = len(text[0])
for x in range(lenght):

    if x == len(text1[0]):
        print(text1[1],end='\r')

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
