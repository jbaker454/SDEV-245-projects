import inputHandler
import fileHandler
import patternHandler

def main():
  rawInput = input("Enter file path or filename: ").strip()
  if not rawInput:
    print("No input provided. Exiting.")
    return

  try:
    validatedInput: str = inputHandler.InputHandlerMain(rawInput)
  except Exception as e:
    print(f"[Input Error] Failed to process input: {e}")
    return

  try:
    fileText: str = fileHandler.fileHandlerMain(validatedInput)
  except FileNotFoundError:
    print("[File Error] File not found.")
    return
  except PermissionError:
    print("[File Error] Access denied.")
    return
  except Exception as e:
    print(f"[File Error] Unexpected error: {e}")
    return

  try:
    patternName: str | None = patternHandler.patternHandlerMain(fileText)
  except Exception as e:
    print(f"[Pattern Error] Failed to detect patterns: {e}")
    return

  if patternName is None:
    print("No pattern found.")
  else:
    print(f"Pattern found: {patternName}")

if __name__ == "__main__":
  main()

    