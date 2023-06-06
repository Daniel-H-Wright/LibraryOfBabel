import random
import time
import colorama
from colorama import Fore
text = ''
x = 0
gate = False
while gate is False:
    word = input('word: ')
    number = input('number of ' + Fore.LIGHTYELLOW_EX + 'total' + Fore.LIGHTWHITE_EX + ' letters in puzzle: ')
    number = int(number) - len(word)
    if len(word) < 4:
        print(Fore.RED + '#[warning]: puzzles using words with 3 or less letters')
        print(end='')
        print('and that have a large number of characters in the puzzle')
        print(end='')
        print('often, due to their nature, take a long time to process.')
        time.sleep(1)
        decision = input(Fore.LIGHTMAGENTA_EX + 'continue? y/n: ')
        if decision.lower() == 'y':
            gate = True
        elif decision.lower() == 'n':
            gate = False
        else:
            gate = False
    else:
        gate = True
gate = False
text = Fore.LIGHTWHITE_EX + ''
while gate is False:
    x = 0
    while x < int(number):
        y = random.randint(1, 26)
        if y == 1:
            if word.find('a') == -1:
                x -= 1
            else:
                text = str(text) + 'a'
        elif y == 2:
            if word.find('b') == -1:
                x -= 1
            else:
                text = str(text) + 'b'
        elif y == 3:
            if word.find('c') == -1:
                x -= 1
            else:
                text = str(text) + 'c'
        elif y == 4:
            if word.find('d') == -1:
                x -= 1
            else:
                text = str(text) + 'd'
        elif y == 5:
            if word.find('e') == -1:
                x -= 1
            else:
                text = str(text) + 'e'
        elif y == 6:
            if word.find('f') == -1:
                x -= 1
            else:
                text = str(text) + 'f'
        elif y == 7:
            if word.find('g') == -1:
                x -= 1
            else:
                text = str(text) + 'g'
        elif y == 8:
            if word.find('h') == -1:
                x -= 1
            else:
                text = str(text) + 'h'
        elif y == 9:
            if word.find('i') == -1:
                x -= 1
            else:
                text = str(text) + 'i'
        elif y == 10:
            if word.find('j') == -1:
                x -= 1
            else:
                text = str(text) + 'j'
        elif y == 11:
            if word.find('k') == -1:
                x -= 1
            else:
                text = str(text) + 'k'
        elif y == 12:
            if word.find('l') == -1:
                x -= 1
            else:
                text = str(text) + 'l'
        elif y == 13:
            if word.find('m') == -1:
                x -= 1
            else:
                text = str(text) + 'm'
        elif y == 14:
            if word.find('n') == -1:
                x -= 1
            else:
                text = str(text) + 'n'
        elif y == 15:
            if word.find('o') == -1:
                x -= 1
            else:
                text = str(text) + 'o'
        elif y == 16:
            if word.find('p') == -1:
                x -= 1
            else:
                text = str(text) + 'p'
        elif y == 17:
            if word.find('q') == -1:
                x -= 1
            else:
                text = str(text) + 'q'
        elif y == 18:
            if word.find('r') == -1:
                x -= 1
            else:
                text = str(text) + 'r'
        elif y == 19:
            if word.find('s') == -1:
                x -= 1
            else:
                text = str(text) + 's'
        elif y == 20:
            if word.find('t') == -1:
                x -= 1
            else:
                text = str(text) + 't'
        elif y == 21:
            if word.find('u') == -1:
                x -= 1
            else:
                text = str(text) + 'u'
        elif y == 22:
            if word.find('v') == -1:
                x -= 1
            else:
                text = str(text) + 'v'
        elif y == 23:
            if word.find('w') == -1:
                x -= 1
            else:
                text = str(text) + 'w'
        elif y == 24:
            if word.find('x') == -1:
                x -= 1
            else:
                text = str(text) + 'x'
        elif y == 25:
            if word.find('y') == -1:
                x -= 1
            else:
                text = str(text) + 'y'
        elif y == 26:
            if word.find('z') == -1:
                x -= 1
            else:
                text = str(text) + 'z'
        x = x + 1

    if text.count(word) > 0:
        text = ''
        gate = False
    else:
        gate = True
    z = random.randint(1, int(number))
    text = text[:z] + Fore.RED + word + Fore.LIGHTWHITE_EX + text[z:]

print(text)
print(text.find(word))