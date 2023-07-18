def linear_search(num, key):
    for i in range(len(num)):
        if key == num[i]:
            return 'found at', i

    return "not found "


num = [2, 3, 6, 2, 4, 9, 7, 3, 5, 6, 1, 0]
key = 1


print(linear_search(num, key))