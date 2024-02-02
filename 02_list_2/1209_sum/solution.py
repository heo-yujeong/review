import sys
sys.stdin = open('input.txt')

for _ in range(10): # 10개의 test case
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        # 행의 합
        hap_r = 0
        for j in range(100):
            hap_r += arr[i][j]
        if hap_r > result:
            result = hap_r

        # 열의 합
        hap_c = 0
        for j in range(100):
            hap_c += arr[j][i]
        if hap_c > result:
            result = hap_c

        # 좌상 우하 대각선
        hap_dia_1 = 0
        hap_dia_1 += arr[i][i]

        # 우상 좌하 대각선
        hap_dia_2 = 0
        hap_dia_2 += arr[i][99-i]

        # 합 중의 가장 큰 값을 result로
        result = max(result, hap_dia_1, hap_dia_2)

    print(f'#{test_case} {result}')