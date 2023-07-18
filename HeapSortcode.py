from Heapcode import  *
def heapSort(arr):

    h = Heap()
    for i in range(len(arr)):
        h.add(arr[i])

    for i in range(len(arr)):
        arr[i] = h.remove()

arr = [int(i) for i in input().split()]
h = Heap()
print(arr)


