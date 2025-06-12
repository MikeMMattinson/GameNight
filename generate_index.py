import os
import re
import argparse

# ----- Parse CLI arguments -----
parser = argparse.ArgumentParser(description="Generate index.html and README.md for game folders.")
parser.add_argument("--sorted", action="store_true", help="Sort the list of games alphabetically by title")
args = parser.parse_args()

# Paths
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(MAIN_DIR, 'contents', 'index.html')
README_TEMPLATE_PATH = os.path.join(MAIN_DIR, 'README.txt')
README_OUTPUT_PATH = os.path.join(MAIN_DIR, 'README.md')

# Ensure 'contents' folder exists
os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

# Folders to exclude
exclude_list = {
    '.git',
    'images',
}

# Detect game folders
game_folders = [
    f for f in os.listdir(MAIN_DIR)
    if os.path.isdir(os.path.join(MAIN_DIR, f))
    and f not in exclude_list
    and f != 'contents'
]

if args.sorted:
    game_folders.sort()

# ---------- Generate index.html ----------
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game Night</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <h1>Available Games</h1>
    <ul>
"""

for folder in game_folders:
    html_content += f'        <li><a href="../{folder}/">{folder}</a></li>\n'

html_content += """
    </ul>
    <footer>
        <p>🧩 Game Night by Mike</p>
        <img src="../images/meeple.png" alt="Meeple" style="width:50px;height:auto;">
    </footer>
</body>
</html>
"""

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] index.html generated at {INDEX_PATH}")

# ---------- Generate game list as Markdown ----------
markdown_list = "\n".join([f"- [{folder}](./{folder}/)" for folder in game_folders])

# ---------- Insert into README.md using README.txt template ----------
with open(README_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

pattern = re.compile(r'<!-- CONTENTS_START -->(.*?)<!-- CONTENTS_END -->', re.DOTALL)
replacement = f'<!-- CONTENTS_START -->\n{markdown_list}\n<!-- CONTENTS_END -->'

if not pattern.search(template):
    print("[WARN] CONTENTS_START and CONTENTS_END tags not found in README.txt")
else:
    updated_readme = pattern.sub(replacement, template)

    with open(README_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(updated_readme)

    print(f"[OK] README.md generated at {README_OUTPUT_PATH}")
