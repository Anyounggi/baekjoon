def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == '(':
                stack.append(s[i])
            else:
                return False
        else:
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
                
    if stack:
        return False
    elif not stack:
        return True