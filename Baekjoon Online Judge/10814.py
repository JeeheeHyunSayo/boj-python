n = int(input())
people = []
for i in range(n):
    age, name = input().split()
    people.append((int(age), name, i))

people.sort(key=lambda x:(x[0], x[2])) # lambda 사용법
for age, name, i in people:
    print(age, name)