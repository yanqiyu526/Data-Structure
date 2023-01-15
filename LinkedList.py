# node of linked list
class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    # return node at given index
    def get(self, i : int):
        if self.isEmpty():
            raise IndexError("list is Empty")
        p = self.head
        j = 0
        while (p != None and j < i):
            j += 1
            p = p.next
        if (j == i):
            return p
        else:
            return None

    # return key at given index
    def getKey(self, i : int):
        return self.get(i).key

    # return head of the linked list
    def getHead(self):
        return self.head

    def size(self):
        return self.size()

    def insertHead(self, key):
        self.insert(0, key)

    def insertTail(self, key):
        self.insert(self.size, key)

    # swap 2 nodes at given index
    def swap(self, i1, i2):
        if (i1 == i2):
            return
        # find left and right index between i1 and i2
        iMax = i1 if i1 > i2 else i2
        iMin = i1 if i1 < i2 else i2
        vMaxPre = self.get(iMax - 1)
        vMax = vMaxPre.next
        vMaxNext = vMax.next
        # if 2 node is near
        if iMax - iMin == 1:
            # if left node is head
            if iMin == 0:
                vMin = self.head
                vMin.next = vMaxNext
                vMax.next = vMin
                self.head = vMax
            else:
                vMinPre = self.get(iMin - 1)
                vMin = vMinPre.next
                vMinPre.next = vMax
                vMin.next = vMaxNext
                vMax.next = vMin
            # end swap
            return
        # if left node is head
        if iMin == 0:
            vMin = self.head
            vMinNext = vMin.next
            # swap
            self.head = vMax
            vMax.next = vMinNext
            vMaxPre.next = vMin
            vMin.next = vMaxNext
        else:
            vMinPre = self.get(iMin - 1)
            vMin = vMinPre.next
            vMinNext = vMin.next
            #swap
            vMinPre.next = vMax
            vMax.next = vMinNext
            vMaxPre.next = vMin
            vMin.next = vMaxNext

    # given node and key, insert a new node into given index
    def insert(self, index, key):
        node = Node(key)
        self.insertNode(index, node)

    # given node and index, insert the node into given index
    def insertNode(self, index, node):
        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return
        preNode = self.get(index - 1)
        if preNode != None:
            node.next = preNode.next
            preNode.next = node
        else:
            raise IndexError("fail to insert")
        self.size += 1

    # remove node at given index
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        preNode = self.get(index - 1)
        if preNode != None:
            delNode = preNode.next
            preNode.next = delNode.next
            self.size -= 1
            return delNode
        else:
            raise IndexError("cant delete")

    # print linked list
    def show(self):
        result = "head"
        current = self.head
        while current != None:
            key = current.key
            result = result + "--->" + str(key)
            current = current.next
        print(result)
        return result