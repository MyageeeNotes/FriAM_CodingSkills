public class TheDogTest1 {

    public static void main(String[] args) {
        Dog elisabeth = new Dog();

        elisabeth.print();

        for (int cnt = 0; cnt < 7; cnt+=1){
            if (cnt < 4){
                elisabeth.roudou();
            }
            else {
                elisabeth.shokuji();
            }
            elisabeth.print();
        }
    }
}

class Dog {
    public static int STATE_TANOSHII = 0; // static変数群
    public static int STATE_FUTSUU = 1;
    public static int STATE_IRAIRA = 2;
    public static int STATE_BYOUKI = 3;

    private int state = STATE_TANOSHII; // 状態変数

    public void roudou() {
        if (state == STATE_TANOSHII) {
            state = STATE_FUTSUU;
        }
        else if (state == STATE_FUTSUU) {
            state = STATE_IRAIRA;
        }
        else if (state == STATE_IRAIRA) {
            state = STATE_BYOUKI;
        } else {
            // 状態遷移なし
        }
    }

    public void shokuji() {
        if (state == STATE_TANOSHII) {
            // 状態遷移なし
        }
        else if (state == STATE_FUTSUU) {
            state = STATE_TANOSHII;
        }
        else if (state == STATE_IRAIRA) {
            state = STATE_TANOSHII;
        }
        else if (state == STATE_BYOUKI){
            state = STATE_FUTSUU;
        }
    }

    public void print() {
        if (state == STATE_TANOSHII) System.out.println("楽しい状態");
        if (state == STATE_FUTSUU) System.out.println("普通状態");
        if (state == STATE_IRAIRA) System.out.println("いらいら状態");
        if (state == STATE_BYOUKI) System.out.println("病気状態");
    }
}
