import random

#La estrategia utilizada es elegir como pivote al elemento del medio, para luego contar la cantidad de menores y mayores a
#ese elemento que se encuentran en la lista, ademas de guardar los indices de estos. Luego intercambia menores con mayores en cada mitad de la lista en caso de ser necesario

def middleList(L):
    menores = 0
    mayores = 0
    secondHalf = 1
    bool1 = True
    pivotI = len(L)//2
    indicesMay = []
    indicesMen = []
    for i in range(0, len(L)):
        if L[i] < L[pivotI]:
            menores += 1
            indicesMen.append(i)
        elif L[i] > L[pivotI]:
            if i > pivotI and bool1 == True:
                secondHalf = mayores
                bool1 = False
            mayores += 1
            indicesMay.append(i)
    if len(indicesMay) == 0:
        return L
    count = 0
    bool1 = True
    for i in indicesMen:
        count +=1
        if i > pivotI and bool1 == True:
            count = 1
            bool1 = False
        if count > menores//2:
            if i < pivotI:
                b = random.randint(secondHalf, len(indicesMay)-1)
                L[i], L[indicesMay[b]] = L[indicesMay[b]], L[i]
                del indicesMay[b]
            elif i > pivotI:
                b = random.randint(0, secondHalf-1)
                L[i], L[indicesMay[b]] = L[indicesMay[b]], L[i]
                del indicesMay[b]

#El costo computacional de contiene_suma es de O(n log n) debido al merge sort que usamos para ordenar la lista

def Contiene_Suma(A,n):
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            mergeSort(L)
            mergeSort(R)
            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    if len(A) < 2:
        return False
    mergeSort(A)
    indexA = 0
    indexB = len(A)-1
    while True:
        if indexA == indexB:
            return False
        if A[indexA] + A[indexB] > n:
            indexB -=1
        elif A[indexA] + A[indexB] < n:
            indexA += 1
        else:
            return True