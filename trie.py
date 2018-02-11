
class Node:

    def __init__(self, data=None):
        self.data = data
        self.children = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = Node(char)
                cur = cur.children[char]
        cur.is_word = True
    def his_word(self, word):
        if word == '':
            rez = 'empty word'
            return  rez
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                rez = 'No'
                return rez
        if cur.is_word :
            rez = 'Yes'
        else:
            rez = 'No'
        return rez

trie = Trie()
words = 'foo foobar foot footer bo boss'
for word in words.split():
    trie.add(word)

print(trie.his_word('bo'))
