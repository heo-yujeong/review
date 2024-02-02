import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 최대 이동 정류장 수, N: 종점, M: 충전기 설치된 정류장 개수
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 번호
    station = list(map(int, input().split()))

    current = 0 # 현재 위치(처음은 0)
    count = 0 # 충전 횟수

    while current + K < N:
        for step in range(K, 0, -1):
            if current + step in station:
                current += step
                count += 1
                break
        else:
            count = 0
            break

    print(f'#{tc} {count}')