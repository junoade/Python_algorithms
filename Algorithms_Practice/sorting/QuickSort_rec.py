"""
    Quick Sort, 
    - 분할 정복 방식의 Comparison - base 알고리즘 

    핵심 알고리즘
    1. 피벗을 잡는다 
        - 가장 왼쪽, 가운데, 마지막 인덱스 또는 랜덤하게
    2. 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 이동시킴
        - 분할 함수 필요
    3. 다시 피벗을 잡음
    4. 반복. 언제까지? 더이상 분할 안될때 까지. ( 왼쪽에서 오는 low 인덱스와 오른쪽에서오는 j 인덱스가 만났을 때 )

"""
import sys
import time
sys.setrecursionlimit(10**7)


def quick_sort(arr, low, high):
    if low >= high: # low 인덱스와 high 인덱스의 위치가 서로 지나치게 되는 경우, 이미 정렬이 완료되어 return 
        return
    
    pivot = partition(arr, low, high)

    # recursive하게, 
    # pivot의 좌측부터 정렬
    quick_sort(arr, low, pivot-1) 
    # pivot의 우측를 정렬하여 마무리
    quick_sort(arr, pivot+1, high)


def partition(arr, low, high):
    pivot = arr[high] # 배열의 끝 부분의 키 값을 pivot으로
    idx = low   # swap이 일어난 자리를 저장하는 인덱서

    # partition 알고리즘
    for i in range(low, high):
        if arr[i] > pivot: # pivot 보다 큰 값이라면, 
            # swap
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    
    # partition 이후, 끝 부분(high)와 마지막 swap이 일어난 자리의 키 값을 swap
    arr[high], arr[idx] = arr[idx], arr[high]

    return idx 



# main 함수 부
file_path = "Algorithms_Practice\sorting\InputSample.txt"

arr = []
with open(file_path, 'r') as f:
    arr = f.readlines()

a = list(map(int, arr[0].split()))

print("Before Sorting...")

before = time.time()
print("After Sorting...")
quick_sort(a, 0, len(a)-1)

after = time.time()
print(a)
print("총 소요 시간 : %lf" % (after-before) )