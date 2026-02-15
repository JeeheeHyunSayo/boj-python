import sys


def solution1(string):
    print(string.count('0'))
    return

def solution2(string):
    for i in range(1, 10):
        print(string.count(str(i)))
    return


if __name__ == '__main__':
    input = sys.stdin.readline

    arr = []
    for _ in range(3):
        n = int(input())
        arr.append(n)

    num = 1
    for elem in arr:
        num *= elem

    string = str(num)
    solution1(string)
    solution2(string)


