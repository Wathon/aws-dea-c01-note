import os
import re

content_dir = "/home/monetine/Workspace/Wathon/aws-dea-c01/content"

# Regex to find links like [Text](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/path/to/file.md)
# We want to replace it with [Text](/path/to/file)
# Wait, let's use Quartz Wiki links if possible, or just standard relative links.
# If we replace `(file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/` with `(/` and strip `.md)`, it becomes `(/path/to/file)`.

regex = re.compile(r'file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/([^)]+)\.md')

count = 0
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = regex.sub(r'/\1', content)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed links in {filepath}")

print(f"Fixed {count} files.")
