import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))

    counts = [0] * 10

    for num in arr:
        counts[num] += 1

    cnt = 0
    idx = 0

    while idx < len(counts):
        if counts[idx] >= 3:
            cnt += 1
            counts[idx] -= 3
            continue
        idx += 1

    idx = 0
    while idx < len(counts) - 2:
        if counts[idx] >= 1 and counts[idx+1] >= 1 and counts[idx+2] >= 1:
            cnt += 1
            counts[idx] -= 1
            counts[idx+1] -= 1
            counts[idx+2] -= 1
            continue
        idx += 1

    print(f'#{tc}', end=' ')
    if cnt == 2:
        print('baby-gin')
    else:
        print('not baby-gin')