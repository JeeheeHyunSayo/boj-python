import sys

input = sys.stdin.readline

n = int(input()) # 정수의 개수
# arr = list(map(int, input().split())) # 입력의 크기가 매우 클 경우 메모리를 많이 사용하게 됨
# print(min(arr), max(arr))

# 메모리 개선 버전
nums = map(int, input().split()) # map은 리스트가 아니라 이터레이터를 반환
first = next(nums) # 이터레이터에서 다음 값을 하나 꺼내는 함수 (하나만 꺼내는거임) 
min_val = first
max_val = first

for num in nums:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(min_val, max_val)