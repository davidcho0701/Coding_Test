def solution(lines):
    # 각 구간(길이 1)이 몇 번 덮였는지 저장할 딕셔너리
    counts = {}
    
    # 1. 3개의 선분을 하나씩 확인
    for start, end in lines:
        # 2. 선분이 지나는 단위 구간(i ~ i+1)을 카운트
        # start부터 end-1까지만 셉니다. (길이를 재야 하므로)
        for i in range(start, end):
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
                
    # 3. 2번 이상 겹친 구간의 개수(길이) 구하기
    answer = 0
    for count in counts.values():
        if count >= 2:
            answer += 1
            
    return answer