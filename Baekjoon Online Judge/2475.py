def solution(p):
    total = 0
    for param in p:
        total += param ** 2
    answer = total % 10
    return answer

numList = list(map(int, input().split()))
print(solution(numList))
