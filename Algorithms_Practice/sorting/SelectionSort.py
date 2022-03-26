"""
    1. 정렬 되지 않은 부분에서 min 값의 index를 select!
    2. 정렬된 부분 집합의 오른쪽 원소와 swap!
    - 평균, 최악 O(n^2)
    - 제자리성 Yes
    - 안전성 No
"""
import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i;
        # 정렬 되지 않은 부분
        for j in range(i+1, len(arr)):
            # if there is smaller value than current min_Value
             if arr[min_idx] >= arr[j]:
                 min_idx = j
        
        # 정렬된 부분의 끝을 가르키는 i와 min_idx의 위치를 swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    

# arr = list(map(int, input().split()))
# file_path = "Algorithms_Practice\sorting\InputSample.txt"
file_path = "Algorithms_Practice/sorting/InputSample.txt"
arr = []
with open(file_path, 'r') as f:
    arr = f.readlines()
    
a = list(map(int, arr[0].split()))

print("Before Sorting...")

before = time.time()
print("After Sorting...")
selection_sort(a)
after = time.time()

print(a)
print("총 소요 시간 : %d" % (after-before) )