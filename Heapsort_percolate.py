def percolate_down(arr, start, end):
    pi = start
    l = 1
    r = 2

    while(l < end):
        mi = pi
        if arr[l] < arr[mi]:
            mi = l
        if r < end and arr[r] < arr[mi]:
            mi = r

        if mi == pi:
            break


        arr[mi], arr[pi] = arr[pi], arr[mi]
        pi = mi
        l = 2*pi + 1
        r = 2*pi + 2

    def heapSort(arr):

        n = len(arr)

        for i in range(n-1, -1 , -1):
            percolate_down(arr, i , n)

        for i in range(0,n-1):
            arr[0], arr[n-i-1] = arr[n-i-1], arr[0]
            percolate_down(arr,0 , n-i-1)

arr = [int(i) for i in input().split()]
heapSort(arr)
print(arr)