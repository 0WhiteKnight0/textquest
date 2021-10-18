from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pickle
import sys
from pygame import mixer
def player(musicpath):
    mixer.init()
    mixer.music.load(musicpath)
    mixer.music.play(-1,0.0)
norl = input("New game or Load(n or l)?: ")
if norl == "l":
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
    numberans = data.pop()
    if numberans == '2':
        firstans = data.pop()
        firstlink = data.pop()
        secondans = data.pop()
        secondlink = data.pop()
        print ((" ") + (text))
        if flag == "муз":
            musicpath = data.pop()
            player(musicpath)
        print (("1: ") + (firstans))
        print (("2: ") + (secondans))
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
        print ((" ") + (text))
        if flag == "муз":
            musicpath = data.pop()
            player(musicpath)
        print (("1: ") + (firstans))
        print (("2: ") + (secondans))
        print (("3: ") + (thirdans))
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
