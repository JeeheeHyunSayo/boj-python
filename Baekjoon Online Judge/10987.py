def solution(s):
    answer = 0
    # 주의 문자열 순회를 안하면 두 개 이상의 같은 모음의 카운트가 안됨 
    for string in s:
        if 'a' == string: answer += 1
        if 'e' == string: answer += 1
        if 'i' == string: answer += 1
        if 'o' == string: answer += 1
        if 'u' ==  string: answer += 1
    return answer

s = input()
print(solution(s))