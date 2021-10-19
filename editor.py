import pickle
global text
def wrtchngs2(argument):
    argument = input(("Write new ") + (argument) + (": "))
    argument 
    data = [secondlink, secondans, firstlink, firstans, numberans, text, flag]
    print (data)
    file = open(('engine/data/data' + (cont) + '.mag'), 'wb')
    pickle.dump(data, file)
    file.close()
def wrtchngsmus2(argument):
    argument = input(("Write new ") + (argument) + (": "))
    result = [musicpath, secondlink, secondans, firstlink, firstans, numberans, text, flag]
    print (result)
    file = open(('engine/data/data' + (cont) + '.mag'), 'wb')
    pickle.dump(result, file)
    file.close()
def wrtchngs3(argument):
    argument = input(("Write new ") + (argument) + (": "))
    result = [thirdlink, thirdans, secondlink, secondans, firstlink, firstans, numberans, text, flag]
    print (result)
    file = open(('engine/data/data' + (cont) + '.mag'), 'wb')
    pickle.dump(result, file)
    file.close()
def wrtchngsmus3(argument):
    argument = input(("Write new ") + (argument) + (": "))
    result = [musicpath, thirdlink, thirdans, secondlink, secondans, firstlink, firstans, numberans, text, flag]
    print (result)
    file = open(('engine/data/data' + (cont) + '.mag'), 'wb')
    pickle.dump(result, file)
    file.close()
while True:
    cont = input("Which file you would like to edit?: ")
    file = open(('engine/data/data' + (cont) + '.mag'), 'rb')
    data = pickle.load(file)
    file.close()
    print(data)
    flag = data.pop()
    text = data.pop()
    numberans = data.pop()
    if numberans == '2':
        firstans = data.pop()
        firstlink = data.pop()
        secondans = data.pop()
        secondlink = data.pop()
        if flag == "1":
            musicpath = data.pop()
            inpt = input("What would you like to change?: ")
            wrtchngsmus2(inpt)
        else:
            inpt = input("What would you like to change?: ")
            wrtchngs2(inpt)
    if numberans == '3':
        firstans = data.pop()
        firstlink = data.pop()
        secondans = data.pop()
        secondlink = data.pop()
        thirdans = data.pop()
        thirdlink = data.pop()
        if flag == "1":
            musicpath = data.pop()
            inpt = input("What would you like to change?: ")
            wrtchngsmus3(inpt)
        else:
            inpt = input("What would you like to change?: ")
            wrtchngs3(inpt)
        
        
            
