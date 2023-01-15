from LinkedHeap import LinkedHeap
import time


def testDelMin():
    cntList = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000]
    timeList = []
    timeList2 = []
    for cnt in cntList:
        lh = LinkedHeap()
        lh2 = LinkedHeap()
        elements = [cnt - i for i in range(0, cnt)]
        elements2 = [i for i in range(0, cnt)]
        # build heap
        for i in range(0, len(elements)):
            lh.insert(elements[i])
            lh2.insert(elements2[i])

        start = time.time()
        while not lh.isEmpty():
            lh.delMin()
        end = time.time()
        t = round(end - start, 2)
        timeList.append(t)
        print('linkedHeap max to min time cost', t, 's')

        start = time.time()
        while not lh2.isEmpty():
            lh2.delMin()
        end = time.time()
        t = round(end - start, 2)
        timeList2.append(t)
        print('linkedHeap min to max time cost', t, 's')
        print()
    print(timeList)
    print(timeList2)



def testInsert():
    cntList = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    timeList = []
    timeList2 = []
    for cnt in cntList:
        elements = [cnt - i for i in range(0, cnt)]
        # from max to min
        linkedHeap = LinkedHeap()
        start = time.time()
        for i in elements:
            linkedHeap.insert(i)
        end = time.time()
        t = end - start
        timeList.append(round(t, 2))
        print('linkedHeap time cost', t, 's')

        # from min to max
        elements2 = [i for i in range(0, cnt)]
        linkedHeap = LinkedHeap()
        start = time.time()
        for i in elements2:
            linkedHeap.insert(i)
        end = time.time()
        t = end - start
        timeList2.append(round(t, 2))
        print('linkedHeap time cost', t, 's')
    print(cntList)
    print(timeList)
    print(timeList2)

if __name__ == "__main__":
    testInsert()
    testDelMin()



