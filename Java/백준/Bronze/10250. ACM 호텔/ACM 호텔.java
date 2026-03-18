import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 테스트 케이스 개수 입력
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int H = sc.nextInt(); // 호텔의 층수
            int W = sc.nextInt(); // 각 층의 방 수
            int N = sc.nextInt(); // 몇 번째 손님

            int floor; // 배정될 층수
            int roomNum; // 배정될 호수

            if (N % H == 0) {
                // N이 H의 배수라면 무조건 꼭대기 층
                floor = H;
                roomNum = N / H;
            } else {
                // 그 외에는 나머지가 층수, 몫+1이 호수
                floor = N % H;
                roomNum = (N / H) + 1;
            }

            // 출력 형식: 층수는 그대로, 호수는 두 자리로 맞춰서 출력
            // printf의 %d는 정수, %02d는 두 자리 숫자로 맞추고 빈칸은 0으로 채움
            System.out.printf("%d%02d\n", floor, roomNum);
        }
    }
}