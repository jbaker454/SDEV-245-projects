import Verification
import random
import base64

class Cipher():
  def __init__(self) -> None:
    pass

  @staticmethod
  def sieve(limit:int):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit+1, num):
                is_prime[multiple] = False
    
    for i in range(2, limit+1):
        if is_prime[i]:
            primes.append(i)
    return primes

  primeNumbersBeforeOneThousand = sieve(1000)

  verifyObj = Verification.verify()

  def generateRandomPrime(self):
    primeListNumber = random.randint(25,len(self.primeNumbersBeforeOneThousand)) 
    return self.primeNumbersBeforeOneThousand[primeListNumber]

  def determineMessage(self):
    message = input("input message here: ")
    return message

  def generateKeys(self):
     P = self.generateRandomPrime()
     Q = self.generateRandomPrime()
     e = 65537
     return {"P": P, "Q": Q, "e": e}

  def determineKeys(self):
    keyA = input("input private key A: ")
    keyB = input("input private key B: ")
    verifiedkeyA = Verification.verify.validateInputRange(self.verifyObj,keyA,[0,1000000])
    if verifiedkeyA == None:
       return None
    verifiedkeyB = Verification.verify.validateInputRange(self.verifyObj,keyB,[0,1000000])
    if verifiedkeyB == None:
       return None
    return {"a": verifiedkeyA, "b": verifiedkeyB}

  def encrypt(self, message:str, keys:dict[str,int]):
    n = keys["P"] * keys["Q"]
    fancyN = (keys["P"] - 1) * (keys["Q"] - 1)
    d = pow(keys["e"], -1, fancyN)
    print("AB public keys are (", keys["e"], ", ",n,")")
    print("AB private keys are (", d, ", ",n,")")

    messageBytes = message.encode("utf-8")
    M = int.from_bytes(messageBytes, "big")

    plainBlockSize = (n.bit_length() - 1) // 8
    cipherBlockSize = (n.bit_length() + 7) // 8

    blocks = [
      messageBytes[i:i + plainBlockSize]
      for i in range(0, len(messageBytes), plainBlockSize)
    ]
    M = [int.from_bytes(block, "big") for block in blocks]
    C = [pow(m, keys["e"], n) for m in M]

    cipher_bytes = b"".join(c.to_bytes(cipherBlockSize, "big") for c in C)
    encryptedMessage = base64.b64encode(cipher_bytes).decode("utf-8")

    return encryptedMessage

  def decrypt(self, message:str, keys:dict[str,int]):
    plainBlockSize = (keys["b"].bit_length() - 1) // 8
    cipherBlockSize = (keys["b"].bit_length() + 7) // 8

    cipher_bytes = base64.b64decode(message)

    C = [
      int.from_bytes(cipher_bytes[i:i+cipherBlockSize], "big")
      for i in range(0, len(cipher_bytes), cipherBlockSize)
    ]

    decryptedBlocks = [pow(c, keys["a"], keys["b"]) for c in C]

    decryptedBytes = b"".join(
      m.to_bytes(plainBlockSize, "big") for m in decryptedBlocks
    )

    decryptedMessage = decryptedBytes.decode("utf-8")
    return decryptedMessage
  
  def encryptProcess(self):
    message = self.determineMessage()
    keys = self.generateKeys()
    if keys == None:
      return None
    return self.encrypt(message,keys)

  def decryptProcess(self):
    message = self.determineMessage()
    keys = self.determineKeys()
    if keys == None:
      return None
    return self.decrypt(message,keys)