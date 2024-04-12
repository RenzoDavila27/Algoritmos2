class Trie:
    root = None

class TrieNode:
    children = []
    parent = None
    key = None
    isEndOfTheWord = False

def display_trie(trie):
    print("Palabras en el Trie:")
    if trie != None and trie.root != None and trie.root.children[0] != None and trie.root.children[0].key != None:
        _display_trie_helper(trie.root.children[0], "")
    else:
        return

def _display_trie_helper(node, prefix):
    if node.isEndOfTheWord:
            print(prefix)
            if len(node.children) != 0:
                _display_trie_helper(node.children[0], prefix + node.key)
            else: 
                return
    for i in range(0, len(node.children)+1):        
        _display_trie_helper(node.children[i], prefix + node.key)

T = Trie()
A= TrieNode()
A.children.append(TrieNode())
A.children[0].key = "A"
A.children[0].isEndOfTheWord = True
A.children[0].parent = A
T.root = 0


display_trie(T)
