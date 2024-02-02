import sys
sys.stdin = open('input.txt')

def search(start, end, target, count):
    center = (start + end) // 2
    if center == target:
        return count
    elif center > target:
        return search(start, center, target, count+1)
    else:
        return search(center, end, target, count+1)


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    start = 1

    count_A = search(start, P, Pa, 0)
    count_B = search(start, P, Pb, 0)

    print(f'#{tc}', end=' ')
    if count_A > count_B:
        print('B')
    elif count_A < count_B:
        print('A')
    else:
        print('0')