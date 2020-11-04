import csv

def generateCol(path, col):
    with open(path, 'rU') as infile:
        reader = csv.DictReader(infile)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]

    Col = data[col]
    return Col

def checkIfDuplicates(array):
    if len(array) == len(set(array)):
        return False
    else:
        return True

def printDuplicates(array, Col):
    if checkIfDuplicates(array) == False:
        return False
    else:

        dup =[]
        progress = 0
        for i in range(len(array)):

            print(progress) #Uncomment for progress (This runs in O(n^2) which requires some time) remind me to implement faster algorithm
            progress=progress+1

            count = 0
            for j in range(len(array)):
                if array[i] == array[j]:
                    count = count + 1 
        
            if count > 1:
                dup.append(array[i])
        
        return(dup)
