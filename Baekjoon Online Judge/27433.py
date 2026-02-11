def solution(num):
    answer = 1
    if num == 0: return answer
    for n in range(1, num+1): # 범위 셋팅 틀리지 마시오...
        answer *= n
    return  answer

num = int(input())
print(solution(num))