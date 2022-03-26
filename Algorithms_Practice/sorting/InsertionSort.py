import time

""" Insertion Sort

1. 정렬된 부분, 정렬되지 않은 부분으로 구분한다
2. 정렬되지 않은 부분의 제일 왼쪽의 element와 정렬된 부분의 elements들을 확인하면서, 
3. 해당 위치에 삽입한다.

- 입력에 민감한 input sensitive 알고리즘 
- 평균/최악 시간 복잡도 O(N^2)
- 제자리성(in place) yes
- 안전성 (stability) yes

"""

def insertion_sort(arr):
    
    # arr[0] 은 insertion 하는 의미가 없으므로, arr[1] 부터 insertion 알고리즘을 반복
    for i in range(1, len(arr)):
        cursorKey = arr[i]
        
        # index에 대해 표현하기에 따라 1 만큼 부등식이 달라질 수 있음 off-by-one error 조심
        # shift 하는 방식
        j = i
        while j > 0 and arr[j-1] > cursorKey : # for j in range(i-1, 0, -1):
            arr[j] = arr[j-1] # 공간을 만들어줌
            j -= 1
        arr[j] = cursorKey

        
file_path = "Algorithms_Practice\sorting\InputSample.txt"
# file_path = "Algorithms_Practice/sorting/InputSample.txt"
arr = []
with open(file_path, 'r') as f:
    arr = f.readlines()
a = list(map(int, arr[0].split()))

print("Before Sorting...")

before = time.time()
print("After Sorting...")
insertion_sort(a)
after = time.time()

print(a)
print("총 소요 시간 : %d" % (after-before) )