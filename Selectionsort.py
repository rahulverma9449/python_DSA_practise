def selectionSort(S):

    for i in range(len(S)):
        cur_index = i
        for j in range(i, len(S)):
            if S[cur_index] > S[j]:
                cur_index = j
        S[i],S[cur_index] = S[cur_index], S[i]
    return S

S = [3,2,1,5,4]
print(selectionSort(S))
