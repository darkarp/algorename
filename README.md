# File Change Utility

[![Build Status](https://img.shields.io/badge/build-passing-green)]()
[![GitHub release](https://img.shields.io/github/release/darkarp/file_change.svg)](https://github.com/darkarp/file_change/releases/)
[![License](https://img.shields.io/github/license/darkarp/file_change.svg)](https://github.com/darkarp/file_change/blob/main/LICENSE)


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Arguments](#command-line-arguments)
- [Logging](#logging)
- [Contributors](#contributors)
- [License](#license)


## Introduction

This utility is a Python script designed to rename files in a folder or an individual file by shifting each alphabetic character in the filenames to the left by 1.


## Prerequisites

- Python 3.6+


## Installation

1. Clone the GitHub repository.
   ```
   git clone https://github.com/darkarp/file_change.git
   ```
2. Navigate to the project directory.
   ```
   cd file_change
   ```
3. Install the required Python packages.
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command Line Arguments

1. To rename a single file:
    ```
    python3 file_change.py -f [path/to/your/file]
    ```

2. To rename all files in a directory:
    ```
    python3 file_change.py -d [path/to/your/directory]
    ```

3. For silent mode (suppress errors):
    ```
    python3 file_change.py -s (...)
    ```  

4. For help:
    ```
    python3 file_change.py -h
    ```

## Logging

Logging is implemented with a rotating log file mechanism to ensure that it doesn't consume too much disk space over time. The log file will be generated in the same directory as the script, named `file_changer.log`. 

- You can set the logging verbosity level via an environment variable `FCLOG_LEVEL`, which accepts values like `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- You can set the log file name via an environment variable `FCLOG_NAME`. This name will be converted to lower-case.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
