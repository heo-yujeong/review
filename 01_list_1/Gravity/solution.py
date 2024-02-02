import sys
sys.stdin = open('input.txt')

N = int(input()) # 상자가 놓인 가루 칸수
height = list(map(int, input().split()))

result = 0

for i in range(N-1):
    count = 0
    for j in range(i, N):
        # i 이후의 박스 중 i의 높이보다 낮으면 count + 1
        if height[i] > height[j]:
            count += 1
    # max count를 result에 넣기
    if count > result:
        result = count

print(result)