import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N * N 달팽이
    result = [[0] * N for _ in range(N)] # 달팽이 출력
    num = 1 # 달팽이를 채울 수

    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    d_idx = 0 # 방향 인덱스

    x = y = 0
    result[x][y] = num
    num += 1

    while num <= N**2:
        ni = x + di[d_idx]
        nj = y + dj[d_idx]
        if 0 <= ni < N and 0 <= nj < N and result[ni][nj] == 0:
            x = ni
            y = nj
            result[x][y] = num
            num += 1
        else:
            d_idx += 1
            if d_idx == 4:
                d_idx = 0

    print(f'#{tc}')
    for res in result:
        print(*res)