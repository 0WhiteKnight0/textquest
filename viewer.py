import pickle
while True:
    numberfile = input("Enter file number: ")
    file = open(('data/data' + (numberfile) + '.mag'), 'rb')
    data = pickle.load(file)
    print (data)
    file.close()
