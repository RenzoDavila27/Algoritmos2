import random

def middleList(L):
    menores = 0
    mayores = 0
    secondHalf = 1
    bool1 = True
    pivotI = len(L)//2
    print(pivotI)
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
        print(L)


        

            
        


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
        