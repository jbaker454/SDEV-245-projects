// vurnability Cryptographic Failures
// issue MD5 is vurnable to decryption breackthroughs

public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
}

// fixed version
// salted MD5 not totally secure but a quick fix agianst rainbow tables

public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(salt.getBytes());
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
}