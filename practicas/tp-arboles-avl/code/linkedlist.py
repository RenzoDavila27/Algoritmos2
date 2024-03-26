from typing import Counter


class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def add(L, element):
  Nodo = Node()
  Nodo.value = element
  Nodo.nextNode = L.head
  L.head = Nodo

def add_end(L, element):
  current = L.head
  newNode = Node()
  newNode.value = element
  if current != None:
    while current.nextNode != None:
      current = current.nextNode
    current.nextNode = newNode
  else:
    L.head = newNode

def search(L,element):
  CurrentNode = L.head
  contador = 0
  Posicion = None
  bool = True
  while CurrentNode != None and bool == True:
    if CurrentNode.value == element:
      Posicion = contador
      bool = False
    else:
      contador = contador + 1
      CurrentNode = CurrentNode.nextNode
  return Posicion

def searchNode(L, Node):
  current = L.head
  count = 0
  while current != None:
    if current == Node:
      return count
    else:
      count += 1
      current = current.nextNode
  
def insert(L, element, position):
  largo = length(L)
  CurrentNode = L.head
  contador = 0
  if largo > position:
    while contador < position - 1:
      CurrentNode = CurrentNode.nextNode
      contador = contador + 1
    newNode = Node()
    newNode.value = element
    newNode.nextNode = CurrentNode.nextNode
    CurrentNode.nextNode = newNode
  elif position == 0:
    add(L, element)
  elif position != 0 and largo == position:
    for i in range(0, position - 1):
      CurrentNode = CurrentNode.nextNode
    newNode = Node()
    newNode.value = element
    CurrentNode.nextNode = newNode
    contador = position
  else:
    contador = None
  return contador
  
def delete(L, element):
  position = search(L, element)
  CurrentNode = L.head
  contador = 0
  if position != None and position != 0:
    while contador < position - 1:
      CurrentNode = CurrentNode.nextNode
      contador = contador + 1
    if CurrentNode.nextNode != None:
        CurrentNode.nextNode = CurrentNode.nextNode.nextNode
        contador = contador + 1
    else:
      contador = None
  elif position == 0:
    L.head = CurrentNode.nextNode
  else:
    contador = None
  return contador

def deletePosition(L, position):
  CurrentNode = L.head
  contador = 0
  if position != None and position != 0:
    while contador < position - 1:
      CurrentNode = CurrentNode.nextNode
      contador = contador + 1
    if CurrentNode.nextNode != None:
      CurrentNode.nextNode = CurrentNode.nextNode.nextNode
      contador = contador + 1
    else:
      contador = None
  elif position == 0:
    L.head = CurrentNode.nextNode
  else:
    contador = None
  return contador

def length(L):
  CurrentNode = L.head
  contador = 0
  while CurrentNode != None:
    CurrentNode = CurrentNode.nextNode
    contador = contador + 1
  return contador

def access(L, position):
  CurrentNode = L.head
  contador = 0
  while CurrentNode != None and contador <= position:
    if contador == position:
      devolver = CurrentNode.value
      break 
    else:
      contador = contador + 1
      CurrentNode = CurrentNode.nextNode
  if CurrentNode == None:
    devolver = None
  return devolver

def accessNode(L, position):
  CurrentNode = L.head
  contador = 0
  while CurrentNode != None and contador <= position:
    if contador == position:
      devolver = CurrentNode
      break 
    else:
      contador = contador + 1
      CurrentNode = CurrentNode.nextNode
  if CurrentNode == None:
    devolver = None
  return devolver


def update(L, element, position):
  CurrentNode = L.head
  contador = 0
  while CurrentNode != None and contador <= position:
    if contador == position:
      CurrentNode.value = element
      break
    else:
      contador = contador + 1
      CurrentNode = CurrentNode.nextNode
  if CurrentNode == None:
    contador = None
  return contador

def showLinkedList(L):
  current = L.head
  while current != None:
    print(current.value, end ="|")
    current = current.nextNode
  print("")

def insertNode(L, posOriginal, posFinal):
  if posFinal != posOriginal:
    current1 = L.head
    contador = 0
    while contador != posOriginal:
      contador += 1
      current1 = current1.nextNode
    pepe = current1
    deletePosition(L, posOriginal)
    contador = 0
    current2 = L.head
    if posFinal != 0:
      while contador != posFinal - 1:
        contador += 1
        current2 = current2.nextNode
      pepe.nextNode = current2.nextNode
      current2.nextNode = pepe
    else:
      pepe.nextNode = L.head
      L.head = pepe

def switchNodes(L, posOriginal, posFinal):
  if posFinal != posOriginal:
    current1 = L.head
    contador = 0
    pepe = accessNode(L, posOriginal)
    deletePosition(L, posOriginal)
    if posFinal > posOriginal:
      posFinal -= 1
    pepe2 = accessNode(L, posFinal)
    deletePosition(L, posFinal)
    if posFinal != 0:
      current2 = accessNode(L, posFinal-1)
      pepe.nextNode = current2.nextNode
      current2.nextNode = pepe
    else:
      pepe.nextNode = L.head
      L.head = pepe
    if posOriginal != 0:
      current2 = accessNode(L, posOriginal-1)
      pepe2.nextNode = current2.nextNode
      current2.nextNode = pepe2
    else:
      pepe2.nextNode = L.head
      L.head = pepe2