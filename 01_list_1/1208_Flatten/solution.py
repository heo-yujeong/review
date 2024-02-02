import sys
sys.stdin = open('input.txt')

for tc in range(1, 11): # 10개의 test case
    N = int(input()) # 덤프 횟수
    num_of_box = list(map(int, input().split())) # 100개의 상자의 높이
    # print(num_of_box)

    for n in range(N): # 덤프 수행하는 횟수 동안
        # 가장 큰 값인 인덱스를 찾아 값을 -1
        # 가장 작은 값인 인덱스를 찾아 값을 +1
        num_of_box[num_of_box.index(max(num_of_box))] -= 1
        num_of_box[num_of_box.index(min(num_of_box))] += 1

    # 덤프 횟수만큼 수행 후 최고점과 최저점의 높이 차
    print(f'#{tc} {max(num_of_box) - min(num_of_box)}')