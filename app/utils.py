import os

def get_directory_structure(rootdir, exclude_folders=None, exclude_files=None):
    """
    Recursively generates the folder structure as a plain text string.
    Exclude folders like 'node_modules', '.git', etc., and files like '.env'.
    """
    if exclude_folders is None:
        # A broader list of common folders to exclude
        exclude_folders = {
            'node_modules', 'build', 'dist', '__pycache__', '.git', '.vscode', '.idea', 
            '.sublime', 'target', 'tmp', 'temp', 'logs', '.log', 'coverage', 
            '.env', '.env.*', '.DS_Store', 'Thumbs.db', 'yarn.lock', 'package-lock.json', 
            '.docker', '.vagrant', '.terraform'
        }

    if exclude_files is None:
        # A broader list of common files to exclude
        exclude_files = {
            '.env', '.env.*', '.DS_Store', 'Thumbs.db', 'yarn.lock', 'package-lock.json', 
            '.gitignore', 'Dockerfile', 'README.md'
        }

    lines = []

    # os.walk starts from the rootdir and traverses all subdirectories and files
    for root, dirs, files in os.walk(rootdir):
        # Exclude directories based on the exclusion list
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        # Compute the level of indentation based on the depth of the directory
        level = root.replace(rootdir, '').count(os.sep)
        indent = '    ' * level  # Use 4 spaces for each level of indentation
        folder_name = os.path.basename(root)

        # Only print the folder if it's not the root directory and is not excluded
        if root != rootdir:
            lines.append(f"{indent}{folder_name}/")

        # Add files with an extra level of indentation
        sub_indent = '    ' * (level + 1)
        for file in files:
            if file not in exclude_files:
                lines.append(f"{sub_indent}{file}")

    return "\n".join(lines)
