import java.util.Scanner;

public class ct_2562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int max = 0; // 최댓값을 저장할 변수
        int index = 0; // 몇 번째인지 저장할 변수

        // 9개의 숫자가 주어지므로 9번 반복합니다.
        for (int i = 1; i <= 9; i++) {
            System.out.println("9번째까지의 숫자들을 차례로 입력하세요. \n" + "숫자를 입력하세요 (" + i + "번째): ");
            int num = sc.nextInt();

            // 입력받은 숫자(num)가 현재 최댓값(max)보다 크면 갱신
            if (num > max) {
                max = num;
                index = i; // 현재 몇 번째(i)인지 저장
            }
        }

        // 결과 출력
        System.out.println(max);
        System.out.println(index);

        sc.close();
    }
}