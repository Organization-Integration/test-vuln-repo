public class Test {
    public static void main(String[] args) {
        String password = "admin123";  // hardcoded secret

        try {
            Runtime.getRuntime().exec("ls " + args[0]);  // command injection
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
