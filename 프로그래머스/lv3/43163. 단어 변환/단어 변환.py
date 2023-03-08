from collections import deque


def solution(begin, target, words):
    if target not in words: # target이 리스트에 없으면 오류
        return 0

    Q = deque()
    Q.append((begin, 0))

    while Q:
        x, answer = Q.popleft()

        for i in range(len(words)):
            cnt = 0
            for j in range(len(x)):
                if x[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:
                if words[i] == target:
                    return answer+1
                else:
                    Q.append((words[i], answer + 1))

    return 0    # target이 리스트에는 있었지만 변경 실패면 오류