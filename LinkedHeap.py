from CBTree import CBTree
from LinkedList import LinkedList

class LinkedHeap():
    def __init__(self):
        self.cbt = CBTree()

    def isEmpty(self):
        return self.cbt.isEmpty()

    def size(self):
        return self.cbt.size()

    # return the minimum key in the heap
    def getMin(self):
        cbt = self.cbt
        if self.isEmpty():
            raise IndexError("heap is Empty")
        return cbt.getRoot().key

    # delete minimum of the heap and return its key
    def delMin(self):
        cbt = self.cbt
        if self.isEmpty():
            raise IndexError("heap is Empty")
        min = cbt.getKey(0)
        cbt.swap(0, cbt.size() - 1)
        cbt.delLast()
        self.sink(0)
        return min

    # insert at the end of the heap and reheapify
    def insert(self, key):
        cbt = self.cbt
        cbt.insert(key)
        self.swim(self.size() - 1)

    # top-down reheapify
    def sink(self, k : int):
        cbt = self.cbt
        while cbt.getLeftChildIndex(k) < self.size():
            lc = cbt.getLeftChildIndex(k)
            rc = lc + 1
            down = lc if rc >= self.size() or cbt.getKey(lc) < cbt.getKey(rc) else rc
            if cbt.getKey(k) < cbt.getKey(down):
                break
            else:
                cbt.swap(k, down)
                k = down

    # move a node at index k to the top of the heap
    def swim(self, k : int):
        cbt = self.cbt
        while (k > 0 and cbt.getKey(k) < cbt.getKey(cbt.getParentIndex(k))):
            cbt.swap(k, cbt.getParentIndex(k))
            k = cbt.getParentIndex(k)

    def show(self):
        self.cbt.print_tree()


def testLinkedList():
    ll = LinkedList()
    for i in range(10):
        ll.insertTail(i)
    # ll.swap(8, 0)
    ll.remove(0)
    ll.insert(4, 0)
    ll.insert(0, 20)
    ll.show()

def testInitCBTree():
    cbt = CBTree()
    for i in range(10):
        cbt.insert(i)
    cbt.swap(0, 8)
    return cbt

def testInitLinkedHeap():
    heap = LinkedHeap()
    for i in range(10):
        heap.insert(i)
    heap.insert(-10)
    heap.insert(100)
    heap.insert(-150)
    return heap

def testCBTree():
    cbt = testInitCBTree()
    cbt.show()
    cbt.print_tree()
    print(cbt.getLeftChild(3).key)
    print(cbt.getRightChild(3).key)


def testLinkedHeap():
    heap = testInitLinkedHeap()
    heap.show()
    while not heap.isEmpty():
        print(heap.delMin())
    print()

def drawLinkedHeap():
    heap = LinkedHeap()
    li = [8,  3, 7, 2, 6, 9, 1, 0, 5, 4]
    for i in li:
        heap.insert(i)
    heap.show()
    print()
    for i in range(3):
        heap.delMin()
    heap.show()


if __name__ == "__main__":
    testLinkedList()

    testCBTree()

    testLinkedHeap()

    drawLinkedHeap()
