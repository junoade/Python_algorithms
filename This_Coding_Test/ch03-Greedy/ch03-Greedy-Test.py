def testCode(a, b):
    result = 0

    max_num = max(nums)
    nums.remove(max_num)
    second_num = max(nums)
    _k = 0
    for i in range(0, M):
        if K == _k:
            _k = 0
            result += second_num
        else:
            result += max_num
            _k += 1
    print(result)

def testJunhoCode1(a,b):
    answers = []
    firstMax = max(b)
    b.remove(firstMax)
    secondMax = max(b)

    cnt = 0
    for val in range(M):
        if(cnt <= K-1):
            answers.append(firstMax)
            cnt +=1
        else:
            answers.append(secondMax)
            cnt = 0
        
    # print(answers)
    print(sum(answers))


while(True):
    N, M, K = map(int, input().split())
    a = (N,M,K)
    nums = list(map(int, input().split()))
    b = nums
    # testCode(a,b)
    testJunhoCode1(a,b)