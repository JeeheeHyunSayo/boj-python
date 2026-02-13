# 아스키코드 : ord('알파벳'), chr(숫자)
import sys
input = sys.stdin.readline

s = input().rstrip()
print(ord(s))