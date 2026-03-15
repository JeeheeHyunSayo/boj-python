import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    # 모든 사람의 키와 몸무게를 서로 비교하는 것

    people = []
    for _ in range(n):
        w, h = map(int, input().split())
        people.append((w, h))

    for w, h in people:
        rank = 1
        for ww, hh in people:
            if ww > w and hh > h:
                rank += 1
        print(rank, end=' ')


