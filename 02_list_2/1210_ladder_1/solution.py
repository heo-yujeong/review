import sys
sys.stdin = open('input.txt')

for _ in range(10): # 10개의 test case
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[0] * 100 for _ in range(100)] # 방문 여부 체크

    di = [0, 0, -1] # 좌 우 상
    dj = [-1, 1, 0]

    x = 99
    y = 0

    # 시작 지점
    for i in range(100):
        if arr[99][i] == 2:
            y = i

    while x != 0:
        for i in range(3):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[x][y] = 1
                x = ni
                y = nj

    print(f'#{test_case} {y}')
