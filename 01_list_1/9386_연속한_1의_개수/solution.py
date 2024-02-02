import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수열의 길이
    arr = list(map(int, input())) +[0]

    result = [] # 1을 카운트 했을 때 길이 들을 저장
    count = 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            result.append(count)
            count = 0

    print(f'#{tc} {max(result)}')