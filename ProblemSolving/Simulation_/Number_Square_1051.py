################################################
#
# 1051 번 숫자 정사각형 
# 구현 문제 
#
#
################################################
import sys

# 입력 처리하기 
N, M = map(int, input().split())
arr = []
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    arr.append(list(temp))

# 알고리즘 작성
# first step)
# > 정사각형 크기를 2 부터 row 값 만큼 늘려가며,
# > max값을 갱신시켜 간다 
# > index out of range 를 조심하자 

max_size = - 1
width = 1
while True:
    if N<M and width >= N:
        break
    elif N>M and width >= M:
        break

    for row in range(len(arr) - width):
        for col in range(len(arr[row]) - width):
            # xor 연산을 하면 좀 더 편하게 할 수 있지 않을까?
            # (반례) a ^ a ^ b ^ b 와 같으면 0으로 나와서 문제가 있다
            # xor 연산을 하고 그 이진수가 기존의 나와 같다면? 역시 X 
            # if int(arr[row][col]) & int(arr[row+width][col]) & int(arr[row][col+width]) & int(arr[row+width][col+width]) == int(arr[row][col]):
            if arr[row][col] == arr[row+width][col] and arr[row][col] == arr[row][col+width] and arr[row][col] == arr[row+width][col+width] :
                current_size = (width + 1)
                if current_size > max_size:
                    max_size = current_size
                    # 여기서 바로 width 를 증가시키고 다음 width 에 대해서 조사하여 계산량을 줄일 수도 있을 듯
                    width += 1
                    row = 0
                    col = 0
                    break
            # if width < row :
            #     width += 1
            #     row = 0
            #     col = 0
            # else:
            #     break

# 출력
print(max_size ** 2)
    

