
def existChar(s,c):
    for char in s:
        if char == s:
            return True
    return False

def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True

def mostRepeatedChar(String):
    chars = {}
    mayor = String[0]
    for char in String:
        chars[char] = chars.get(char,0) + 1
        if chars[char] > chars[mayor]:
            mayor = char
    return mayor

def getBiggestIslandLen(String):
    contador = 0
    mayor = 1
    for i in range(1, len(String)):
        if String[i] != String[i-1]:
            if mayor < contador:
                mayor = contador
            contador = 1
        else:
            contador += 1
    return mayor

def isAnagram(s,p):
    if len(s) != len(p):
        return False
    
    charsS = {}
    charsP = {}

    for charS,charP in zip(s,p):
        charsP[charP] = charsP.get(charP,0) + 1
        charsS[charS] = charsS.get(charS,0) + 1

    return charsS == charsP

def verifyBalancedParentheses(String):

    contador = 0

    for char in String:
        if char == "(":
            contador += 1
        elif char == ")":
            if contador > 0:
                contador -= 1
            else:
                return False
            
    return contador == 0

def reduceLen(String):

    newString = ""
    for i in range(0, len(String)-1,2):
        if String[i] != String[i + 1]:
            newString += String[i] + String[i+1]
        if i == len(String)-3:
            newString += String[len(String)-1]
        
    
    return newString

def isContained(string,secuency):

    j = i = 0

    while j < len(string) and i < len(secuency):
        if string[j] == secuency[i]:
            j += 1
        i += 1

    return j == len(string)

def isPatternContained(string,pattern,c):
    
    i = j = 0
    pattern = pattern.split(c)
    print(pattern)
    while i < len(string):

        print(string[i:i+len(pattern[j])], pattern[j])
        if string[i:i+len(pattern[j])] == pattern[j]:
            i += len(pattern[j])
            j += 1
            if j == len(pattern):
                return True
        else:
            i += 1

    return False

def RabinKarp(T,P):

    hashTable = {}
        
    m = len(P)

    for k in range(m):
        hashTable[P] = (27*hashTable.get(P,0) + ord(P[k])) % 64
        hashTable[T[0:m]] = (27*hashTable.get(T[0:m],0) + ord(T[k])) % 64

    for s in range(len(T)-m+1):

        if hashTable[P] == hashTable[T[s:s+m]]:
            if P == T[s:s+m]:
                return (f"Se encontro el patron en {s}")
        if s < len(T) - m:
            hashTable[T[s+1:s+m+1]] = 27 *((hashTable[T[s:s+m]] - 27^(m-1) * ord(T[s+1])) + ord(T[s+m])) % 64
    return(f"No se encontro el patron")

def KMP(T,P):

    def makePi():
        
        pi = [0] * (m)
        pi[0] = 0
        state = 0
        for q in range(1,m):
            while state > 0 and P[state] != P[q]:
                state = pi[state]
            if P[state] == P[q]:
                state += 1
            pi[q] = state

        return pi
    
    m = len(P)
    estado = 0
    pi = makePi()
    finalArray = []

    for i in range(0, len(T)):
        while estado > 0 and P[estado] != T[i]:
            estado = pi[estado-1]
        if P[estado] == T[i]:
            estado += 1
        if estado == m:
            finalArray.append(i-m+1)
            estado = pi[estado-1]

    return finalArray

def KMPMod(T,P):

    def makePi():
        
        pi = [0] * (m)
        pi[0] = 0
        state = 0
        for q in range(1,m):
            while state > 0 and P[state] != P[q]:
                state = pi[state]
            if P[state] == P[q]:
                state += 1
            pi[q] = state

        return pi
    
    m = len(P)
    estado = 0
    pi = makePi()
    finalArray = []

    for i in range(0, len(T)):
        while estado > 0 and P[estado] != T[i]:
            estado = pi[estado-1]
        if P[estado] == T[i]:
            estado += 1
        if estado == m:
            finalArray.append(i-m+1)
            estado = 0
    
    if len(finalArray) == 0:
        return None
    return finalArray
p = "aa"
a = "aabababaaa"