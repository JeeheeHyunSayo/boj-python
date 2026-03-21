import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(3)]

# isdigit()  # 숫자인거 찾기
value = 0
for i in range(len(arr)):
    if arr[i].isdigit():
        value = int(arr[i]) - i

answer = value + 3
if answer % 3 == 0 and answer % 5 != 0:
    print("Fizz")
elif answer % 5 == 0 and answer % 3 != 0:
    print("Buzz")
elif answer % 5 == 0 and answer % 3 == 0:
    print("FizzBuzz")
else:
    print(answer)