################################################
#
# 1920 번 수찾기
# 유형 : 문자열, 숫자 배열 탐색, 이진 탐색 O(log N) 
#
# 요약) N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#
# 풀이 
# - 입력 범위와 시간을 보아 
# - 예제 입력에서 입력으로 찾는 대상 리스트 개수, 리스트, 찾을 숫자 리스트 개수 찾을 숫자 리스트를 받는다.
################################################

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이진 탐색(Binary Serach) 구현하기
def solution(A, B):

    # 1. 대상 리스트를 먼저 정렬_오름차순
    A.sort() # O(NlogN) 시간 복잡도

    for b_val in B:
        # 설정
        isFound = False
        left = 0
        right = len(A)-1

        while left <= right : # 이진 탐색 O(log N)
            mid = (left + right) // 2  # 소수점 제거
            if A[mid] == b_val:
                print(1)
                isFound = True
                break
            elif A[mid] < b_val:
                left = mid + 1
            else:
                right = mid - 1 # -1 뺴먹지 말자 
        
        if not isFound:
            print(0)
        
solution(A,B) 