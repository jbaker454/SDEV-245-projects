import re

txtPattern: str = r"^.*\.txt$"
inputPattern: str = r"[^\w.\-\\/]"

def sanitizeInput(input: str) -> str:
  """
  Removes leading/trailing spaces and potentially unsafe characters.
  Example: turns ' ../file.txt ' into 'file.txt'
  """           
  sanitizedInput = re.sub(inputPattern, "", input)  
  return sanitizedInput

def validateInput(sanitizedInput: str) -> bool:
  """
  Validates that the sanitized input matches the pattern.
  Returns True if valid, False otherwise.
  """
  return bool(re.match(txtPattern, sanitizedInput))


def InputHandlerMain(input:str):
  sanitizedInput: str = sanitizeInput(input)
  isValid: bool = validateInput(sanitizedInput)
  if isValid:
    return sanitizedInput
  else:
    raise ValueError(f"Invalid input: {sanitizedInput}")
