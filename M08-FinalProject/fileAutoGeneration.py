import os

SAFE_DIR = os.path.abspath("safe_files")
os.makedirs(SAFE_DIR, exist_ok=True)

files = {
    "plain_text.txt": """Hello!
This is a safe, normal text file.
No patterns should be detected here.
""",

    "google_key.txt": """User configuration:
api_key = AIzaSyA1b2c3d4e5f6g7h8i9j0kLmNoPqRsTuv
""",

    "facebook_token.txt": """Access token:
EAACEdEose0cBA12345xyzABCDEF
""",

    "twitter_token.txt": """Bearer token example:
1234567890-ABCDEFGHIJKLMNOPQRSTUVWX1234567890abcd
""",

    "instagram_token.txt": """Instagram token:
abc1234.0123456789abcdef0123456789abcdef
""",

    "base64_data.txt": """SGVsbG8gV29ybGQhCg==""",  # "Hello World!" in Base64

    "empty.txt": ""  # Empty file
}

for name, content in files.items():
    path = os.path.join(SAFE_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(files)} test files in '{SAFE_DIR}'")