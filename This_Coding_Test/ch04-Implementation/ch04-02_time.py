####################################
#
#   이코테 ch04 - 02 시각
#   정수 N 이 입력되면 00시 00분 00 초 부터 N 시 59분 59초 까지 모든 시각 중에서 
#   3 이 하나라도 포함되는 경우의 수를 구하여라 
#   
#   - Brute Force 방식 구현문제 
# 
####################################
import time

N = int(input())

def solution(n):
    cnt = 0
    div = 60
    start = time.time()

    for i in range(n+1):
        for min in range(0, div):
            for sec in range(0, div):
                # 가독성이 좋지 않다. 근데 시간은 더 빠르네 
                #if(sec // 10 == 3 or sec % 10 == 3 or min // 10 == 3 or min % 10 == 3 or i // 10 == 3 or i % 10 == 3):
                #    cnt +=1

                # 파이썬의 in 연산자를 문자열에 대해 써보자 
                if '3' in str(i) + str(min) + str(sec):
                    cnt +=1
    print(cnt)
    end = time.time()
    print(end - start)

def soultion2(n):
    # 초 단위로 변환해서 해볼수도 있을까? 
    pass

solution(N)

