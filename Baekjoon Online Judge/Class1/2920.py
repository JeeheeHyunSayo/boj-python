import sys

def solution(first, nums):
    code = ''
    for num in nums[1:]:
        if first > num:
            code += '1'
        else:
            code += '2'

        first = num

    return code

if __name__ == '__main__':
    input = sys.stdin.readline
    nums = list(map(int, input().split()))
    first = nums[0]
    code = solution(first, nums)

    if ('1' in code) and ('2' in code): print("mixed") # 12, 21 -> 안될수도
    else:
        if first < nums[1] : print("ascending")
        elif first > nums[1]: print("descending")

