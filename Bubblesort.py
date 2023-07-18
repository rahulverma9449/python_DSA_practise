# Bubble sort program
# def bubblesort(a):
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

#     return a
# def bubblesort(a):
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a


# a = input("Enter number of bubble")
#list = [3,5,2,7,9,1,10]
def sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


    return a


list2 = [2,5,7,8,1]

print(sort(list2))