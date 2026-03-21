import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    layer = 1
    maxNum = 1

    while n > maxNum:
        maxNum  += 6 * layer
        layer += 1

    print(layer)