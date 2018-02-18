
class Node:
    def __init__(self, data=None):
        self.data = data
        self.child_left = None
        self.child_right = None
        self.parent = None

class BineryTree:
    def __init__(self):
        self.root = Node()

    def add(self,data):
        if self.root.data == None:
            self.root.data = data
        else:

            self.__add(self.root, data)

    def __add(self, cur, data):

        if cur.data > data :

            if cur.child_left == None:
                cur.child_left = Node(data)
                cur.child_left.parent = cur
            else:
                self.__add(cur.child_left, data)
        elif cur.data < data :

            if cur.child_right == None :
                cur.child_right = Node(data)
                cur.child_right.parent = cur
            else:
                self.__add(cur.child_right, data)
        else:
            print('data already in tree  ')

    def find_nod(self, data):
        if self.root.data == None:
            return None
        else:
            return self.__find_node(self.root, data)
    def __find_node(self, cur, data):
        if cur.data == data:
            return cur
        elif cur.data > data:
            if cur.child_left == None:
                return None
            else:
               return self.__find_node(cur.child_left, data)
        else:
            if cur.child_right == None:
                return  None
            else:
                return self.__find_node(cur.child_right, data)
    def remove_data(self, data):
        return self.remove_node(self.find_nod(data))
    def remove_node(self, cur):
        if cur == None:
            print "Node not find in the tree"
            return None
        else:
            def num_children(node):
                num_children = 0
                if node.child_left != None:
                    num_children += 1
                if node.child_right != None:
                    num_children += 1
                return num_children
            def min_right_node(node):
                if node.child_left != None:
                    min_right_node(node.child_left)
                return  node
            children = num_children(cur)
            if children == 0:
                if cur.parent.child_left == cur:
                    cur.parent.child_left = None
                else:
                    cur.parent.child_right = None
            if children == 1:
                if cur.parent.child_left == cur:
                    if cur.child_left != None:
                        cur.parent.child_left = cur.child_left
                    else:
                        cur.parent.child_left = cur.child_right
                else:
                    if cur.child_left != None:
                        cur.parent.child_right = cur.child_left
                    else:
                        cur.parent.child_right = cur.child_right
            if children == 2:
                min_right = min_right_node(cur.child_right)
                cur.data = min_right.data
                self.remove_node(min_right)






    def get_sorttree(self):
        if self.root.data == None:
            print "tree is empty"
        else:
            self.__get_sorttree(self.root)
    def __get_sorttree(self,cur):
        if cur != None :
            self.__get_sorttree(cur.child_left)
            print (cur.data)
            self.__get_sorttree(cur.child_right)


tree1 = BineryTree()
tree2 = BineryTree()
nodes = [5,3,7,8,4,1]
for node in nodes:
    tree1.add(node)
tree1.get_sorttree()
tree2.get_sorttree()
tree1.remove_data(5)
print (tree1.get_sorttree())



        