import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr_one = []
for a in arr:
    arr_one += a

for i in range(len(arr_one)):
    min_idx = i
    for j in range(i+1, len(arr_one)):
        if arr_one[min_idx] > arr_one[j]:
            min_idx = j
    arr_one[i], arr_one[min_idx] = arr_one[min_idx], arr_one[i]


result = [[0] * 5 for _ in range(5)]

di = [0, 1, 0, -1] # 우 하 좌 상
dj = [1, 0, -1, 0]
d_idx = 0 # 방향 인덱스

x = y = 0
idx = 0
result[x][y] = arr_one[idx]
idx += 1

while idx < N**2:
    ni = x + di[d_idx]
    nj = y + dj[d_idx]
    if 0 <= ni < N and 0 <= nj < N and result[ni][nj] == 0:
        x = ni
        y = nj
        result[x][y] = arr_one[idx]
        idx += 1
    else:
        d_idx += 1
        if d_idx == 4:
            d_idx = 0

for res in result:
    print(*res)