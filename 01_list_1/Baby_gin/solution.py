import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))

    counts = [0] * 10

    for num in arr:
        counts[num] += 1

    cnt_run = 0
    cnt_triplet = 0

    for i in range(len(counts)-2):
        if counts[i] == 3:
            cnt_triplet += 1
            counts[i] -= 3
        elif counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            cnt_run += 1
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1

    print(f'#{tc}', end=' ')
    if cnt_run + cnt_triplet == 2:
        print('baby-gin')
    else:
        print('not baby-gin')