# Docker Tag Automation 

This project provides a streamlined approach to automate Docker image tagging using versioning strategies. It supports two main versioning approaches:

- **Semantic Versioning**
- **Timestamp-based Versioning**

<img src="https://github.com/smoothcoode/Image/blob/main/dockertag.gif?raw=true"  height="600" />

---
## Features

- Semantic versioning stored in a JSON file and Automated version increments (major, minor, patch)
- Timestamp-based versioning for unique build identifiers
- Cross-platform setup instructions for Windows and Linux
---

## Docker Image Reference Structure

![Docker Tag Illustration](https://github.com/smoothcoode/Image/blob/main/dockerreferenceimage.gif?raw=true)
### 🔹 REGISTRY_HOST[:PORT] (Optional)

Specifies the hostname (and optional port) of the Docker registry.


### 🔹 NAMESPACE (Optional)

Represents the user or organization account within the registry.
### 🔹 REPOSITORY (Required)
The actual name of the image.
### 🔹 TAG (Optional but Important)

Identifies a specific version or variant of the image.

- If omitted, Docker defaults to `latest`.
- Tags allow managing multiple versions of the same image:
  - `myapp:1.0.0` (semantic version)
  - `myapp:2025_10_14_1200` (timestamp-based tag)
  - `myapp:latest` (default if none specified)

---

## Semantic Versioning

The core script `pyv.py` manages semantic versioning stored in a `docker_version.json` file. It allows incrementing major, minor, and patch versions, and displays the current version.

### How it works

- If the version file does not exist, it initializes to version `1.0.0`.
- Supports commands:
  - `show`: Displays current version
  - `major`: Increments major version
  - `minor`: Increments minor version
  - `patch`: Increments patch version

### Usage

```bash
python pyv.py show
python pyv.py major
python pyv.py minor
python pyv.py patch
```



### Global Command Setup

#### Windows PowerShell

1. **Create a batch file (`pyv.bat`)**

```batch
@echo off
python "%~dp0pyv.py" %*
```

2. **Set up PowerShell Profile**

```powershell
Test-Path $PROFILE
New-Item -ItemType File -Path $PROFILE -Force
notepad $PROFILE
```

3. **Add alias to profile**

```powershell
Set-Alias pyv "C:\path\to\pyv.bat"
```

4. **Configure execution policy**

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Linux

1. **Create a script (`pyv`)**

```bash
#!/usr/bin/env python3
# Add the Python script code here
```

2. **Make it executable and copy**

```bash
chmod +x pyv
sudo cp pyv /usr/local/bin/
```

---
## Date Timestamps
###  Windows PowerShell

Add the following function to your PowerShell profile to generate timestamp strings:

```powershell
notepad $PROFILE
```
add this function 
```powershell
function dtsv { Get-Date -Format "yyyy_MM_dd__HH_mm_ss" }
```

**Usage:**

```powershell
dtsv
```

---

###  Linux

Add the alias to your shell configuration (`~/.bashrc` or `~/.zshrc`):

```bash
echo $SHELL  #To know your shell 
```
Set Date-Timestamps alias 
```bash
alias dtsv="date +'%Y_%m_%d__%H_%M_%S'"
```

After editing, source the profile:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

---

## Summary

This setup enables efficient Docker image tagging through semantic or timestamp-based versioning, with cross-platform support and easy integration into your build process.

---