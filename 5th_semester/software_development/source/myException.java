class myException {
    public static void main(String args[]) {
        try {
            throw new ExtraException(2);
        } catch (ExtraException e) {
            System.out.println(e);
        }
    }
}

class ExtraException extends Exception {
    int a ;
    ExtraException(int b) {
        a = b;
    }
    public String toString() {
        return ("Exception Number = " + a);
    }
}

