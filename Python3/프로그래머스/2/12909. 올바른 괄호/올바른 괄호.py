'''
def solution(s):
    pairs={'(':')','{':'}','[':']'}
    stack=[]
    for ch in s:
        if ch in "({[":
            answer= True
            return answer
        elif ch in")}]":
            if not stack:   #닫는 괄호인데 스택이 비어있으면 실패 
                return False
            if stack[-1]!=pairs[ch]: # stack[-1] > 최근에 열린괄호,스택 맨 위  
                return False
            


테스트 1
입력값 〉	"()()"
기댓값 〉	true
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	"(())()"
기댓값 〉	true
실행 결과 〉	테스트를 통과하였습니다.
테스트 3
입력값 〉	")()("
기댓값 〉	false
실행 결과 〉	테스트를 통과하였습니다.
테스트 4
입력값 〉	"(()("
기댓값 〉	false
실행 결과 〉	실행한 결괏값 true이 기댓값 false과 다릅니다.
'''


def solution(s):
    pairs={'(':')','{':'}','[':']'}
    stack=[]
    for ch in s:
        if ch in "({[":
            stack.append(ch)

        elif ch in")}]":
            if not stack:   #닫는 괄호인데 스택이 비어있으면 실패 
                return False
            if pairs[stack[-1]]!=ch: # stack[-1] > 최근에 열린괄호,스택 맨 위  
                return False
            else:
                stack.pop()
    return not stack # 반복 끝났는데 남아있으면 틀림 
            