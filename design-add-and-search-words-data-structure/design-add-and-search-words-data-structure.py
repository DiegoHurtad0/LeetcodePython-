class TrieNode(object):
    def __init__(self):
        #self.children = [None]*26
        self.isEndOfWord = False  
        self.children = dict()  
        
class WordDictionary(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()
    

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        
        current = self.root
        
        for c in word:
            if c not in current.children:
                #prefix = word[0:c+1]
                #current.children[c] = TrieNode(prefix)
                current.children[c] = TrieNode()
                

            current = current.children[c]

        current.isEndOfWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        #current = self.root
        #Output=[]
        
        nodelevel = [self.root]

        for char in word:
            Output = []

            if char == '.':
                for node in nodelevel:
                    Output.extend( node.children.values() )
            else:
                for node in nodelevel:
                    if char in node.children:
                        Output.append( node.children[char] )

            if not Output:
                return False

            nodelevel = Output

        for node in Output:
            if node.isEndOfWord:
                return True

        return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)