import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]

# 1-1. 대각선의 합
hap = 0

for i in range(5):
    # 좌상우하 : 0 0  1 1  2 2
    # 우상좌하 : 0 4 1 3 2 2
    hap += arr[i][i]
    hap += arr[i][4-i]

hap -= arr[2][2]

print(hap)

# 1-2. 이웃 요소와의 차의 절대값
result = [[0] * 5 for _ in range(5)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(5):
    for j in range(5):
        abs_hap = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                abs_hap += abs(arr[i][j] - arr[ni][nj])
        result[i][j] = abs_hap

for i in range(5):
    for j in range(5):
        print(result[i][j], end=' ')
    print()