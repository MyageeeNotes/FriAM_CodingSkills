public class FactoryMethodTest {
    public static void main(String[] args) {
        // インスタンス生成
        Koujyou koujyou1 = new TvKoujyou();     // ＴＶを作成するKoujyouインスタンス
        Koujyou koujyou2 = new RadioKoujyou();  // Ｒａｄｉｏを作成するKoujyouインスタンス
        Seihin[] array = new Seihin[3];         // 作成した製品を格納する配列

        // 製品製造
        array[0] = koujyou1.create();   // koujyou1（ＴＶ）で製造
        array[1] = koujyou2.create();   // koujyou2（Radio）で製造
        array[2] = koujyou1.create();   // koujyou1（ＴＶ）で製造

        // 製品情報の表示
        for (int i = 0; i < array.length; ++i) {
            array[i].print();
        }
    }
}

// 工場クラス
abstract class Koujyou {
    // 製品の製造と登録
    public final Seihin create() {
        Seihin seihin = factoryMethod();
        touroku(seihin);
        return seihin;
    }
    public abstract Seihin factoryMethod();
    public abstract void touroku(Seihin s);
}

// 工場クラスから拡張したテレビ工場
class TvKoujyou extends Koujyou {
    public Seihin factoryMethod() { return new Television(); }
    public void touroku(Seihin s) {
        Television t = (Television) s;
        t.numberring(); t.setDate(Date.today());
    }
}
// 工場クラスから拡張したラジオ工場
class RadioKoujyou extends Koujyou {
    public Seihin factoryMethod() { return new Radio(); }
    public void touroku(Seihin s) {
        Radio r = (Radio) s; r.numberring();
    }
}

abstract class Seihin { public abstract void print(); }

class Television extends Seihin {
    private int tvSerialNumber;
    private String date;
    public void numberring() {
        tvSerialNumber = Counter.getTvNumber();
    }
    public void setDate(String date) { this.date = date; }
    public void print() {
        System.out.println("このテレビに関する情報:");
        System.out.println(" 製造番号:" + tvSerialNumber);
        System.out.println(" 製造年月日:" + date);
    }
}

class Radio extends Seihin {
    private int radioSerialNumber;
    public void numberring() {
        radioSerialNumber = Counter.getRadioNumber();
    }
    public void print() {
        System.out.println("このラジオに関する情報:");
        System.out.println(" 製造番号:" + radioSerialNumber);
    }
}

class Date {
    public static String today() {
        return "2004/01/20";
    }
}

class Counter {
    private static int tvNum = 100;
    private static int radioNum = 76;
    public static int getTvNumber() { return tvNum++; }
    public static int getRadioNumber() { return radioNum++; }
}