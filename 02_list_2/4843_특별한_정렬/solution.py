import sys
sys.stdin = open('input.txt')

T = int(input())

def selectSort():
    for x in range(10):
        midx = x
        for y in range(x+1, N):
            if x % 2 == 1:
                if arr[midx] > arr[y]:
                    midx = y
            else:
                if arr[midx] < arr[y]:
                    midx = y
        arr[midx], arr[x] = arr[x], arr[midx]


for tc in range(1, T+1):
    N = int(input()) # 정수 갯수
    arr = list(map(int, input().split()))

    selectSort()
    print(f'#{tc}', *arr[:10])