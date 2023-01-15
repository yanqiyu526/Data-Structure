from LinkedList import LinkedList

class CBTree():
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        return self.linkedList.isEmpty()

    def size(self):
        return self.linkedList.size

    def getRoot(self):
        return self.linkedList.head

    def getKey(self, i : int):
        return self.linkedList.getKey(i)

    # return the parent of a given index i
    def getParent(self, i : int):
        return self.linkedlist.get(self.getParentIndex(i))

    # return the left child of a given index i
    def getLeftChild(self, i : int):
        return self.linkedList.get(self.getLeftChildIndex(i))

    # return the right child of a given index i
    def getRightChild(self, i : int):
        return self.linkedList.get(self.getRightChildIndex(i))

    # return the parent index of a given index i
    def getParentIndex(self, i : int):
        pIndex = (i - 1) // 2
        return pIndex

    # return the left child index of a given index i
    def getLeftChildIndex(self, i : int):
        lcIndex = i * 2 + 1
        return lcIndex

    # return the right child index of a given index i
    def getRightChildIndex(self, i : int):
        rtIndex = i * 2 + 2
        return rtIndex

    # insert into last position of cb-tree
    def insert(self, key):
        self.linkedList.insertTail(key)

    def delLast(self):
        i = self.size() - 1
        self.linkedList.remove(i)

    # swap two nodes
    def swap(self, i1, i2):
        self.linkedList.swap(i1, i2)

    # show this cbtree
    def show(self):
        self.linkedList.show()

    def print_tree(self):
        floor = 1
        p = self.getRoot()
        while (p != None):
            for i in range(0, floor):
                if p == None:
                    break
                print(p.key, end = " ")
                p = p.next
            floor *= 2
            print()