import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = [i for i in range(1, 13)]
    result = []

    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N and sum(subset) == K:
            result.append(subset)

    count = len(result)

    print(f'#{tc} {count}')