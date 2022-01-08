def solution(line):
    stack = []
    for i in range(0,len(line)):
        if stack and line[i] == ')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(line[i])
    if stack:
        return False
    else :
        return True

T = int(input())

while T:
    a = input()
    if solution(a):
        print("YES")
    else:
        print("NO")
    T -= 1

