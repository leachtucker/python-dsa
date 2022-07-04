class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
                
            ptr = ptr.children[letter]

        ptr.isEndOfWord = True
        print("Inserted!")

    def search(self, word: str) -> bool:
        ptr = self.root

        for letter in word:
            if letter not in ptr.children:
                return False

            ptr = ptr.children[letter]
        
        if not ptr.isEndOfWord:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root

        for letter in prefix:
            if letter not in ptr.children:
                return False

            ptr = ptr.children[letter]
        
        return True
    

myTree = Trie()

myTree.insert("apple")

print(myTree.search("apple")) # expected: True
print(myTree.search("appl")) # expected: False

print(myTree.startsWith('appl')) # expected: True
print(myTree.startsWith('ap')) # expected: True