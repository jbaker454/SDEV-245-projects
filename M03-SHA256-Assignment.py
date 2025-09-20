startState = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
         0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

K = [
0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

def rotate(x:int, n:int): 
  return ((x >> n) | (x << (32 - n))) & 0xffffffff
def shift(x:int, n:int): 
  return x >> n

def choice(x:int, y:int, z:int): 
  #takes 3 0s and 1s and chooses the minority
  return (x & y) ^ (~x & z)
def majority(x:int, y:int, z:int): 
  #takes 3 0s and 1s and chooses the majority
  return (x & y) ^ (x & z) ^ (y & z)

def bigSigma0(x:int): 
  return rotate(x, 2) ^ rotate(x, 13) ^ rotate(x, 22)
def bigSigma1(x:int): 
  return rotate(x, 6) ^ rotate(x, 11) ^ rotate(x, 25)
def littleSigma0(x:int): 
  return rotate(x, 7) ^ rotate(x, 18) ^ shift(x, 3)
def littleSigma1(x:int): 
  return rotate(x, 17) ^ rotate(x, 19) ^ shift(x, 10)

def determineMessage():
  message = input("input message here: ")
  return message

def padByteMessage(byteMessage: bytes):
  byteMessageLength = len(byteMessage) * 8
  byteMessage += b'\x80'
  while ((len(byteMessage) * 8) % 512) != 448:
    byteMessage += b'\x00'
  byteMessage += byteMessageLength.to_bytes(8, 'big')
  return byteMessage

def processBlock(block: bytes, currentState: list[int]):
  W = [int.from_bytes(block[j:j+4], 'big') for j in range(0, 64, 4)]
  for t in range(16, 64):
    val = (littleSigma1(W[t-2]) + W[t-7] + littleSigma0(W[t-15]) + W[t-16]) & 0xffffffff
    W.append(val)

  a,b,c,d,e,f,g,h = currentState
  for t in range(64):
    T1 = (h + bigSigma1(e) + choice(e,f,g) + K[t] + W[t]) & 0xffffffff
    T2 = (bigSigma0(a) + majority(a,b,c)) & 0xffffffff
    h = g
    g = f
    f = e
    e = (d + T1) & 0xffffffff
    d = c
    c = b
    b = a
    a = (T1 + T2) & 0xffffffff

  newState = [(currentState[0]+a) & 0xffffffff, (currentState[1]+b) & 0xffffffff,
              (currentState[2]+c) & 0xffffffff, (currentState[3]+d) & 0xffffffff,
              (currentState[4]+e) & 0xffffffff, (currentState[5]+f) & 0xffffffff,
              (currentState[6]+g) & 0xffffffff, (currentState[7]+h) & 0xffffffff]
  return newState

def processMessage(message:str) -> str:
  byteMessage = message.encode("utf-8")
  byteMessage = padByteMessage(byteMessage)
  
  currentState = startState
  for i in range(0, len(byteMessage), 64):
    block = byteMessage[i:i+64]
    currentState = processBlock(block, currentState)

  processedMessage = ''.join(f'{i:08x}' for i in currentState)
  return processedMessage

def main():
  message = determineMessage()
  processedMessage = processMessage(message)
  print("processedMessage: ", processedMessage)
main()