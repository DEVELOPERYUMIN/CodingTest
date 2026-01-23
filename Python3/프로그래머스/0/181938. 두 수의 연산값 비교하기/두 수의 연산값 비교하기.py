def solution(a, b):
    concat = int(str(a) + str(b))   # a ⊕ b
    prod = 2 * a * b                # 2 * a * b
    return concat if concat >= prod else prod
