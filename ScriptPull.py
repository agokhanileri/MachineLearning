# Contents: Useful classes/methods to utilize in problems and projects
 # Classes: LinkedList, BinaryTree,     - to use classes: from ScriptPull import MyClass
 # Methods: clear_all, bsearch, qsort   - to use methods: from ScriptPull import *


# -----------------------------------
# Clear variables
def clear_all():                             # not working yet
    # import gc
    # gc.collect()

    for name in dir():
        if not name.startswith('_'):
            del globals()[name]             # KeyError: 'gc'

    # import sys, os
    # clear = lambda: os.system('cls')
    # clear()
    # reset                                 # only works with ipython or jupyter notebook

    # Check: print(locals().keys())
    return None


# -----------------------------------
# Compare
def cmp(num1, num2):                    # = math.cmp(a,b), N/A for Python 3.x
    return (num1 > num2) - (num1 < num2)


# -----------------------------------
# BinarySearch
def bsearch(arr, val):
    n = len(arr)
    i = int(round(n / 2, 0))
    cnt = 1
    while i < n:
        if arr[i] == val:
            return i
        elif arr[i] > val:
            cnt = cnt + 1
            i = i - int(round((n / (2**cnt)), 0))
        else:
            cnt = cnt + 1
            i = i + int(round((n / (2**cnt)), 0))
    return -1


# -----------------------------------
# QuickSort
def part(arr, L, R):
    i = L - 1                               # index to place the valsfound, start at -1
    #j = L                                  # index to compare to pivot
    for j in range(L, R):                   # pivot is the R
        #print(L, R, i, j, arr)
        if arr[j] < arr[R] :                # if smaller value found
            i = i + 1                       # prepare it's index (i)
            temp = arr[j]                   # switch it with (j)
            arr[j] = arr[i]                 # places smaller elements to left of pivot and vv.
            arr[i] = temp                   #
    temp = arr[R]                           # since 0-i contains smaller than pivot,
    arr[R] = arr[i+1]                       # place pivot at i+1
    arr[i+1] = temp
    return i+1                              # pivot is placed at i, it's sorted!

def qsort(arr, L, R):                  # recursion to divide, real issue is to merge
    if L < R:
        pivot = part(arr, L, R)
        qsort(arr, L, pivot-1)         # sort left
        qsort(arr, pivot + 1, R)       # sort right

# -----------------------------------
# Stack
class Stack:
    def __init__(self):
        self.arr = []
    def isEmpty(self):
        return self.arr == []

    def push(self, x):
        self.arr.append(x)
    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.arr.pop()

    def peek(self):
        return self.arr[-1]
    def print(self):
        return self.arr
    def size(self):
        return len(self.arr)


# -----------------------------------
# LinkedList
class LinkedNode:  # better to put it in LinkedList() if multiple things point to the head
    def __init__(self, data):  # init an node
        self.data = data  # assign data if given, o.w. null
        self.next = None  # init a null next

    def print_node(self):
        temp = self.data
        if temp:  # if there's a data there?
            print(self.data)

class LinkedList:
    def __init__(self):  # init the head
        self.head = None  # why not data?

    def len_ll(self):
        temp = self.head
        cnt = 0
        while temp:   # if there's a data there?
            cnt = cnt + 1
            temp = temp.next  # go to next data
        return cnt

    def print_ll(self):
        temp = self.head
        while temp:  # if there's a data there
            print(temp.data, end=" ")
            temp = temp.next  # go to next node index
        print("\r")

    def get_data(self, n):
        temp = self.head
        cnt = 0  # node counter
        while temp and (cnt < n):  # instead of cnt < n, can do
            # while temp and (temp.data == val): # alternative if value input
            # if cnt == n:
            temp = temp.next  # go to next node index
            cnt = cnt + 1
        return temp.data

    def set_data(self, n, val):
        temp = self.head  # start scanning from head till..
        cnt = 0  # node counter
        while temp and (cnt < n):  # there's a data
            temp = temp.next  # go to next node index
            cnt = cnt + 1  # eventually reaches n
        temp.data = val  # then value is inserted there

    def ins_data(self, n, val):  #
        temp = self.head
        cnt = 0
        if n == 0:  # if inserting to the head
            self.head = LinkedNode(val)
            self.head.next = temp  # previous head becomes the next
        else:
            while temp and (cnt < n - 1):  # append --> just remove cnt < condition
                # if cnt == n:
                temp = temp.next
                cnt = cnt + 1
            new_node = LinkedNode(val)  # create the node to be inserted
            new_node.next = temp.next  # make next of new Node as next of prev_node
            temp.next = new_node  # link the given node to this node

    def del_data(self, n):  # deletes n-th node
        temp = self.head
        cnt = 0  # node counter
        if n == 0:
            self.head = temp.next
            temp = None
        else:
            while temp and (cnt < n - 1):
                # if cnt == n:
                temp = temp.next
                cnt = cnt + 1
            bad_node = temp.next
            temp.next = temp.next.next
            # del bad_node                     # free from memory
            bad_node.next = None  # alternative


# -----------------------------------
# BinaryTree
class BinaryTree:
    def __init__(self, root):
        self.root = root

class BinaryNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def bt_insert(self, data):  # BST style insert
        if self.data:
            if data < self.data:  # compare the new value with the parent node
                if self.left is None:  # no node yet
                    self.left = BinaryNode(data)
                else:
                    self.left.insert(data)  # there's a node but wanna overwrite
            elif data > self.data:
                if self.right is None:
                    self.right = BT_node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def set_left(self, data):  # direct insert
        if self.left is None:  # no node yet
            self.left = BinaryNode(data)

    def set_right(self, data):  # direct insert
        if self.right is None:  # no node yet
            self.right = BinaryNode(data)

    def print_node(self):  # inorder
        if self.left:
            self.left.print_node()  # recursive print left nodes first
        print(self.data)  # print root
        if self.right:  # print right nodes
            self.right.print_node()

    def inorder(self, root):  # Left -> Root --> Right
        res = []
        if root:  #
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

    def postorder(self, root):  # Root --> Left --> Right
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)  #
        return res

    def preorder(self, root):  # Left --> Right --> Root
        res = []
        if root:
            res.append(root.data)  #
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def bfs(self, root):  # Lparent --> Lchildren --> Rparent --> Rchildren
        res = []
        q = [root]  # queue of visited nodes
        while len(
                q) > 0:  # while + pop = go back and retry until all queue popped
            node = q.pop(0)  # 1st layer
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
