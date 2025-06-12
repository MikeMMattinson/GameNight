import os

# Main directory (where the script is located)
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

# Output index.html path
INDEX_PATH = os.path.join(MAIN_DIR, 'contents', 'index.html')

# Ensure 'contents' folder exists
os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

# Folders to exclude
exclude_list = {
    '.git',
    'images'
}

# Dynamically scan and filter game folders
game_folders = [
    f for f in os.listdir(MAIN_DIR)
    if os.path.isdir(os.path.join(MAIN_DIR, f)) and f not in exclude_list and f != 'contents'
]

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game Index</title>
</head>
<body>
    <h1>Available Games</h1>
    <ul>
"""

for folder in sorted(game_folders):
    html_content += f'        <li><a href="../{folder}/">{folder}</a></li>\n'

html_content += """
    </ul>
</body>
</html>
"""

# Write the generated HTML to file
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Index successfully generated at {INDEX_PATH}")
