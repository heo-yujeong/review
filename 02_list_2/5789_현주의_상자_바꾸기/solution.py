import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 상자 개수, Q: 변경 횟수
    N, Q = map(int, input().split())
    box = [0] * (N + 1)

    for q in range(Q):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            box[i] = q + 1

    print(f'#{tc}', *box[1:])