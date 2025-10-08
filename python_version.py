import json
import sys
import os

VERSION_FILE = "version.json"

def get_version():
    if not os.path.exists(VERSION_FILE):
        return {"major": 1, "minor": 0, "patch": 0}  # Start at version 1

    with open(VERSION_FILE, 'r') as f:
        return json.load(f)

def save_version(version):
    with open(VERSION_FILE, 'w') as f:
        json.dump(version, f, indent=2)

def format_version(version):
    """Format version according to the new rules"""
    major = version['major']
    minor = version['minor']
    patch = version['patch']
    if patch == 0:
        if minor == 0:
            return f"{major}"  # e.g., 1.0.0 -> "1"
        else:
            return f"{major}.{minor}"  # e.g., 5.3.0 -> "5.3"
    else:
        return f"{major}.{minor}.{patch}"  # e.g., 6.0.1 -> "6.0.1"

def increment_major():
    v = get_version()
    v['major'] += 1
    v['minor'] = 0
    v['patch'] = 0
    save_version(v)
    return format_version(v)

def increment_minor():
    v = get_version()
    v['minor'] += 1
    v['patch'] = 0
    save_version(v)
    return format_version(v)

def increment_patch():
    v = get_version()
    v['patch'] += 1
    save_version(v)
    return format_version(v)

def show_version():
    v = get_version()
    return format_version(v)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(show_version())
        sys.exit(0)

    if len(sys.argv) != 2:
        print("Usage: python_versioning <major|minor|patch|show>")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'major':
        print(increment_major())
    elif command == 'minor':
        print(increment_minor())
    elif command == 'patch':
        print(increment_patch())
    elif command == 'show':
        print(show_version())
    else:
        print("Invalid command. Use: major, minor, patch, or show")
        sys.exit(1)






