import java.sql.*;
import java.util.Scanner;

public class TestSQLi {
    public static void main(String[] args) throws Exception {
        Connection connection = DriverManager.getConnection("jdbc:h2:mem:test");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter username: ");
        String userInput = scanner.nextLine();   // user-controlled input

        String query = "SELECT * FROM users WHERE name = '" + userInput + "'";

        Statement stmt = connection.createStatement();
        stmt.executeQuery(query);   // SQL injection sink
    }
}
