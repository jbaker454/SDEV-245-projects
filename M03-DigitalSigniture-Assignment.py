import hashlib
from typing import TypedDict, Literal
import base64

class ABKeys(TypedDict):
  kind: Literal["ab"]
  A:int
  B:int

def validateInputInt(value: str):
  try:
    return int(value) 
  except ValueError:
    return None

def determineMessage():
  message = input("input message here: ")
  return message

def determineSingitureMessage():
  message = input("input signiture here: ")
  return message

def hashMessage(message:str):
  byteMessage = message.encode("utf-8")
  hashObject = hashlib.sha256(byteMessage)
  digest = hashObject.digest()
  hashedMessage = int.from_bytes(digest, byteorder='big')
  return hashedMessage

def determineKeys() -> ABKeys | None:
  A = validateInputInt(input("input private decryption key A: "))
  B = validateInputInt(input("input private decryption key B: "))
  if A is None or B is None:
    return None
  return {"kind":"ab","A": A, "B": B}

def signHash(hashedMessage:int, privateKey: ABKeys):
  digitalSigniture = (hashedMessage ^ privateKey["A"]) % privateKey["B"]
  digitalSigniture = hex(digitalSigniture)
  return digitalSigniture

def createDigitalSingiture(message:str):
  hashedMessage = hashMessage(message)
  privateKey = determineKeys()
  if privateKey == None:
    return
  digitalSigniture = signHash(hashedMessage, privateKey)
  return digitalSigniture
  

def main():
  choice = input("sign or veryify:")
  if choice == "sign":
    message = determineMessage()
    digitalSigniture = createDigitalSingiture(message)
    if digitalSigniture == None:
      return
    print("digitalSigniture: (", message,", ", digitalSigniture, ")")
  elif choice == "veryify":
    message = determineMessage()
    possibleDigitalSigniture = determineSingitureMessage()
    digitalSigniture = createDigitalSingiture(message)
    if possibleDigitalSigniture == digitalSigniture:
      print("signiture veryified")
    else:
      print("signiture missmatch")
  else:
    return
main()