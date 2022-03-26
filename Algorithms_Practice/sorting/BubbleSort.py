
from operator import truediv
import time


""" bubble sort

1. 인접한 원소끼리 대소 비교
2. swap
3. 정렬되지 않은 부분에 대해 반복

평균, 최악 시간 복잡도 O(N^2)
제자리성 yes
안정성 yes 

"""
def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size-1):
            # 오름차순 정렬
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# swap 안하면 break 하기 그렇게 빠르진 않았다.
def bubble_sort_better(arr):
    size = len(arr)

    for i in range(size):
        swap = False

        for j in range(size - 1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                
        if not swap:
            break





osX_filepath = "Algorithms_Practice/sorting/InputSample.txt"
arr = []
with open(osX_filepath, 'r') as f:
    arr = f.readline().rstrip()

a = list(map(int, arr.split()))

print("Before Sorting...")

before = time.time()
print("After Sorting...")
# bubble_sort(a)
bubble_sort_better(a)
after = time.time()

print(a)
print("총 소요 시간 : %d" % (after-before) ) # 기본 - 1트 307초 

