public class SingletonTest {
    public static void main(String[] args) {
        Renban renban = Renban.getInstance();
        renban.getNumber();
        renban.print();

        Renban renban2 = Renban.getInstance();
        renban2.getNumber();
        renban2.print();

        Renban renban3 = Renban.getInstance();
        renban3.getNumber();
        renban3.print();
    }
}
class Renban {
    private static Renban jittai = new Renban();
    private int number;
    private Renban() {
        this.number = 0;
    }

    public static Renban getInstance() {
        return jittai;
    }
    public int getNumber() {
        this.number += 1;
        return this.number;
    }
    public void print(){
        System.out.println(String.format("%04d", this.number));
    }
}