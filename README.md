## Overview
DSX is a powerful tool designed for parsing and analyzing `.DS_Store` files, commonly used by macOS to store custom attributes of a folder. This tool allows users to easily extract directory and file information from these files, providing a straightforward interface for data analysis.

## Features
- **File Parsing**: Efficiently parse `.DS_Store` files to extract directories and files.
- **URL Support**: Download and parse `.DS_Store` files directly from URLs.
- **User-Friendly Interface**: Simple command-line interface for ease of use.
- **Logging**: Provides informative logging to track the process and errors.

## Installation
To install the required dependencies, run the following command:

```bash
pip install ds_store requests
```

## Usage
Here’s a quick example of how to use the DSX tool from the command line
```bash
python DSX.py path/to/your/file.DS_Store
```
You can also provide a URL to a .DS_Store file:
```bash
python DSX.py http://example.com/path/to/your/file.DS_Store
```
The tool will output the directories and files contained within the specified .DS_Store file.

## Example Output
When you run the tool, you will see output similar to the following:
```
Directories:
folder1
folder2

Files:
file1.txt
file2.jpg
```
## Contributing
We welcome contributions! Please read our contributing guidelines for more information.

## License
This project is licensed under the MIT License - see the LICENSE file for details
