from asyncio import PriorityQueue


class stack:
    def __init__(self, size):
        self.size =  size
        self.arr = [0 for i in range(self.size)]
        self.top = -1

    def isEmpty(self):
        if self.top ==-1:
            return True
        return False


    def isFull(self):
        if self.top == self.size -1:
            return True
        return False


    def push(self,ele):
        if self.isFull() == True:
            print("Stack is full")
            return
        self.top += 1
        self.arr[self.top] = ele


    def pop(self, ele):
        if self.isEmpty() == True:
            print("Stack is empty")
            return
        ele = self.arr[self.top]
        self.top -= 1
        return ele

    def peek(self):
        if self.isEmpty() == True:
            print("Stack is empty!")
            return
        return self.array[self.top]

class queue:

    def __init__(self, size):
        self.s1 = stack(size)
        self.s2 = stack(size)



    def isEmpty(self):
        if self.s1.isEmpty() ==True:
            return True
        return False

    def isFull(self):

        return self.s1.isFull()

    def push(self, ele):
        if(self.isFull() ==True):
            print("Queue is full")
            return
        self.s1.push(ele)

    def pop(self):
        if self.isEmpty() ==True:
            print("Queue is empty  ")
            return

        while(self.s1.isEmpty() ==False):
            ele = self.s1.pop()
            self.s2.push(ele)

        result = self.s2.pop()

        while(self.s2.isEmpty() == False):
            ele = self.s2.pop()
            self.s1.push(ele)

        return result

class priorityQueue():

    def __init__(self):
        self.arr = []



    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False

    def push(self, ele):

        self.arr.append(ele)

        self.arr.sort(key=lambda x: x[1], reverse=True)

    def pop(self):

        if self.isEmpty() == True:
            print("priority queue is empty")
            return
        self.arr.pop(0)





q1 = queue(5)

q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)
q1.push(5)

q1.pop()
