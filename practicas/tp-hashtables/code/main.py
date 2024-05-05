from dictionary import *

#Ejercicio 4

def permutationString(s, p):
    
    D = [None]*max(len(s), len(p))
    for char in s:
        insert(D, ord(char), char)
    for char2 in p:
        if search(D, ord(char2)) == None:
            return False
    return True

#Ejercicio 5

def repeatedData(L):
    n = len(L)
    D = [None] * n
    for element in L:
        if search(D, element, n) != None:
            return False
        else:
            insert(D, element, element, n)
    return True

#Ejercicio 6

def hashPostal(zip):

    primerCaracter = zip[0].lower()
    primerNumero = zip[1]
    return ord(primerCaracter) - ord("a") + int(primerNumero )


#Ejercicio 7

def compresedString(string):
    string = string.lower()
    D = [None] * 10
    num = 0
    iter = 0
    charAct = ""
    compString = ""
    for char in string:
        if char == charAct:
            num += 1
        else:
            if num > 1:
                compString += str(num)
            compString += char
            charAct = char
            num = 1
    if num > 1:
        compString += str(num)
    if len(compString) > len(string):
        return string
    else:
        return compString

#Ejercicio 8



        

    