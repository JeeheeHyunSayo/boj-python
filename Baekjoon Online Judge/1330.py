def solution(a, b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '=='

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solution(a, b))

