import SHA256
import Verification

class Signiture ():
  def __init__(self) -> None:
    pass

  verifyObj = Verification.verify()
  SHA256Obj = SHA256.Cipher()

  def determineHash(self):
    message = input("input hash here: ")
    return message

  def determineKeys(self):
    keyA = input("input private key A")
    keyB = input("input private key B")
    verifiedkeyA = Verification.verify.validateInputRange(self.verifyObj,keyA,[0,1000^2])
    if verifiedkeyA == None:
       return None
    verifiedkeyB = Verification.verify.validateInputRange(self.verifyObj,keyB,[0,1000^2])
    if verifiedkeyB == None:
       return None
    return {"a": verifiedkeyA, "b": verifiedkeyB}

  def signHash(self, hashedMessage:int, privateKey:dict[str,int]):
    digitalSigniture = (hashedMessage ^ privateKey["A"]) % privateKey["B"]
    digitalSigniture = hex(digitalSigniture)
    return digitalSigniture

  def getHashMessage(self):
    digest = bytes.fromhex(self.SHA256Obj.createHash())
    hashedMessage = int.from_bytes(digest, byteorder='big')
    return hashedMessage

  def createDigitalSingiture(self):
    hashedMessage = self.getHashMessage()
    privateKey = self.determineKeys()
    if privateKey == None:
      return
    digitalSigniture = self.signHash(hashedMessage, privateKey)
    return digitalSigniture

  def signSigniture(self):
    digitalSigniture = self.createDigitalSingiture()
    if digitalSigniture == None:
      return
    return digitalSigniture
    
  def verifySingiture(self):
    possibleDigitalSigniture = self.determineHash()
    digitalSigniture = self.createDigitalSingiture()
    if possibleDigitalSigniture == digitalSigniture:
      return ("signiture veryified")
    else:
      return ("signiture missmatch")
