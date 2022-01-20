#################################################
#
# 1051 번 숫자 정사각형 
# 구현 문제 2트
# 날짜 : 0120
# 유형 - 구현, 브루트포스
# 핵심 : 2차원 배열 범위 잘 다루기, N 또는 M이 클때 직사각형 모양 생각하기
# O(N^3)
################################################

import sys


# 입력 처리 
N, M = map(int, input().split())
arr = []
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    arr.append(list(temp))

# 주요 알고리즘 작성
# (놓치지 말 것) N이 클수도 있고, M이 클수도 있다.

def solution(N, M, arr):
    max_size = 0 
    width = 0
    min_side = min(N,M)
    
    # 시뮬레이션 범위
    run_status = True
    while run_status:
        
        if width == min_side:
            break

        for row in range(N - width): # row 
            for col in range(M - width): # col
                if row+width < N and col+width < M:
                    if arr[row][col] == arr[row][col+width] and arr[row][col] == arr[row+width][col] and arr[row][col] == arr[row+width][col+width]:
                        max_size = max(max_size, (width + 1) ** 2)
                        # current_size = width + 1
                        # if current_size > max_size:
                        #     max_size = current_size
                        #     width += 1                # width 를 여기서 증감 시키니까 문제가 있었다.
                        #     row = 0
                        #     col = 0
                else:
                    run_status = False
                    break
        width += 1        
    return max_size

print(solution(N,M, arr))
