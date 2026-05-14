def solution(participant, completion):
    hash_dict = {}
    
    # 1. 참가자 명단을 딕셔너리에 넣고, 이름이 등장할 때마다 +1
    for p in participant:
        if p in hash_dict:
            hash_dict[p] += 1
        else:
            hash_dict[p] = 1
            
    # 2. 완주자 명단을 돌면서 딕셔너리에서 값(등장 횟수)을 -1
    for c in completion:
        hash_dict[c] -= 1
        
    # 3. 딕셔너리를 돌면서 값이 0이 아닌(즉, 1인) 사람을 찾음
    for key, value in hash_dict.items():
        if value > 0:
            return key