import os
import re

# Set the main directory (where the script is located)
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

# Template for the standard <head> section
STANDARD_HEAD_TEMPLATE = """
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <link rel="stylesheet" href="../styles.css?v=2">
</head>
""".strip()

# Folders to exclude from processing
EXCLUDE = {'contents', 'images', '.git', '.vscode', '__pycache__'}

# Loop through each folder in the main directory
for folder in os.listdir(MAIN_DIR):
    folder_path = os.path.join(MAIN_DIR, folder)
    if not os.path.isdir(folder_path) or folder in EXCLUDE:
        continue

    index_path = os.path.join(folder_path, 'index.html')
    if not os.path.isfile(index_path):
        continue

    # Use the folder name (title case) as the <title>
    title = folder.replace('-', ' ').title()

    # Build the new <head> block
    new_head = STANDARD_HEAD_TEMPLATE.format(title=title)

    # Read the current content
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the existing <head> section
    updated_content = re.sub(
        r"<head>.*?</head>",
        new_head,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Save the updated file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"[OK] HEAD updated: {folder}/index.html → Title set to '{title}'")
