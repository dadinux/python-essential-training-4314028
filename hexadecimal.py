hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if any(char not in hexNumbers for char in hexNum):
        print('Errore: il numero inserito non è un numero esadecimale valido.')
    else:
        totl = 0
        l = len(hexNum) - 1
                
        for char in hexNum:
            totl = totl + (hexNumbers[char] * (16**l))
            l = l -1
        
        print(str(hexNum) + ' corrisponde in valore decimale a: ' + str(totl))

hexToDec('AAF10')