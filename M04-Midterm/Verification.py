class verify():
  def __init__(self) -> None:
     pass
     
  errors = [
    "invalid input",
    "invalid intiger",
    "invalid range",
  ]

  def validateInputNumber(self,value: str):
    try:
      return float(value)  
    except ValueError:
      print(self.errors[0])
      return None

  def validateInputInt(self,value: str):
    try:
      return int(value) 
    except ValueError:
      print(self.errors[1])
      return None

  def validateInputRange(self,value:str ,range: list[int]):
    Intvalue = self.validateInputInt(value)
    if not (Intvalue == None):
      if range[0] <= Intvalue <= range[1]:
        return Intvalue
      print(self.errors[2])
    return None