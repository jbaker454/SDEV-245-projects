import Verification
import SymmetricCipher
import AsymmetricCipher
import SHA256
import DigitalSigniture

verifyObj = Verification.verify()
SymmetricCipherObj = SymmetricCipher.Cipher()
AsymmetricCipherObj = AsymmetricCipher.Cipher()
SHA256Obj = SHA256.Cipher()
DigitalSignitureObj = DigitalSigniture.Signiture()

processes = [
  "symetric encryption",
  "symetric decryption",
  "asymetric encryption",
  "asymetric decryption",
  "create hash",
  "createDigitalSigniture",
  "verifyDigitalSigniture",
]

def determineProcess():
  print("choose a process: {")
  for n in range(len(processes)):
    print(processes[n], " type ", n)
  inputProcess = input("} process number here: ")
  verifiedInputProcess = Verification.verify.validateInputRange(verifyObj,inputProcess,[0,len(processes)])
  return verifiedInputProcess

def processMessage(process: int):
  
  if process == 0:
    return SymmetricCipherObj.encryptProcess()
  
  elif process == 1:
    return SymmetricCipherObj.decryptProcess()

  if process == 2:
    return AsymmetricCipherObj.encryptProcess()

  if process == 3:
    return AsymmetricCipherObj.decryptProcess()
  
  if process == 4:
    return SHA256Obj.createHash()

  if process == 5:
    return DigitalSignitureObj.signSigniture()
  
  if process == 6:
    return DigitalSignitureObj.verifySingiture()

  return None


def main():
  process = determineProcess()
  if process == None:
    return 
  processedMessage = processMessage(process)
  if processedMessage == None:
    return
  print("processedMessage: ", processedMessage)
main()