import pickle
count = 1
while True:
    cont = str(count)
    flag = input(": ")
    text = input("Enter a text: ")
    numberans = input("Enter a number of answers: ")
    if numberans == "2":
        firstans = input("1: ")
        firstlink = input("Enter the link to the next file: ")
        secondans = input("2: ")
        secondlink = input("Enter the link to the next file: ")
        if flag == "муз":
            musicpath = ('data/music/') + input("Enter music file name: ") + ('.mp3')
            result = [musicpath, secondlink, secondans, firstlink, firstans, numberans, text, flag]
        else:
            result = [secondlink, secondans, firstlink, firstans, numberans, text, flag]
    if numberans == "3":
        firstans = input("1: ")
        firstlink = input("Enter the link to the next file: ")
        secondans = input("2: ")
        secondlink = input("Enter the link to the next file: ")
        thirdans = input("3: ")
        thirdlink = input("Enter the link to the next file: ")
        if flag == "муз":
            musicpath = ('data/music/') + input("Enter music file name: ") + ('.mp3')
            result = [musicpath, thirdlink, thirdans, secondlink, secondans, firstlink, firstans, numberans, text, flag]
        else:
            result = [thirdlink, thirdans, secondlink, secondans, firstlink, firstans, numberans, text, flag]
    if numberans == 'end':
       result = [numberans, text, flag] 
    file = open(('engine/data/data' + (cont) + '.mag'), 'wb')
    pickle.dump(result, file)
    file.close()
    count += 1
