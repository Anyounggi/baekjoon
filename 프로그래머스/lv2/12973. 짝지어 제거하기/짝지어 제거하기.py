def solution(s):
    stack = []
    for i in s:
        if not stack or (stack and stack[-1] != i):
            stack.append(i)
        else:
            stack.pop()

    if stack:
        answer = 0
    else:
        answer = 1

    return answer