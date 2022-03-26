"""
    Shell Sort 
    - Insertion Sort에 전처리 과정을 추가하여 단점을 보완함.
    - 일정 간격(gap)으로 떨어진 부분 배열을 나누어, 그 각각에 Insertion Sort를 적용 
    
    단점
    - 현재 삽입하고자 하는 키가 정렬 후에 도착할 자리에서 많이 벗어나 있더라도, 한번에 한자리 씩만 그곳에 접근할 수 밖에 없다는 단점

    1. gap을 정함 ( gap sequence, such as knuth's formula, Tokuda 또는 경험에 의한 Ciura Sequence 등등 )
    2. 각 간격별 부분 배열에 대해 삽입 정렬을 진행
    3. gap을 update
    4. gap == 1 일 때 까지 반복 

    평균 시간 복잡도 O(N log(N))
    knuth's formula에 의한 최악 시간 복잡도는 O(n^1.5) 
    in place 한 알고리즘 
    not stable 함.

"""
import math
import time

def shell_sort_my(arr):
    L = len(arr)
    k = int(math.log((2*L+1), 3))
    h = (3**k -1) // 2

    while h > 0 and k >= 0:
        for i in range(h, L):
            # insertion sort
            value = arr[i]
            j = i-h
            while j>=0 and arr[j] > value:
                arr[j+h] = arr[j]
                j-= h
            arr[j+h] = value
        k -= 1
        h = (3**k - 1) // 2

def shell_sort_knuth(arr):
    L = len(arr)
    h = 1
    # h 를 미리 증가 시켜놓을 필요가 있음
    while h < L:
        h = h * 3 + 1 

def shell_sort_original(arr):
    L = len(arr)
    h = L//2
    while h > 0:
        for i in range(h, L):
            # insertion sort
            value = arr[i]
            j = i-h
            while j >= 0 and arr[j] > value:
                arr[j+h] = arr[j]
                j -= h
            arr[j+h] = value
        h //=2


file_path = "Algorithms_Practice\sorting\InputSample.txt"

arr = []
with open(file_path, 'r') as f:
    arr = f.readlines()

a = list(map(int, arr[0].split()))

print("Before Sorting...")

before = time.time()
print("After Sorting...")
shell_sort_my(a)

# shell_sort_original(a)
after = time.time()
nanoTosec = 10 ** 9 

print(a)
# print("총 소요 시간 : %lf" % ((after-before)/nanoTosec) )
print("총 소요 시간 : %lf" % (after-before) )