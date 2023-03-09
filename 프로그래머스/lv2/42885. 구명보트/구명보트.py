from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    Q = deque(people)
    while len(Q) > 1:
        if Q[0] + Q[-1] <= limit:
            Q.popleft()
        answer += 1
        Q.pop()
    if Q:
        answer += 1
    return answer