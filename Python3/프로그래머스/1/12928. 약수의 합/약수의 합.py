def solution(n):
    answer = 0
    
    # 1부터 n까지 반복합니다. (range는 끝 숫자를 포함하지 않으므로 n + 1)
    for i in range(1, n + 1):
        # n을 i로 나누었을 때 나머지가 0이면 약수!
        if n % i == 0:
            answer += i  # 약수라면 정답에 더해줍니다.
            
    return answer