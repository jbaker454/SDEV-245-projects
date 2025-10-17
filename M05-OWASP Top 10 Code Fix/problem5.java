import java.sql.ResultSet;

// vurnability Injection
// issue username is concatinated with a direct result ffrom user

String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = '" + username + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);

// fixed version
// sanitized version using prepared statements

String username = request.getParameter("username");

String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, username);

ResultSet rs = pstmt.executeQuery();