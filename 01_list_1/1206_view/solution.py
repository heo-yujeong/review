import sys
sys.stdin = open('input.txt')

for tc in range(1, 11): # 10개의 test case
    N = int(input()) # 건물의 개수
    height = list(map(int, input().split()))
    # print(height)

    result = 0

    for i in range(2, N-2):
        if height[i] > height[i-2] and height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i+2]:
            result += height[i] - max(height[i-2],height[i-1], height[i+1], height[i+2])

    print(f'#{tc} {result}')