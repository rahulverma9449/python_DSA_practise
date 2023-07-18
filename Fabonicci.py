def fib(n, arr):
    if n == 0 or n == 1:
        return n
    if arr[n] != None:
        return arr[n]
    arr[n] = fib(n-1, arr) + fib(n-2, arr)
    return arr[n]
n = int(input())
arr =  [None]*(n+1)
fib(n , arr)