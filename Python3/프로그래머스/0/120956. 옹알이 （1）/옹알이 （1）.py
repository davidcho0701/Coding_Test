def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for speakable in can_speak:
            # 발음할 수 있는 단어가 포함되어 있다면 공백으로 치환
            # ""(빈 문자열)이 아닌 " " (공백)으로 치환하는 이유는 
            # 단어가 합쳐져서 새로 발음 가능한 단어가 되는 것을 방지하기 위함입니다.
            if speakable in word:
                word = word.replace(speakable, " ")
        
        # 모든 치환이 끝난 후, 공백을 제거했을 때 아무것도 남지 않는다면 발음 가능한 단어
        if word.strip() == "":
            answer += 1
            
    return answer

