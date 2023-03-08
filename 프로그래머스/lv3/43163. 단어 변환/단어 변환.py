from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    Q = deque()
    Q.append((begin, 0))
    
    while Q:
        x, answer = Q.popleft()
        if x == target:
            return answer
        
        for i in range(len(words)):
            cnt = 0
            for j in range(len(x)):
                if x[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:
                Q.append((words[i], answer+1))
    
    return 0