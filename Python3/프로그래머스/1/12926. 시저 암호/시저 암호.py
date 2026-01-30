'''
ord('A')=65
66 > B
a~z 
'''

def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ' '
            continue
        if ch.isupper():
            kk = ord('A')
        else:
            kk = ord('a')
        pos = ord(ch) - kk # 알파벳위치 0~25 
        pos = pos + n   # 위치 + n
        pos = pos % 26 # 알파벳 26개 
        answer += chr(pos + kk)  # 문자로 변환

    return answer


'''
같은 코드 string 에 아스키 있음 
from string import ascii_lowercase, ascii_uppercase

lower = list(ascii_lowercase)  # ['a' ... 'z']
upper = list(ascii_uppercase)  # ['A' ... 'Z']

def solution(s, n):
    result = ""

    for ch in s:
        if ch == " ":
            result += " "  # 공백은 그대로

        elif ch in lower:  # 소문자
            i = lower.index(ch)
            result += lower[(i + n) % 26]

        elif ch in upper:  # 대문자
            i = upper.index(ch)
            result += upper[(i + n) % 26]

    return result

''' 
