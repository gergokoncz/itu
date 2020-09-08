class ArrayDemo2 {
	public static void passByReference(String a[]){
		a[0] = "changed";
	}
	public static void main(String args[]){
		String []b = {"Apple", "Mango", "Orange"};
		System.out.println("Before function call	" + b[0]);
		ArrayDemo2.passByReference(b);
		System.out.println("After function call	" + b[0]);
	}
}
