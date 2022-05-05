#!/usr/bin/python3

import getch
import time
import colorama

# some text
text = '''Mahomet was born at Mecca in Arabia, in the year of our Lord 571.''' 

# main vars
lenght = len(text)
mistake = 0
right = 0

textPart = text.split(',')

print(textPart[0],end='\r')
for sentence in range(len(textPart)):

    for charStep in range(lenght):
        char = getch.getch()

        if charStep == 0:
           start = time.time()
       
        if charStep == len(textPart[sentence]):
            for x in range(len(textPart)):
                a = len(textPart[sentence])
                print('\b'*a,textPart[x],'\r',end='',flush=True)

        if char == text[charStep]:
            print(colorama.Fore.GREEN,char, colorama.Style.RESET_ALL, sep='', end='', flush=True)
            right += 1
    
        else:
            print(colorama.Fore.RED,char,   colorama.Style.RESET_ALL, sep='', end='', flush=True)
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
