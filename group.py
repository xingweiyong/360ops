#coding:utf-8

class Node(object):
    def __init__(self,data = -1,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        self.root = Node()
    #判断树是否为空
    def isEmpty(self):
        return True if self.root.data == -1 else False
    #增加节点
    def gen(self,data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def add(self,k,v):
        if self.isEmpty():
            self.root = k
            k.lchild = v
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node == k:
                    if tree_node.lchild == None:
                        tree_node.lchild = v
                        return
                    if tree_node.lchild == None and tree_node.rchild == None:
                        tree_node.rchild = v
                        return
            self.gen(k)
            self.gen(v)
                    
    def get(self,k):
        node = k
        if node == None:
            return
        print node.data
        if node.lchild == None and node.rchild == None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def pre_order_loop(self):
        if self.isEmpty():
            return
        stack = []
        node = self.root
        while node or stack:
            while node:
                print node.data
                stack.append(node)
                node = node.lchild
            if stack:
                node = stack.pop()
                node = node.rchild

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    print arr

    tree = BinaryTree()
    for i in arr:
        tree.gen(i)
    tree.add(Node(13),Node(76))
