abstract class Shape {
    final int b = 20;
    public void display() {
        System.out.println("This is display method");
    }
    abstract public void calculateArea();
}

public class Rectangle extends Shape {
    public static void main (String args[]) {
        Rectangle obj = new Rectangle();
        obj.display();
    }
    public void calculateArea(){}
}