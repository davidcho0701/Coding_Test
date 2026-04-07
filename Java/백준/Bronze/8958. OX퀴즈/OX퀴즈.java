import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. 테스트 케이스 개수 입력
        int t = sc.nextInt();
        
        for (int i = 0; i < t; i++) {
            // 2. OX 문자열 읽기
            String s = sc.next();
            
            int totalScore = 0; // 최종 점수
            int currentConsecutive = 0; // 현재 연속된 O의 개수
            
            // 3. 문자열을 하나씩 탐색
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == 'O') {
                    currentConsecutive++; // O면 연속 횟수 증가
                    totalScore += currentConsecutive; // 증가된 값을 점수에 합산
                } else {
                    currentConsecutive = 0; // X면 연속 횟수 리셋
                }
            }
            
            // 4. 결과 출력
            System.out.println(totalScore);
        }
        
        sc.close();
    }
}