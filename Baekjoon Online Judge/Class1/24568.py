# regular - 8 cup cakes, samll - 3 cupcakes
# student - 28

def solution(r, s):
    total = r * 8 + s * 3
    answer = total - 28
    return answer

r = int(input()) # number of regular box
s = int(input()) # number of small box
print(solution(r, s))