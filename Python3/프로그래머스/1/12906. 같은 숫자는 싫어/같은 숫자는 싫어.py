# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if arr[i]!=arr[i-1]:
#             answer.append(arr[i])
#     return answer

'''
테스트 1
입력값 〉	[1, 1, 3, 3, 0, 1, 1]
기댓값 〉	[1, 3, 0, 1]
실행 결과 〉	실행한 결괏값 [3,0,1]이 기댓값 [1,3,0,1]과 다릅니다.
테스트 2
입력값 〉	[4, 4, 4, 3, 3]
기댓값 〉	[4, 3]
실행 결과 〉	테스트를 통과하였습니다.
'''

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0 or arr[i]!=arr[i-1]:  # 첫번째 원소일 경우에 추가 
            answer.append(arr[i])
    return answer
