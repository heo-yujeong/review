import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 색칠 영역 개수
    result = [[0]*10 for _ in range(10)]

    count = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                result[r][c] += color

    for i in range(10):
        for j in range(10):
            if result[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')