'''
앞자리를 가능한 한 크게 만드는선택이 항상 유리함 -> 그리디 


'''

def solution(number, k):
    stack = []

    for digit in number:
        # 1) 아직 지울 수 있고, 2) 스택에 뭔가 있고, 3) 마지막이 현재 digit보다 작으면
        # 마지막을 지워서 더 큰 digit 이 앞에 오게 만든다
        while True:
            # (1) k가 0이면 더 이상 지울 수 없음
            if k == 0:
                break
            # (2) 스택이 비어있으면 비교할 대상이 없음
            if len(stack) == 0:
                break
            # (3) 마지막 숫자가 현재 digit보다 크거나 같으면 지울 이유 없음
            last = stack[-1]
            if last >= digit:
                break

            # 위 break 조건들에 걸리지 않았다면 지움 
            stack.pop() 
            k -= 1

        # 현재 digit은 무조건 넣기
        stack.append(digit)

    # 끝까지 왔는데 k가 남으면 뒤에서 k개 제거
    result = stack[:len(stack) - k] 
    return ''.join(result)

# while 문이랑 같은코드 : while k>0 and answer and answer[-1]<num:
# 아직 지울 수 있고, 앞에 숫자가 있으며, 그 숫자가 지금 숫자보다 작다면 뒤에 온 더 큰 숫자를 앞으로 보내기 위해 앞의 작은 숫자를 계속 제거한다
