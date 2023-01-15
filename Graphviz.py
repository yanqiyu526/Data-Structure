from graphviz import Digraph
from LinkedHeap import LinkedHeap

def drawLinkedHeap(heap : LinkedHeap, fileName):
    dot = Digraph()
    for i in range(0, heap.size()):
        dot.node(str(heap.cbt.getKey(i)))
    for i in range(0, heap.size()):
        cbt = heap.cbt
        if cbt.getLeftChildIndex(i) < cbt.size():
            dot.edge(str(cbt.getKey(i)), str(cbt.getLeftChild(i).key))
        if cbt.getRightChildIndex(i) < cbt.size():
            dot.edge(str(cbt.getKey(i)), str(cbt.getRightChild(i).key))
    dot.format = 'png'
    dot.view(filename=fileName, directory='./heapImg')

def testDotLinkedHeap():
    heap = LinkedHeap()
    li = [8, 3, 7, 2, 6, 9, 1, 0, 5, 4]
    for i in li:
        heap.insert(i)
    drawLinkedHeap(heap, "LinkedHeap_0")
    heap.delMin()
    drawLinkedHeap(heap, "LinkedHeap_1")
    heap.insert(-1)
    drawLinkedHeap(heap, "LinkedHeap_2")


if __name__ == "__main__":
    testDotLinkedHeap()