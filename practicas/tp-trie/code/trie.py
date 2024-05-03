class Trie:
    root = None

class TrieNode:
    children = None
    parent = None
    key = None
    isEndOfTheWord = False

#Ejercicio 1

def insert(T, element):

    def searchWord(CurrentChild, index):
        if CurrentChild.children == None:
            CurrentChild.children = []
        for child in CurrentChild.children:
                if child.key == element[index]:
                    if len(element) == index+1:
                        child.isEndOfTheWord = True
                        return
                    index += 1
                    searchWord(child, index)
                    return

        insertCharacter(CurrentChild, index)
    
    def insertCharacter(currentNode, index):
        newNode = TrieNode()
        newNode.key = element[index]
        newNode.parent = currentNode
        currentNode.children.append(newNode)
        if len(element) == index+1:
            newNode.isEndOfTheWord = True
            return
        newNode.children = []
        insertCharacter(newNode, index+1)

    if T == None:
        T = Trie()
    if T.root == None:
        node = TrieNode()
        node.children = []
        T.root = node
    current = T.root
    searchWord(current, 0)

def search(T, element):

    if T == None or T.root == None:
        return False
    
    def searchR(currentNode, index):
        if currentNode.children == None:
            return False
        for child in currentNode.children:
            if child.key == element[index]:
                if len(element) == index+1:
                    if child.isEndOfTheWord == True:
                        return True
                    else:
                        return False
                index += 1
                return searchR(child, index)
        return False
    
    return searchR(T.root, 0)

#Ejercicio 3

def delete(T, element):
    
    def searchR(currentNode, index):
        if currentNode.children == None:
            return False
        for child in currentNode.children:
            if child.key == element[index]:
                if len(element) == index+1:
                    if child.isEndOfTheWord == True:
                        return child
                    else:
                        return False
                index += 1
                return searchR(child, index)
        return False

    if T == None or T.root == None:
        return False
    
    current = searchR(T.root, 0)
    if current == False:
        return False
    else:
        if current.children != None:
            current.isEndOfTheWord = False
            return True
        current.isEndOfTheWord = False
        while True:
            if current.isEndOfTheWord == True:
                return True
            parent = current.parent
            if parent == T.root:
                T.root.children.remove(current)
                return True
            if len(parent.children) > 1:
                parent.children.remove(current)
                return True
            else:
                parent.children = None
            current = parent

#Ejercicio 4

def Prefix(T, p, n):

    def searchEndOfPrefix(currentNode, index):
        if currentNode.children == None:
            return False
        for child in currentNode.children:
            if child.key == p[index]:
                if len(p) == index+1:
                    return child
                index += 1
                return searchEndOfPrefix(child, index)
        return False

    def findWords(currentNode, prefix, iter):
        if currentNode.children == None:
            if iter == n-len(p)+1:
                words.append(prefix)
            return
        for child in currentNode.children:
            if iter == n-len(p)+1:
                if currentNode.isEndOfTheWord == True:
                    words.append(prefix)
                    return
            if iter < n-len(p)+1:
                findWords(child, prefix + child.key, iter+1)
                
                    
    endPrefix = searchEndOfPrefix(T.root, 0)
    if endPrefix == False:
        print("No existen palabras que empiezen por", p)
        return
    words = []
    findWords(endPrefix, p, 1)
    if len(words) == 0:
        print("No existen palabras que empiezen por", p, "de", n, "caracteres")
        return
    print("Las palabras encontradas son:")
    for i in words:
        print(i)

#Ejercicio 5

def DuplicatedTrie(T1, T2):
    if T1 == None and T2 == None:
        return True
    elif T1 == None or T2 == None:
        return False
    
    a = get_all_words(T1)
    b = get_all_words(T2)
    
    if len(a) == len(b):
        if list.sort(a) == list.sort(b):
            return True
    
    return False

#El costo computacional es de O(n logn) + O(m logm), siendo n y m la cantidad de palabras de T1 y T2 respectivamente 

#Ejercicio 6

def invertedWords(T):

    def getWords(node, prefix):
        if node.isEndOfTheWord:
            return prefix
        if node.children != None:
            for child in node.children:
                return getWords(child, prefix + child.key)
        else: 
            return 
        
    if T== None or T.root == None:
        return False
    
    Tmodified = T

    while True:
        prefix = getWords(Tmodified.root, "", )
        print(prefix)
        delete(Tmodified, prefix)
        print(get_all_words(Tmodified))
        if search(T, prefix[::-1]):
            return True
        if len(Tmodified.root.children) == 0:
            return False

#Ejercicio 7

def autoCompletar(T, cadena):
    
    if T == None or T.root == None:
        return ""

    def searchEndOfPrefix(currentNode, index):
        if currentNode.children == None:
            return False
        for child in currentNode.children:
            if child.key == cadena[index]:
                if len(cadena) == index+1:
                    return child
                index += 1
                return searchEndOfPrefix(child, index)
        return False

    currentNode = searchEndOfPrefix(T.root, 0)
    complement = ""
    if currentNode == False or currentNode.children == None:
        return complement
    if len(currentNode.children) == 1:
        currentNode = currentNode.children[0]
    else: 
        return complement
    while True:
        if currentNode.children == None:
            return complement + currentNode.key
        if len(currentNode.children) == 1:
            if currentNode.isEndOfTheWord == True:
                return complement + currentNode.key
            complement = complement + currentNode.key
            currentNode = currentNode.children[0]
        else:
            return complement + currentNode.key

#Otras funciones

def _get_all_words(node, prefix, result):
    if node.isEndOfTheWord:
        result.append(prefix)
    if node.children != None:
        for child in node.children:
            _get_all_words(child, prefix + child.key, result)
    else: 
        return 

def get_all_words(trie):
    result = []
    _get_all_words(trie.root, "", result)
    return result

T = Trie()
insert(T, "dedos")
insert(T, "deli")
insert(T, "deseo")
insert(T, "desod")
print(get_all_words(T))
Prefix(T, "de", 5)