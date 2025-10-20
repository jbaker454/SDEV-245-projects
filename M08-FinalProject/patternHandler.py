import re

patterns: dict[str, str] = {
    "base64": r"^(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$",
    "Twitter": r"\b[1-9][0-9]+-[0-9A-Za-z]{35,45}\b",
    "Facebook": r"EAACEdEose0cBA[0-9A-Za-z]+",
    "InstaGram": r"[0-9a-fA-F]{7}\.[0-9a-fA-F]{32}",
    "Google": r"\bAIza[0-9A-Za-z\-_]{33,37}\b",
}

def checkForPatterns(fileText: str):
  """
  Scans the given file text for known patterns such as API keys or tokens.
  Returns the name of the first pattern detected, or None if no match.
  """
  for pattern, regex in patterns.items():
    if re.search(regex, fileText, flags=re.MULTILINE | re.IGNORECASE):
      return pattern
  return None

def patternHandlerMain(fileText: str):
  pattern: str|None = checkForPatterns(fileText)
  return pattern
