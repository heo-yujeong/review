import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 버스 노선 개수
    bus_info = [list(map(int, input().split())) for _ in range(N)] # 버스 노선 정보
    P = int(input()) # 정류장 개수
    C = [int(input()) for _ in range(P)]# 버스 정류장 번호

    counts = [0] * P

    for bus in bus_info:
        for i in range(len(C)):
            if bus[0] <= C[i] <= bus[1]:
                counts[i] += 1

    print(f'#{tc}', *counts)



