import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 카드 장수
    arr = list(map(int, input()))

    counts = [0] * 10

    for num in arr:
        counts[num] += 1

    number = 0
    for i in range(len(counts)):
        if counts[i] == max(counts):
            number = i

    print(f'#{tc} {number} {max(counts)}')