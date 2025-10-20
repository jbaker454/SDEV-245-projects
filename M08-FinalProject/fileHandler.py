import os

def fetch_file_safe(filePath: str):
  """
  Safely reads a text file.
  - Only allows reading files from a known safe directory.
  - Blocks path traversal (e.g., ../../secret.txt).
  """
  SAFE_DIR = os.path.abspath("safe_files")  
  os.makedirs(SAFE_DIR, exist_ok=True)      

  abs_path = os.path.abspath(os.path.join(SAFE_DIR, filePath))
  
  if not abs_path.startswith(SAFE_DIR):
    raise PermissionError("Unsafe file path detected.")

  if not os.path.isfile(abs_path):
    raise FileNotFoundError(f"File not found: {abs_path}")

  with open(abs_path, "r", encoding="utf-8") as f:
    text = f.read()

  return text


def fileHandlerMain(filePath:str):
  text: str = fetch_file_safe(filePath)
  return text