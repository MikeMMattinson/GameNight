import os

# Main directory (script location)
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

# Output path for index.html
INDEX_PATH = os.path.join(MAIN_DIR, 'contents', 'index.html')

# Ensure 'contents' folder exists
os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

# Folders to exclude
exclude_list = {
    '.git',
    'images',
}

# Find game folders
game_folders = [
    f for f in os.listdir(MAIN_DIR)
    if os.path.isdir(os.path.join(MAIN_DIR, f))
    and f not in exclude_list
    and f != 'contents'
]

# Generate HTML content including external CSS and footer image
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game Night</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <h1>Game Night Rules</h1>
    <ul>
"""

for folder in sorted(game_folders):
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

# Write HTML content to index.html
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Index successfully generated at {INDEX_PATH}")
