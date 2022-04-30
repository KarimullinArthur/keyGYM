import colorama
import getch

text = "Hello world!"
mistake = 0 
for x in range(len(text)):
    char = getch.getch()

    if char == text[x]:
        print(colorama.Fore.GREEN,char, sep='', end='', flush=True)
    else:
        print(colorama.Fore.RED,char,   sep='', end='', flush=True )
        mistake += 1
      
mistakePercent = mistake/len(text)*100
mistakePercent = round(mistakePercent,2)

print(f"\n\nmistake {mistakePercent}%")
print(colorama.Style.RESET_ALL)
