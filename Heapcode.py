class Heap:
    def __init__(self):
        self.arr = []
    def add(self, ele):
        self.arr.append(ele)

        n = len(self.arr)
        ci = n-1
        while(ci > 0):
            pi = (ci -1)//2

            if self.arr[ci] < self.arr[pi]:
                self.arr[ci], self.arr[pi] = self.arr[pi], self.arr[ci]
                ci =pi
            else:
                break

    def remove(self):
        if len(self.arr) ==0:
            print("Heap is empty! cannot remove! ")
            return

        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        ele = self.arr[-1]
        self.arr.pop()


        pi = 0
        l = 2*pi +1
        r =2*pi +2

        n = len(self.arr)

        while(l < n):
            mi = pi
            if(self.arr[1] < self.arr[mi]):
                mi = 1

            if(r < n and self.arr[r] < self.arr[mi]):
                mi = r
            if mi == pi:
                break
            else:
                self.arr[mi],self.arr[pi] = self.arr[pi], self.arr[mi]
                pi = mi
                l = 2*pi + 1
                r = 2*pi +2
        return ele
    def display(self):
        print(self.arr)




h= Heap()
h.add(3)
h.add(7)
h.add(4)
h.add(2)
h.add(3)
h.add(1)


h.display()

h.remove()
h.display()


