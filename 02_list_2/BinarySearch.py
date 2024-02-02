def BinarySearch(lst, start, end, key):
    if start > end:
        return None
    center = (start + end) // 2
    if lst[center] == key:
        return center
    elif lst[center] > key:
        return BinarySearch(lst, start, center-1, key)
    else:
        return BinarySearch(lst, center+1, end, key)



arr = [2, 4, 7, 9, 11, 19, 23]
searchNum = [7, 20]

for snum in searchNum:
    idx = BinarySearch(arr, 0, len(arr)-1, snum)
    if idx:
        print(f'{idx}번째에 값이 있습니다.')
    else:
        print('값을 찾을 수 없습니다.')