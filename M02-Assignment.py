from typing import TypedDict, Union, Optional, Literal
import base64

class SymmetricKey(TypedDict):
  kind: Literal["symmetric"]
  key: int

class RSAKeys(TypedDict):
  kind: Literal["rsa"]
  P: int
  Q: int
  e: int

class ABKeys(TypedDict):
  kind: Literal["ab"]
  A:int
  B:int

KeyTypes = Union[SymmetricKey, RSAKeys, ABKeys]

errors = [
  "invalid process",
  "invalid key",
]

processes = [
  "symetric encryption",
  "symetric decryption",
  "asymetric encryption",
  "asymetric decryption",
]

primeNumbersBeforeOneHundred = [
  2,3,5,7,11,13,17,19,23,
  29,31,37,41,43,47,53,59,
  61,67,71,73,79,83,89,97
]



def validateInputNumber(value: str):
  try:
    return float(value)  
  except ValueError:
    return None

def validateInputInt(value: str):
  try:
    return int(value) 
  except ValueError:
    return None

def validateInputProcess(inputProcess: str):
  process = validateInputInt(inputProcess)
  if not (process == None):
    if 0 <= process < len(processes):
      return process
  print(errors[0])
  return None

def validateInputPrimeNumber(value: str):
  intiger = validateInputInt(value)
  if intiger in primeNumbersBeforeOneHundred:
    return intiger
  print(errors[1])
  return None

def determineMessage():
  message = input("input message here: ")
  return message

def determineProcess():
  print("choose a process: {")
  for n in range(len(processes)):
    print(processes[n], " type ", n)
  inputProcess = input("} process number here: ")
  if not (validateInputProcess(inputProcess) == None):
    process = int(inputProcess)
    return process
  return None

def determineKeys(process: int) -> Optional[KeyTypes]:
  if process in (0, 1):
    key = validateInputInt(input("input encryption/decryption key: "))
    if key is None:
      return None
    return {"kind":"symmetric","key": key}

  elif process == 2:
    P = validateInputInt(input("input 1st Prime number 1-100 key: "))
    Q = validateInputInt(input("input 2nd Prime number 1-100 key: "))
    e = validateInputInt(input("input e key: "))
    if P is None or Q is None or e is None:
      return None
    return {"kind":"rsa","P": P, "Q": Q, "e": e}

  elif process == 3:
    A = validateInputInt(input("input private decryption key A: "))
    B = validateInputInt(input("input private decryption key B: "))
    if A is None or B is None:
      return None
    return {"kind":"ab","A": A, "B": B}

  return None

def symetricEncryption(message: str, keys: SymmetricKey):
  encryptedMessage = ""
  for char in message:
    code = ord(char)  
    encrypted_code = (code + keys["key"]) % 1114112
    encryptedMessage = encryptedMessage + (chr(encrypted_code))
  return encryptedMessage

def symetricDecryption(message: str, keys: SymmetricKey):
  decryptedMessage = ""
  for char in message:
    code = ord(char)  
    decrypted_code = (code - keys["key"]) % 1114112
    decryptedMessage = decryptedMessage + (chr(decrypted_code))
  return decryptedMessage

def asymetricEncryption(message: str, keys: RSAKeys):
  n = keys["P"] * keys["Q"]
  fancyN = (keys["P"] - 1) * (keys["Q"] - 1)
  d = pow(keys["e"], -1, fancyN)
  print("AB public keys are (", keys["e"], ", ",n,")")
  print("AB private keys are (", d, ", ",n,")")

  messageBytes = message.encode("utf-8")
  M = int.from_bytes(messageBytes, "big")
  blockSize = (n.bit_length() - 1) // 8
  blocks = [
    messageBytes[i:i + blockSize]
    for i in range(0, len(messageBytes), blockSize)
  ]
  M = [int.from_bytes(block, "big") for block in blocks]
  C = [pow(m, keys["e"], n) for m in M]

  cipher_bytes = b"".join(c.to_bytes(blockSize, "big") for c in C)
  encryptedMessage = base64.b64encode(cipher_bytes).decode("utf-8")

  return encryptedMessage

def asymetricDecryption(message: str, keys: ABKeys):
  blockSize = (keys["B"].bit_length() - 1) // 8

  cipher_bytes = base64.b64decode(message)

  C = [
    int.from_bytes(cipher_bytes[i:i+blockSize], "big")
    for i in range(0, len(cipher_bytes), blockSize)
  ]

  decryptedBlocks = [pow(c, keys["A"], keys["B"]) for c in C]

  decryptedBytes = b"".join(
    m.to_bytes(blockSize, "big") for m in decryptedBlocks
  )

  decryptedMessage = decryptedBytes.decode("utf-8")
  return decryptedMessage



def processMessage(message: str, process: int, keys: SymmetricKey | RSAKeys | ABKeys):
  if keys["kind"] == "symmetric":
    if process == 0:
      return symetricEncryption(message, keys) 
    elif process == 1:
      return symetricDecryption(message, keys)

  elif keys["kind"] == "rsa":
    if process == 2:
      return asymetricEncryption(message, keys) 

  elif keys["kind"] == "ab":
    if process == 3:
      return asymetricDecryption(message, keys) 

  return None

def main():
  message = determineMessage()
  process = determineProcess()
  if process == None:
    return  
  keys = determineKeys(process)
  if keys == None:
    return
  processedMessage = processMessage(message, process, keys)
  if processedMessage == None:
    return
  print("processedMessage: ", processedMessage)
main()