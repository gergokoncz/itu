class Variables {
	public static void main(String args[]){
		System.out.println("Variables");
		// declaration
		int a,b,c;
		float pi;
		double d;
		char e = 'v';
		// initialization
		pi = 3.14f;
		d = 20.22d;
		// example
		byte x;
		int y = 270;
		double z = 128.128;
		System.out.println("int converted to byte");
		x = (byte) y;
		System.out.println("y and x " + y + " " + x);
		System.out.println("double converted to int");
		y = (int) z;
		System.out.println("y and z " + y + " " + z);
		System.out.println("\ndouble converted to byte");
		x = (byte) z;
		System.out.println("x and z " + x + " " + z);
	}
}

class Guru99 {
	static int a = 1; //static variable
	int data = 99; // instance variable
	void method() {
		int b = 90; // local variable
	}
}
