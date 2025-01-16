# CodeFilesToTxt 📝

> A Python utility to combine C++ source and header files into a single text file for easy sharing

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://choosealicense.com/licenses/apache-2.0/)

## 🎯 Overview

CodeFilesToTxt simplifies code sharing by merging `.cpp` and `.h` files into a single text file. Perfect for sharing code examples with people who don't have access to a compiler or development environment.

## 📑 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Smart Merging:** Combines C++ source and header files while maintaining readability
- **Simple Operation:** Easy-to-use command-line interface
- **Preserves Structure:** Maintains code organization and comments
- **Platform Independent:** Works on any system with Python installed

## 🔧 Requirements

- Python 3.x installed on your system
- Basic familiarity with command-line operations

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PascalND/CodeFilesToTxt.git
   cd CodeFilesToTxt
   ```

## 📖 Usage Guide

### Basic Usage

1. **Open the solution in your preferred IDE**

2. **Modify the directory path:**
   - Locate the `directory` variable in the code
   - Set it to the path where your `.cpp` and `.h` files are located
   ```python
   directory = "C:/Users/YourName/Path/To/Your/CppFiles"
   ```

3. **Run the script:**
   - Execute the script directly from your IDE
   - The program will process all `.cpp` and `.h` files in the specified directory

### Expected Output

The script will generate `output.txt` in the same directory as your source files, containing:
- Contents of the header file(s)
- A clear separator
- Contents of the source file(s)

### Example

```bash
# Your source directory before:
C:/Users/YourName/CppFiles/
  ├── example.cpp
  └── example.h

# After running the script:
C:/Users/YourName/CppFiles/
  ├── example.cpp
  ├── example.h
  └── output.txt
```

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

*Made with ❤️ by PascalND*
