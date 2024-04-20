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
            parent.children.remove(current)
            current = parent

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
