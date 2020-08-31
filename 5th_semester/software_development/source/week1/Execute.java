// Class declaration

class Dog {
	// instance variables
	String breed;
	String size;
	int age;
	String color;

	// method 1
	public String getInfo() {
		return ("Breed is: " + breed + " Size is:" + size + " Age is:" + age + "color is: " + color);
	}
}

public class Execute{
	public static void main(String args[]){
		Dog maltese = new Dog();
		maltese.breed = "Maltese";
		maltese.size = "small";
		maltese.age = 2;
		maltese.color = "white";
		System.out.println(maltese.getInfo());
	}
}
