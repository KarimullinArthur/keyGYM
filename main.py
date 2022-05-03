#!/usr/bin/python3

import getch
import time
import colorama

text = '''Mahomet was born at Mecca in Arabia, in the year of our Lord 571. He was of the tribe of the Korashites, esteemed the noblest in all that country, and was descended in a direct line, from Pher Koraish, the first founder of it.''' 
# some text

# main vars
lenght = len(text)
mistake = 0
right = 0

text1 = text.split(',')

print(text1[0],end='\r')
for sentence in range(len(text1)):

    for charStep in range(lenght):
    
        if charStep == len(text1[sentence]):
            for b in text1:
                a = len(text1[sentence])
                print('\b'*a,b,'\r',end='')
 
        char = getch.getch()
    
        if char == text[charStep]:
    
            if charStep == 0:
                start = time.time()
    
            print(colorama.Fore.GREEN,char, colorama.Style.RESET_ALL, sep='', end='', flush=True)
            right += 1
    
        else:
            print(colorama.Fore.RED,char,   colorama.Style.RESET_ALL, sep='', end='', flush=True )
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
