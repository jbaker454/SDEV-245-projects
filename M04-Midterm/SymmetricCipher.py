import Verification

class Cipher():
  def __init__(self) -> None:
    pass

  verifyObj = Verification.verify()

  def determineMessage(self):
    message = input("input message here: ")
    return message

  def determineKey(self):
    key = input("input key number betweeen 1-100: ")
    verifiedInputProcess = Verification.verify.validateInputRange(self.verifyObj,key,[0,100])
    return verifiedInputProcess

  def encrypt(self, message:str, key):
    encryptedMessage = ""
    for char in message:
      code = ord(char)  
      encrypted_code = (code + key) % 1114112
      encryptedMessage = encryptedMessage + (chr(encrypted_code))
    return encryptedMessage

  def decrypt(self, message:str, key):
    decryptedMessage = ""
    for char in message:
      code = ord(char)  
      decrypted_code = (code - key) % 1114112
      decryptedMessage = decryptedMessage + (chr(decrypted_code))
    return decryptedMessage
  
  def encryptProcess(self):
    message = self.determineMessage()
    key = self.determineKey()
    if key == None:
      return None
    return self.encrypt(message,key)

  def decryptProcess(self):
    message = self.determineMessage()
    key = self.determineKey()
    if key == None:
      return None
    return self.decrypt(message,key)
