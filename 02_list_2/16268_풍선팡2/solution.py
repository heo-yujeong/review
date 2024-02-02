import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    max_count = 0

    for i in range(N):
        for j in range(M):
            hap = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    hap += arr[ni][nj]
            if hap > max_count:
                max_count = hap

    print(f'#{tc} {max_count}')