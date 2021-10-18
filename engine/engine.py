from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pickle
import sys
import time
from pygame import mixer
def player(musicpath):
    mixer.init()
    mixer.music.load(musicpath)
    mixer.music.play(-1,0.0)
def otpt(put):
    for char in put:
            print(char, end="", flush=True)
            time.sleep(0.02)
    print("")
musicpath = ("/")
norl = input("New game or Load?: ")
if norl == "load":
    save = open((('data/save.mag')), 'rb')
    savelist = pickle.load(save)
    musicpath = savelist.pop()
    count = savelist.pop()
    player(musicpath)
else:
    count = ('1')
while True:
    cont = str(count)
    file = open((('data/data') + (cont) + ('.mag')), 'rb')
    data = pickle.load(file)
    flag = data.pop()
    text = data.pop()
    output = (("  ")+(text))
    numberans = data.pop()
    if numberans == '2':
        firstans = data.pop()
        firstlink = data.pop()
        secondans = data.pop()
        secondlink = data.pop()
        otpt(output)
        print("")
        if flag == "1":
            musicpath = data.pop()
            player(musicpath)
        ans1out = (("1: ") + (firstans))
        ans2out = (("2: ") + (secondans))
        otpt(ans1out)
        otpt(ans2out)
        answer = input(": ")
        if answer == '1':
            count = firstlink
        elif answer == '2':
            count = secondlink
        elif answer == 'save' or 'exit' or 'quit':
            save = open((('data/save.mag')), 'wb')
            savelist = [cont, musicpath]
            pickle.dump(savelist, save)
            save.close()
            sys.exit()
    if numberans == '3':
        firstans = data.pop()
        firstlink = data.pop()
        secondans = data.pop()
        secondlink = data.pop()
        thirdans = data.pop()
        thirdlink = data.pop()
        for char in output:
            print(char, end="", flush=True)
            time.sleep(0.03)
        print("")
        if flag == "1":
            musicpath = data.pop()
            player(musicpath)
        ans1out = (("1: ") + (firstans))
        ans2out = (("2: ") + (secondans))
        ans3out = (("3: ") + (thirdans))
        otpt(ans1out)
        otpt(ans2out)
        otpt(ans3out)
        answer = input(": ")
        if answer == '1':
            count = firstlink
        elif answer == '2':
            count = secondlink
        elif answer == '3':
            count = thirdlink
        elif answer == 'save' or 'exit' or 'quit':
            save = open((('data/save.mag')), 'wb')
            pickle.dump(cont, save)
            save.close()
            sys.exit()
    elif numberans == 'end':
        print ((" ") + (text))
        a = "b"
        print ("")
        input("Press enter to exit")
        sys.exit()
