import re
import sys
from pathlib import Path
import subprocess

def bump_version(version: str, level: str) -> str:
    major, minor, patch = map(int, version.split("."))
    if level == "patch":
        patch += 1
    elif level == "minor":
        minor += 1
        patch = 0
    elif level == "major":
        major += 1
        minor = 0
        patch = 0
    return f"{major}.{minor}.{patch}"

pyproject = Path("emota_loader/pyproject.toml")
content = pyproject.read_text()

current_version = re.search(r'version\s*=\s*"([\d.]+)"', content).group(1)
level = sys.argv[1] if len(sys.argv) > 1 else "patch"
new_version = bump_version(current_version, level)

new_content = re.sub(r'version\s*=\s*"[\d.]+"', f'version = \"{new_version}\"', content)
pyproject.write_text(new_content)

print(f"Bumped version: {current_version} → {new_version}")

# Git tag and commit
subprocess.run(["git", "commit", "-am", f"Bump version to {new_version}"])
subprocess.run(["git", "tag", f"v{new_version}"])
subprocess.run(["git", "push", "origin", "main", "--tags"])