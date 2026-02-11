def solution(n):
    if (n % 4 == 0) and (n % 100 != 0):
        return 1
    elif (n % 400 == 0):
        return 1
    else:
        return 0


if __name__  == '__main__':
    year = int(input())
    print(solution(year))