from linkedlist import add, search, LinkedList

class AVLTree:
  root = None

class AVLNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None
  bf = None

#Ejercicio 1

def rotateLeft(Tree, avlnode):
  newRoot = avlnode.rightnode
  if newRoot.leftnode != None:
    newRoot.leftnode.parent = avlnode
    avlnode.rightnode = newRoot.leftnode
  else:
    avlnode.rightnode = None
  newRoot.leftnode = avlnode
  if avlnode.parent != None:
    newRoot.parent = avlnode.parent
    if avlnode.parent.rightnode == avlnode:
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
  else:
    Tree.root = newRoot
    newRoot.parent = None
  avlnode.parent = newRoot
  return newRoot
    
def rotateRight(Tree, avlnode):
  newRoot = avlnode.leftnode
  if newRoot.rightnode != None:
    newRoot.rightnode.parent = avlnode
    avlnode.leftnode = newRoot.rightnode
  else:
    avlnode.leftnode = None
  newRoot.rightnode= avlnode
  if avlnode.parent != None:
    newRoot.parent = avlnode.parent
    if avlnode.parent.rightnode == avlnode:
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
  else:
    Tree.root = newRoot
    newRoot.parent = None
  avlnode.parent = newRoot
  return newRoot

#Ejercicio 2

def calculateBalance(AVLTree):
      
  def PreOrdenR(NodeAVL):
    if NodeAVL != None:
      NodeAVL.bf = heightPlusOne(NodeAVL.leftnode) - heightPlusOne(NodeAVL.rightnode)   
      PreOrdenR(NodeAVL.leftnode) 
      PreOrdenR(NodeAVL.rightnode)
  PreOrdenR(AVLTree.root)

  return AVLTree

#Ejercicio 3

def ReBalance(AVLTree):
  calculateBalance(AVLTree)
  def PostOrdenR(NodeAVL):
      if NodeAVL != None:  
        PostOrdenR(NodeAVL.leftnode)
        PostOrdenR(NodeAVL.rightnode)
        if NodeAVL.bf < -1:
          if NodeAVL.rightNode.leftnode != None:
            NodeAVL = rotateRight(AVLTree, NodeAVL.rightnode).parent
            updateBF(NodeAVL)
            updateBF (NodeAVL.rightnode)
          newRoot = rotateLeft(AVLTree, NodeAVL)
          updateBF(newRoot)
          updateBF (newRoot.leftnode)
          NodeAVL = newRoot
        elif NodeAVL.bf > 1:
          if NodeAVL.leftnode.rightnode != None:
            NodeAVL = rotateLeft(AVLTree, NodeAVL.leftnode).parent
            updateBF(NodeAVL)
            updateBF (NodeAVL.leftnode)
          newRoot = rotateRight(AVLTree, NodeAVL)
          updateBF(newRoot)
          updateBF (newRoot.rightnode)
          NodeAVL = newRoot
  PostOrdenR(AVLTree.root)
  return AVLTree

#Ejercicio 4

def insertAvl(AVLTree, element, key):
  newNode = AVLNode()
  newNode.key = key
  newNode.value = element
  newNode.bf = 0
  def insertAvlR(current, newNode):
    if current.key == newNode.key:
      return None
    else:
      if current.key > newNode.key and current.leftnode != None:
        return insertAvlR(current.leftnode, newNode)
      elif current.key > newNode.key and current.leftnode == None:
        current.leftnode = newNode
        current.leftnode.parent = current
        return newNode
      elif current.key < newNode.key and current.rightnode != None:
        return insertAvlR(current.rightnode, newNode)
      elif current.key < newNode.key and current.rightnode == None:
        current.rightnode = newNode
        current.rightnode.parent = current
        return newNode
    

  if AVLTree.root == None:
    AVLTree.root = newNode
  else:
    insertedNode = insertAvlR(AVLTree.root, newNode)
    if insertedNode != None:
      currentParent = insertedNode.parent
      while currentParent != None:
        updateBF(currentParent)
        if abs(currentParent.bf) > 1:
          currentParent = balanceSubTree(AVLTree, currentParent)
        currentParent = currentParent.parent

  return key

#Ejercicio 5    

def delete(B, element):
  
  L = LinkedList()
  key = search(B, element)
  if key != None:
    current = deleteR(B, B.root, key, L)
    while current != None:
      if updateBF(current) > 1:
        current = balanceSubTree(B, current)
      current = current.parent
    return key
      

def deleteR(B, Node, key, L):
  
  def higherOfTheLowers(Node):
    current = Node.leftnode
    while current.rightnode != None:
      current = current.rightnode
    return current

  def lowersOfTheHigher(Node):
    current = Node.rightnode
    while current.leftnode != None:
      current = current.leftnode
    return current
  
  def searchNodeR(Node, key):
    if Node != None:
      if Node.key == key:
        return Node
      if searchNodeR(Node.leftnode, key) != None:
        return searchNodeR(Node.leftnode, key)
      return searchNodeR(Node.rightnode, key)
    
  nodeDelete = searchNodeR(Node, key)
  if nodeDelete == B.root:
    if nodeDelete.rightnode == None and nodeDelete.leftnode != None:
      candidato = higherOfTheLowers(B.root)
      current = candidato.parent
      if candidato.leftnode != None:
        add(L, candidato.leftnode)
        candidato.leftnode = None
        if candidato == nodeDelete.leftnode:
          nodeDelete.leftnode = candidato.leftnode
        else:
          candidato.parent.rightnode = L.head.value
      else:
        if nodeDelete.leftnode == candidato:
          nodeDelete.leftnode = None
        else:
          candidato.parent.rightnode = None
      while current != nodeDelete:
        updateBF(current)
        if abs(current.bf) > 1:
          current = balanceSubTree(B, current)
        current = current.parent
      add(L, nodeDelete.leftnode)
      candidato.leftnode = L.head.value
      B.root = candidato
      devolver = B.root
    elif nodeDelete.leftnode == None and nodeDelete.rightnode != None:
      candidato = lowersOfTheHigher(B.root)
      current = candidato.parent
      if candidato.rightnode != None:
        add(L, candidato.rightnode)
        candidato.rightnode = None
        if candidato == nodeDelete.rightnode:
          nodeDelete.rightnode = candidato.rightnode
        else:
          candidato.parent.leftnode = L.head.value
      else:
        if nodeDelete.rightnode == candidato:
          nodeDelete.rightnode = None
        else:
          candidato.parent.leftnode = None
      while current != nodeDelete:
        updateBF(current)
        if abs(current.bf) > 1:
          current = balanceSubTree(B, current)
        current = current.parent
      add(L, nodeDelete.rightnode)
      candidato.rightnode = L.head.value
      B.root = candidato
      devolver = B.root
    elif nodeDelete.leftnode != None and nodeDelete.rightnode != None:
      candidato = higherOfTheLowers(B.root)
      current = candidato.parent
      if nodeDelete.leftnode == candidato:
        nodeDelete.leftnode = candidato.leftnode
      else:
        candidato.parent.rightnode = candidato.leftnode
      add(L, nodeDelete.leftnode)
      add(L, nodeDelete.rightnode)
      while current != nodeDelete:
        updateBF(current)
        if abs(current.bf) > 1:
          current = balanceSubTree(B, current)
        current = current.parent
      candidato.leftnode = L.head.nextNode.value
      candidato.rightnode = L.head.value
      B.root = candidato
      devolver = B.root
  elif nodeDelete.leftnode == None and nodeDelete.rightnode == None:
    devolver = nodeDelete.parent
    if nodeDelete.parent.leftnode == nodeDelete:
      nodeDelete.parent.leftnode = None
    else:
      nodeDelete.parent.rightnode = None
  elif nodeDelete.leftnode != None and nodeDelete.rightnode == None:
    devolver = nodeDelete.parent
    if nodeDelete.parent.leftnode == nodeDelete:
      nodeDelete.parent.leftnode = nodeDelete.leftnode
    else:
      nodeDelete.parent.rightnode = nodeDelete.leftnode
  elif nodeDelete.leftnode == None and nodeDelete.rightnode != None:
    devolver = nodeDelete.parent
    if nodeDelete.parent.leftnode == nodeDelete:
      nodeDelete.parent.leftnode = nodeDelete.rightnode
    else:
      nodeDelete.parent.rightnode = nodeDelete.rightnode
  else:
    higher = higherOfTheLowers(nodeDelete)
    current = higher.parent
    if higher.leftnode != None:
      add(L, higher.leftnode)
      higher.leftnode = None
      add(L, higher)
      higher.parent.rightnode = L.head.nextNode.value
    else:
      add(L, higher)
      if nodeDelete.leftnode == higher:
        nodeDelete.leftnode = None
      else:
        higher.parent.rightnode = None
    while current != nodeDelete:
        updateBF(current)
        if abs(current.bf) > 1:
          current = balanceSubTree(B, current)
        current = current.parent
    add(L, nodeDelete.leftnode)
    add(L, nodeDelete.rightnode)
    if nodeDelete.parent.rightnode == nodeDelete:
      nodeDelete.parent.rightnode = L.head.nextNode.nextNode.value
      devolver = nodeDelete.parent.rightnode
      nodeDelete.parent.rightnode.rightnode = L.head.value
      nodeDelete.parent.rightnode.leftnode = L.head.nextNode.value
    elif nodeDelete.parent.leftnode == nodeDelete:
      nodeDelete.parent.leftnode = L.head.nextNode.nextNode.value
      devolver = nodeDelete.parent.leftnode
      nodeDelete.parent.leftnode.rightnode = L.head.value
      nodeDelete.parent.leftnode.leftnode = L.head.nextNode.value
  return devolver

  
def deleteKey(B, key):

  L = LinkedList()
  if searchNodeR(B.root, key) != None:
    current = deleteR(B, B.root, key, L)
    while current != None:
      if updateBF(current) > 1:
        current = balanceSubTree(B, current)
      current = current.parent
  return key

#Ejercicio 7

def AxB(A, x, B):
  hA = heightPlusOne(A.root)
  hB = heightPlusOne(B.root) 
  newNode = AVLNode()
  newNode.key = x
  if hA > hB:
    current = A.root
    for i in range(0, hA-hB-1):
      if current.rightnode == None:
        break
      current = current.rightnode
    newNode.rightnode = B.root
    newNode.rightnode.parent = newNode
    newNode.leftnode = current.rightnode
    newNode.leftnode.parent = newNode
    current.rightnode = newNode
    current.rightnode.parent = current
    current = current.rightnode
    while current != None:
      if abs(updateBF(current)) > 1:
        current = balanceSubTree(A, current)
      current = current.parent
    return A
  elif hB > hA:
    current = B.root
    for i in range(0, hB-hA-1):
      if current.leftnode == None:
        break
      current = current.leftnode
    newNode.leftnode = A.root
    newNode.leftnode.parent = newNode
    newNode.rightnode = current.leftnode
    newNode.rightnode.parent = newNode
    current.leftnode = newNode
    current.leftnode.parent = current
    current = current.leftnode
    while current != None:
      if abs(updateBF(current)) > 1:
        current = balanceSubTree(B, current)
      current = current.parent
    return B
  else:
    newNode.rightnode = B.root
    newNode.leftnode = A.root
    updateBF(newNode)
    Tree = AVLTree()
    Tree.root = newNode
    return Tree

  

#Otras Funciones
  
def imprimir_arbol(root, nivel=0, prefijo="Raíz: ", simbolo="☺"):
    if root != None:
      print(" " * (nivel * 4) + prefijo + simbolo, root.value)
      imprimir_arbol(root.leftnode, nivel + 1, "L--> ", "└──")
      imprimir_arbol(root.rightnode, nivel + 1, "R--> ", "└──")

def heightPlusOne(Node):
  if Node != None:
    if Node.leftnode == None and Node.rightnode == None:
      return 1
    elif Node.leftnode == None and Node.rightnode != None:
      return 1 + heightPlusOne(Node.rightnode)
    elif Node.rightnode == None and Node.leftnode != None:
      return 1 + heightPlusOne(Node.leftnode)
    else:
      if heightPlusOne(Node.rightnode) <= heightPlusOne(Node.leftnode):
        return 1 + heightPlusOne(Node.leftnode)
      elif heightPlusOne(Node.rightnode) > heightPlusOne(Node.leftnode):
        return 1 + heightPlusOne(Node.rightnode)
      else:
        return 0
  else: 
    return 0

def updateBF(AVLNode):
  AVLNode.bf = heightPlusOne(AVLNode.leftnode) - heightPlusOne(AVLNode.rightnode)
  return AVLNode.bf

def searchNodeR(Node, key):
    if Node != None:
      if Node.key == key:
        return Node
      if searchNodeR(Node.leftnode, key) != None:
        return searchNodeR(Node.leftnode, key)
      return searchNodeR(Node.rightnode, key)
    
def balanceSubTree(AVLTree, AVLNode):
  if AVLNode.bf < -1:
    if AVLNode.rightnode.leftnode != None:
      AVLNode = rotateRight(AVLTree, AVLNode.rightnode).parent
      updateBF (AVLNode.rightnode)
      updateBF(AVLNode.rightnode.rightnode)
    newRoot = rotateLeft(AVLTree, AVLNode)
    updateBF(newRoot)
    updateBF (newRoot.leftnode)
  elif AVLNode.bf > 1:
    if AVLNode.leftnode.rightnode != None:
      AVLNode = rotateLeft(AVLTree, AVLNode.leftnode).parent
      updateBF (AVLNode.leftnode)
      updateBF(AVLNode.leftnode.leftnode)
    newRoot = rotateRight(AVLTree, AVLNode)
    updateBF(newRoot)
    updateBF (newRoot.rightnode)
  return newRoot

def mostrarBF(root, nivel=0, prefijo="Raíz: ", simbolo="♥"):
  if root is not None:
      print(" " * (nivel * 4) + prefijo + simbolo, root.bf)
      mostrarBF(root.leftnode, nivel + 1, "L--> ", "└──")
      mostrarBF(root.rightnode, nivel + 1, "R--> ", "└──")
