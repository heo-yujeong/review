import sys
sys.stdin = open('input.txt')

N = int(input()) # 정수 개수
arr = list(map(int, input().split()))

for i in range(1, 1 << 10):
    subset = []
    for j in range(10):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 0:
        print('존재')
        break
else:
    print('존재하지 않음')