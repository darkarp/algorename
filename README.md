# AlgoRename

[![Build Status](https://img.shields.io/badge/build-passing-green)]()
[![GitHub release](https://img.shields.io/github/release/darkarp/algorename.svg)](https://github.com/darkarp/algorename/releases/)
[![License](https://img.shields.io/github/license/darkarp/algorename.svg)](https://github.com/darkarp/algorename/blob/main/LICENSE)


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Arguments](#command-line-arguments)
- [Algorithm Loading](#algorithm-loading)
- [Algorithm Listing](#algorithm-listing)
- [Multiprocessing](#multiprocessing)
- [Logging](#logging)
- [License](#license)


## Introduction

This utility is a Python script designed to rename files in a folder or an individual file based on a dynamically loaded algorithm. It utilizes multiprocessing for efficiency and can operate recursively on directories. The example algorithm shifts each alphabetic character in the filenames to the left by 1.

## Prerequisites

- Python 3.6+


## Installation

1. Clone the GitHub repository.
   ```
   git clone https://github.com/darkarp/algorename.git
   ```
2. Navigate to the project directory.
   ```
   cd algorename
   ```
3. Install the required Python packages.
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command Line Arguments

1. To rename a single file:
 ```
 python algorename.py -f [path/to/your/file]
 ```

2. To rename all files in a directory:
 ```
 python algorename.py -d [path/to/your/directory]
 ```

3. To rename files recursively in a directory:
 ```
 python algorename.py -d [path/to/your/directory] -r
 ```

4. For silent mode (suppress errors):
 ```
 python algorename.py -s (...)
 ```  

5. To not create a log file:
 ```
 python algorename.py -nl (...)
 ```  

6. To use a specific algorithm:
 ```
 python algorename.py -a [algorithm_name]
 ```  

7. To list available algorithms:
 ```
 python algorename.py -l
 ```

8. For help:
 ```
 python algorename.py -h
 ```

## Algorithm Loading  

The script supports loading custom algorithms. Place your algorithm module under the `algorithms/` folder, and the script will be able to import it dynamically. Make sure to define a function called `apply_algorithm` within the module.

The environment variable `FCLOG_PATH` specifies the directories where the script will look for custom algorithm modules. You can modify this by changing your environment variables or by creating a `.env` file.

Example:  

- Windows: `FCLOG_PATH=C:\path\to\algorithms;D:\another\path\to\algorithms`
- Linux/Mac: `FCLOG_PATH=/path/to/algorithms:/another/path/to/algorithms`

## Algorithm Listing  

You can list all available algorithms along with their metadata using the `-l` flag. This is useful for understanding what each algorithm does before using it.

## Multiprocessing

This utility uses multithreading to efficiently rename multiple files in a directory. It uses `concurrent.futures.ThreadPoolExecutor` to speed up the renaming tasks.

## Logging

Logging is implemented with a rotating log file mechanism to ensure that it doesn't consume too much disk space over time. The log file will be generated in the same directory as the script, named `algorename.log`. 

- You can set the logging verbosity level via an environment variable `FCLOG_LEVEL`, which accepts values like `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- You can set the log file name via an environment variable `FCLOG_NAME`. This name will be converted to lower-case.
- You can disable logging by specifying `-nl` argument.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
