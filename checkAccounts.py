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
        import collections
        print([item for item, count in collections.Counter(Col).items() if count > 1])


