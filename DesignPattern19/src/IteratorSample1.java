import java.util.ArrayList;
import java.util.List;

public class IteratorSample1 {
    public static void main(String[] args){
        PrefectureListAggregate prefListAggregate = new PrefectureListAggregate();
        Iterator iterator = prefListAggregate.createIterator();
        prefListAggregate.add(new Prefecture("京都府", 26));
        prefListAggregate.add(new Prefecture("東京都", 13));
        prefListAggregate.add(new Prefecture("北海道", 1));
        prefListAggregate.add(new Prefecture("大阪府", 27));
        iterator.first();
        while ( ! iterator.isDone() ) {
            Prefecture pref = (Prefecture)iterator.getItem();
            System.out.println(pref.getName());
            iterator.next();
        }
    }
}

class Prefecture {
    private String name;
    private int number;
    public Prefecture(String name, int number) {
        this.name= name;
        this.number = number;
    }
    public String getName() {
        return name;
    }
    public int getPrice() {
        return number;
    }
}

interface Iterator {
    public void first();
    public void next();
    public boolean isDone();
    public Prefecture getItem();
}

class PrefectureListIterator implements Iterator {
    private PrefectureListAggregate aggregate;
    private int current;
    public PrefectureListIterator(PrefectureListAggregate aggregate) {
        this.aggregate = aggregate;
    }
    @Override
    public void first() {
        current = 0;
    }
    @Override
    public void next() {
        current += 1;
    }
    @Override
    public boolean isDone() {
        if (current >= aggregate.getNumberOfStock()) {
            return true;
        }
        else {
            return false;
        }
    }
    @Override
    public Prefecture getItem() {
        return aggregate.getAt(current);
    }
}

interface Aggregate {
    public Iterator createIterator();
}

class PrefectureListAggregate implements Aggregate {
    private List<Prefecture> list = new ArrayList<>();
    private int numberOfStock;
    @Override
    public Iterator createIterator() {
        return new PrefectureListIterator(this);
    }
    public void add(Prefecture pref) {
        list.add(pref);
        numberOfStock += 1;
    }
    public Prefecture getAt(int number) {
        return list.get(number);
    }
    public int getNumberOfStock() {
        return numberOfStock;
    }
}
