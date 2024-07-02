#Part 1: BackTracking
#Ejercicio 1
def darCambio(Cambio, Monedas):

    def darCambioR(cambioActual,monedasUtilizadas, mayorMonedas):
        for coin in reversed(Monedas):
            if cambioActual > coin:
                if len(monedasUtilizadas) + 1 < mayorMonedas:
                    p = darCambioR(cambioActual-coin,monedasUtilizadas + [coin], mayorMonedas + 1)
                    return p
                else: return len(monedasUtilizadas) + 1
            elif cambioActual == coin:
                return len(monedasUtilizadas)+1

    mayorMonedas = r = Cambio

    for coin in reversed(Monedas):
        if Cambio > coin:
            r = darCambioR(Cambio-coin,[coin],mayorMonedas)
        elif Cambio == coin:
            return 1
        
        if r < mayorMonedas:
            mayorMonedas = r

    return mayorMonedas

#Ejercicio 2
def mochila(PesoMax, latas):

    def agregarLatas(latasAgregadas, listRest, pesoAlcanzado):

        nonlocal pesoMaxAlcanzado, listMaxAlcanzada

        if len(listRest) == 0:
            return (latasAgregadas, pesoAlcanzado)

        for index in range(len(listRest)):

            if pesoAlcanzado + listRest[index] == PesoMax:
                return (latasAgregadas + [listRest[index]], pesoAlcanzado + listRest[index])
            elif pesoAlcanzado + listRest[index] < PesoMax:
                b = agregarLatas(latasAgregadas + [listRest[index]], listRest[index+1:len(listRest)], pesoAlcanzado + listRest[index])
                if b[1] < PesoMax:
                    if b[1] > pesoMaxAlcanzado:
                        pesoMaxAlcanzado = b[1]
                        listMaxAlcanzada = b[0]
                    else:
                        continue
                elif b[1] == PesoMax:
                    return b
                else:
                    return (latasAgregadas, pesoAlcanzado)
            else:
                if index == len(listRest)-1:
                    return (latasAgregadas, pesoAlcanzado)
                else:
                    continue
        
        return listMaxAlcanzada
    
    pesoMaxAlcanzado = 0
    listMaxAlcanzada= []

    for lata in range(len(latas)):
        a = agregarLatas([latas[lata]], latas[lata+1:len(latas)], latas[lata])
        if a[1] == PesoMax:
            return a[0]
        if a[1] > pesoMaxAlcanzado:
            pesoMaxAlcanzado = a[1]
            listMaxAlcanzada = a[0]
    
    return listMaxAlcanzada
    
#Ejercicio 3
def subsecuenciaCreciente(numeros):

    def proxElemento(secuenciaActual, listRest):
        nonlocal mejorSecuencia

        if len(secuenciaActual) > len(mejorSecuencia):
            mejorSecuencia = secuenciaActual

        for index in range(len(listRest)):
            if listRest[index] > secuenciaActual[-1]:
                proxElemento(secuenciaActual + [listRest[index]], listRest[index+1:len(listRest)])
            else:
                if len(secuenciaActual) + len(listRest) < len(mejorSecuencia):
                    return
                else:
                    continue
    
    mejorSecuencia = []

    for index in range(len(numeros)):
        secuenciaActual = [numeros[index]]
        proxElemento(secuenciaActual, numeros[index+1:len(numeros)])
        secuenciaActual.pop()
        if len(numeros) - index < len(mejorSecuencia):
            return mejorSecuencia
    
    return mejorSecuencia

#Ejercicio 4
def subconjuntoSuma(numeros, valor): 

    def sumar(sumaActual,listRest):

        print(sumaActual)

        nonlocal result

        if sumaActual == valor:
            return True

        for index in range(len(listRest)):
            if sumaActual + listRest[index] > valor:
                continue
            else:
                a = sumar(sumaActual + listRest[index], listRest[index+1:len(listRest)])

            if a == True:
                return a
            
        return False

    result = False

    return sumar(0,numeros)

#Part 2: Greedy
#Ejercicio 5
def adminActividades(tareas, inicio, fin):
    
    tareas.sort(key=lambda x:x[1])
    listAsks = []
    index = 0
    
    while index < len(tareas)-1:
        if tareas[index][0] < inicio or tareas[index][1] > fin:
            index += 1
        else:
            listAsks.append(tareas[index])
            start = index
            index = 0 
            break

    for ask in tareas[start+1:len(tareas)]:

        if ask[0] < inicio:
            continue
        if ask[1] > fin:
            break

        if ask[0] >= listAsks[index][1]:
            listAsks.append(ask)
            index += 1

    return listAsks

#Ejercicio 6
def buscaPares(vector):

    vector.sort()
    listPares = []
    max = vector[0] + vector[0]

    for i in range(len(vector)//2):
        num = vector[i] + vector[-1-i]
        listPares.append([vector[i],vector[-1-i]])
        if num > max:
            max = num
    
    return (listPares, max)

#Ejercicio 7
def mochilaGreedy(PesoMax, latas):
    
    latas.sort(key=lambda x:x[1])
    latasOrd = reversed(latas)
    latasFinales = []
    pesoActual = 0

    for lata in latasOrd:
        if pesoActual + lata[0] <= PesoMax:
            latasFinales.append(lata)
            pesoActual += lata[0]

        if pesoActual == PesoMax:
            break

    return latasFinales

#Parte 3: Divide and conquer
#Ejercicio 8:
def busquedaBinaria(lista, x): 

    def R(inicio,fin):

        if inicio == fin:
            return False

        k = (fin-inicio)//2

        if lista[inicio + k] == x:
            return True
        elif lista[inicio+k]<x:
            return R(inicio+k+1, fin)
        else:
            return R(inicio, inicio+k)
        
    return R(0, len(lista))
    
#Ejercicio 9:
def busquedaKesimo(lista, k):

    def partition(start, end, pivotIndex):
        pivot = lista[pivotIndex]

        lista[pivotIndex], lista[end] = lista[end], lista[pivotIndex]
        posPivot = start

        for i in range(start, end):
            if lista[i] < pivot:
                lista[posPivot], lista[i] = lista[i], lista[posPivot]
                posPivot += 1

        lista[end], lista[posPivot] = lista[posPivot], lista[end]
        return posPivot


    def quickselect(start, end, k):

        if start == end:
            return lista[start]
        
        pivotIndex = (start + end) // 2
    
        pivotIndex = partition(start, end, pivotIndex)
        
        if k == pivotIndex:
            return lista[k]
        elif k < pivotIndex:
            return quickselect(start, pivotIndex - 1, k)
        else:
            return quickselect(pivotIndex + 1, end, k)

    return quickselect(0, len(lista) - 1, k - 1)

#Ejercicio 10

def subsecuenciaCrecienteDC(numeros):

    sub = []
    pos = []

    def busquedaBinariaKey(sub, num):
        low, high = 0, len(sub) - 1
        while low <= high:
            mid = (low + high) // 2
            if sub[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return low

    for num in numeros:
        idx = busquedaBinariaKey(sub, num)
        if idx >= len(sub):
            sub.append(num)
        else:
            sub[idx] = num
        pos.append((idx, num))

    lis = []
    print(sub)
    print(pos)
    current_length = len(sub) - 1
    for idx, num in reversed(pos):
        if idx == current_length:
            lis.append(num)
            current_length -= 1

    return lis[::-1]

#Parte 4: Programacion Dinamica
#Ejercicio 12
def darCambioDP(Cambio, Monedas):

    tabla = {1: [k for k in range(Cambio+1)]}
    listaCambio = [None] * (Cambio + 1)
    lastCoin = 1

    for coin in Monedas[1:]:
        listaActual = listaCambio[:]
        for cambioActual in range(Cambio+1):
            if cambioActual >= coin:
                listaActual[cambioActual] = (min(tabla[lastCoin][cambioActual], listaActual[cambioActual-coin]+1))
            else:
                listaActual[cambioActual] = tabla[lastCoin][cambioActual]
        tabla[coin] = listaActual
        lastCoin = coin

    return tabla[Monedas[-1]][-1]

#Ejercicio 13
def mochilaDP(A, K):

    tabla = []

    for i in range(len(A)+1):
        columna = []
        for j in range(K+1):
            if j == 0:
                columna.append(True)
            else:
                columna.append(False)
        tabla.append(columna)
    
    for i in range(1,len(A)+1):
        for j in range(1,K+1):
            tabla[i][j] = tabla[i-1][j] or (j >= A[i-1] and tabla[i-1][j - A[i-1]])

    for element in tabla:
        print(element)
    return tabla[-1][-1]


#Ejercicio 14
def mejorCamino(tabla):

    n = len(tabla)

    for i in range(1,n):
        tabla[i][0] += tabla[i-1][0]
        tabla[0][i] += tabla[0][i-1]

    for i in range(1,n):
        for j in range(1,n):
            arriba = tabla[i-1][j]
            izquierda = tabla[i][j-1]
            tabla[i][j] += min(arriba, izquierda)

    for a in tabla:
        print(a)
    print()
    return tabla[-1][-1]

#Ejercicio 15
def LCS(X,Y):

    lenghtRoads = [[[0,None] for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

    for i in range(1,len(X)+1):

        for j in range(1, len(Y)+1):

            if X[i-1] == Y [j-1]:
                diagonal = lenghtRoads[i-1][j-1][0]
                lenghtRoads[i][j][0] = diagonal + 1
                lenghtRoads[i][j][1] = (i-1,j-1) #Padres
            else:
                arriba = lenghtRoads[i-1][j][0]
                izquierda = lenghtRoads[i][j-1][0]
                lenghtRoads[i][j][0] = max(arriba, izquierda)
                if arriba >= izquierda:
                    lenghtRoads[i][j][1] = (i-1,j)
                else:
                    lenghtRoads[i][j][1] = (i,j-1)

    ultimo = lenghtRoads[-1][-1]
    padre = ultimo[1]
    secuenciaFinal = ""

    while padre != None:
        
        if ultimo[0] != lenghtRoads[padre[0]][padre[1]][0]:
            secuenciaFinal = X[padre[0]] + secuenciaFinal
        ultimo = lenghtRoads[padre[0]][padre[1]]
        padre = ultimo[1]

    return secuenciaFinal





        
    
        
        




