class Node:
    value = None
    key = None

#Ejercicio 2

def h(k):
  return (k % 9)

def insert(D, key, value):
    if search(D, key) == None:
        index = h(key)
        typeDate = type(D[index])
        N = Node()
        N.value = value
        N.key = key
        if typeDate == list:
            D[index].append(N)
        elif D[index] == None:
            D[index] = N
        else:
            L = [D[index], N]
            D[index] = L
    return D

def search(D, key):
    index = h(key)
    inicio = D[index]
    if type(inicio) == Node:
        if inicio.key == key:
            return inicio.value
    elif type(inicio) == list:
        for i in inicio:
            if i.key == key:
                return i.value
    return None
        
def delete(D, key):
    if search(D, key) != None:
        index = h(key)
        data = D[index]
        if type(data) == Node:
            D[index] = None
        else:
            iter = 0
            for i in data:
                if i.key == key:
                    data.pop(iter)
                iter += 1
    return D
        



#Otras funciones

def showDictionary(D):
    iter=0
    for i in D:
        if type(i) == list:
            list1 = []
            for n in i:
                list1.append(n.value)
            print(f"{iter}: {list1}")
        elif type(i) == Node:
            print(f"{iter}: {i.value}")
        else:
            print(f"{iter}: {i}")
        iter += 1
                