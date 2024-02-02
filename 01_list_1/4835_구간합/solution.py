import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 정수의 개수, M: 구간의 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    hap_list = []

    for i in range(N-M+1):
        hap = 0
        for j in range(i, i+M):
            hap += arr[j]
        hap_list.append(hap)

    print(f'#{tc} {max(hap_list) - min(hap_list)}')