arr = [64, 25, 10, 22, 11]

def SelectionSort(lst):
    for i in range(len(lst)):
        minIdx = i
        for j in range(i+1, len(lst)):
            if lst[minIdx] > lst[j]:
                minIdx = j
        lst[i], lst[minIdx] = lst[minIdx], lst[i]

    return lst

sort_arr = SelectionSort(arr)

print(sort_arr)