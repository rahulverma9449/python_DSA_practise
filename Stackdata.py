def push(num, n):
    num.append(n)
    return num
def pop(num):
    if isEmpty(num):
        print("Stack is not Empty")
        return False
    else:
        print("Stack is Empty")
        num.pop()
        return num

def isEmpty(num):
    if not num:
        return True
    else:
        return False

num = []
push(num, 2)
push(num, 5)
push(num, 3)
push(num, 8)
pop(num)
pop(num)
pop(num)
pop(num)

print(num)
