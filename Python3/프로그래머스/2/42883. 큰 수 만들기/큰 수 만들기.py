
def solution(number, k):
    answer = []
    for num in number:
        while k>0 and answer and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
        # print(answer) # 조인해야됨
        
    return ''.join(answer[:len(answer)-k])
