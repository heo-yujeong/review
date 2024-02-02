import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 2, 3, 5, 7, 11으로 나누어 떨어지는지를 count하는 배열
    result = [0] * 5

    while True:
        if N % 2 == 0:
            result[0] += 1
            N //= 2
        elif N % 3 == 0:
            result[1] += 1
            N //= 3
        elif N % 5 == 0:
            result[2] += 1
            N //= 5
        elif N % 7 == 0:
            result[3] += 1
            N //= 7
        elif N % 11 == 0:
            result[4] += 1
            N //= 11

        if N == 1:
            break

    print(f'#{tc}', *result)
