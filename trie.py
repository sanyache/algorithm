
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
    def get_trie(self, node=None, prefix=None):

        dict_word = []
        if prefix == None:
            letter= ''
        else:
            letter= prefix[:-1]
        if node == None:
            node = self.root
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur == -1:
                letter = letter[:-1]
                continue
            if cur.data != None:
                letter += cur.data
                stack.append(-1)
            for char,nod in cur.children.items():
                stack.append(nod)
            if cur.is_word:
                dict_word.append(letter)
        return dict_word
    def prefix_list(self, prefix):
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                print ('dictionary does not have "%s" word'%(prefix))
                return
        return  self.get_trie(cur, prefix)
trie = Trie()
words = 'foo foobar foot footer bo boss'
for word in words.split():
    trie.add(word)

print(trie.his_word('bar'))
print trie.get_trie()
print trie.prefix_list('fo')
print trie.prefix_list('fool')
