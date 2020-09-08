import java.util.ArrayList;

class Test_ArrayList {

	public static void main(String args[]) {
		// creating  a generic arrayList
		ArrayList<String> arlTest = new ArrayList<String>();
		// size of arraylist
		System.out.println("Size of ArrayList at creation: " + arlTest.size());
		// add some stuff
		arlTest.add("D");
		arlTest.add("U");
		arlTest.add("K");
		arlTest.add("E");
		// size of arraylist
		System.out.println("Size of ArrayList after adding elements: " + arlTest.size());
		// display all contents of arrayList
		System.out.println("List of all elements: "+ arlTest);

		// remove elements
		arlTest.remove("D");
		System.out.println("See contents after removing one element: " + arlTest);

		// remove element by index
		arlTest.remove(2);
		System.out.println("See contents after removing one element by index: " + arlTest);
		// size of arraylist
		System.out.println("Size of ArrayList after removing: " + arlTest.size());
		// see content
		System.out.println("See contents after removing two elements: " + arlTest);

		// check if contains stuff
		System.out.println(arlTest.contains("K"));
	}
}
