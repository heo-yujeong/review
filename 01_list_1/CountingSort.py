arr = [0, 4, 1, 3, 1, 2, 4, 1]

counts = [0] * (max(arr) + 1) # 0 ~ 4까지 인덱스를 갖는 0 배열

# arr에 있는 값을 인덱스로 하는 counts배열에 +1
for num in arr:
    counts[num] += 1

# 누적한 값을 counts에
for i in range(1, len(counts)):
    counts[i] += counts[i-1]

sort_arr = [0] * len(arr)

# arr의 뒤에서 모든 요소를 하나씩 뽑아와서 자리 잡아줌!
for i in range(len(arr)-1, -1, -1):
    counts[arr[i]] -= 1
    sort_arr[counts[arr[i]]] = arr[i]

print(sort_arr)