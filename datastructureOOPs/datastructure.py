#import section


class Stack:
    def __init__(self):
        self.stack = list()


    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            print(f"Empty stack : {str(self.stack)}")
        else:
            del(self.stack[-1])


    def peek(self):
        return self.stack[-1]

    def show_stack(self):
        print(f"Stack elements : {str(self.stack)}")

class Queue :
    def __init__(self):
        self.queue = list()


    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) < 1:
            print(f"Empty Queue : {str(self.queue)}")
        else:
            del(self.queue[0])


    def peek(self):
        return self.queue[0]

    def show_queue(self):
        print(f"Queue elements : {str(self.queue)}")


class MaxHeap:
    def __init__(self, items ):
        self.max_heap = list()
        self.max_heap.append(0)
        for item in items:
            self.max_heap.append(item)
            self.node_up(len(self.max_heap) -1)


    def push(self,item):
        self.max_heap.append(item)
        self.node_up(len(self.max_heap) - 1)

    def pop(self):
        if len(self.max_heap) -1 < 1:
            print("Max heap is Empty")
        elif len(self.max_heap)-1 > 0 and len(self.max_heap)-1 <=2:
            del(self.max_heap[1])
        else:
            self.swap_nodes(1,len(self.max_heap)-1)
            del(self.max_heap[-1])
            self.node_down(1)


    def getMax(self):
        if len(self.max_heap)-1 < 1:
            return "Empty Heap"
        else:
            return self.max_heap[1]

    def node_up(self,index):
        parent = index //2
        if index <= 1:
            return
        elif self.max_heap[index] > self.max_heap[parent] :
            self.swap_nodes(index,parent)
            self.node_up(parent)
        else:
            return
    def node_down(self,index):
        left = 2 * index
        right = 2 * index + 1
        heap_size = len(self.max_heap) - 1
        if heap_size >= left and heap_size >= right  :
            largest = self.max_heap[left] if self.max_heap[left] > self.max_heap[right] else self.max_heap[right]
            child_index = left if self.max_heap[left] > self.max_heap[right] else right
        elif heap_size >= left :
            largest = self.max_heap[left]
            child_index = left
        else:
            return
        if largest > self.max_heap[index]:
            self.swap_nodes(index , child_index)
            self.node_down(child_index)
        else:
            return


    def swap_nodes(self, index, parent):
        self.max_heap[index] , self.max_heap[parent] = self.max_heap[parent] , self.max_heap[index]

    def show_max_heap(self):
        if len(self.max_heap) - 1 < 1:
            print( "Empty Heap")
        else:

            print(f"Max Heap : {' --> '.join(map(str, self.max_heap[1:]))}")

# Node for linked list
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')


# single linked list
class Single_linked_list:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self,  d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return True
            else:
                this_node = this_node.next_node
        return False


    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False
    def show_linkedlist(self):
        this_node = self.root
        print("Root Node",end="-->")
        while this_node is not None:
            print(this_node, end="-->")
            this_node = this_node.next_node
        print('None')

# Circular Linked list
class Circular_linkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0


    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size +=1



    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node


    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -=1
                return True

            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def  show_linked_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="-->")
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node,end="-->")
        print()

# Double linked list
class Double_linkedList:
    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0


    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1


    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return False

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -=1
                return True
            else:
                this_node = this_node.next_node
        return False
    def show_linked_list(self):
        if self.size == 0:
            return
        this_node = self.root
        while this_node is not None:
            print(this_node, end="-->")
            this_node = this_node.next_node
        print("None")





## ************* Binary Tree Operation **************************

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


    def insertNode(self, data):

        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insertNode(data)
            else:
                self.left = BinaryTree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insertNode(data)
            else:
                self.right = BinaryTree(data)
                return True

    def findNode(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if  self.left is None:
                return False
            else:
                return self.left.findNode(data)
        else:
            if  self.right is None:
                return False
            else:
                return self.right.findNode(data)

    def get_size(self):
        if  self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return  1

    def preorder(self):
        if self is not None:
            print(self.data, end='-->')
            if self.left is not None:
               self.left.preorder()
            if self.right:
               self.right.preorder()


    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data,end='-->')
            if self.right is not None:
                self.right.inorder()

    def postorder(self):
        if self.right is not None:
            self.right.postorder()
        if self.left is not None:
            self.left.postorder()

        print(self.data, end='-->')




















