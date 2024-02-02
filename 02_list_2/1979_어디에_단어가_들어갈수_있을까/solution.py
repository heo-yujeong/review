import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 단어퍼즐 길이(N*N), K:단어의 길이
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    puzzle_t = list(map(list, zip(*puzzle))) # 전치행렬
    N += 1

    result = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
               cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

        for j in range(N):
            if puzzle_t[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')