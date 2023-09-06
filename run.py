#!/usr/bin/env python3

import os
import argparse
import logging
import json
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


def setup_logging(verbosity_level: str, filename: str = "file_changer.log", max_size: int = (1024 ** 2) * 1):
    """Setting up logging

    Args:
        verbosity_level (str): Log verbosity level; can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
    """
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_handler = RotatingFileHandler(filename, maxBytes=max_size, backupCount=5)
    logging.basicConfig(handlers=[log_handler], format=log_format, level=getattr(logging, verbosity_level, "INFO"))


def log_json(action: str, old: str, new: str):
    """Logs messages in JSON.

    Args:
        action (str): Description of the performed action.
        old (str): Original filename or path.
        new (str): New filename or path.
    """
    log_entry = json.dumps({"action": action, "old_name": old, "new_name": new})
    logging.info(log_entry)


def shift_filename(filename: str) -> str:
    """Shift each alphabetic character in a filename to the left by 1.

    Args:
        filename (str): The original filename.

    Returns:
        str: The shifted filename.
    """
    shifted_name = ""
    for char in filename:
        if char.isalpha():
            shifted_char = chr(ord(char) - 1) if char.lower() != 'a' else 'z' if char.islower() else 'Z'
        else:
            shifted_char = char
        shifted_name += shifted_char
    return shifted_name


def shift_directory(folder_path: str):
    """Rename all files in the given directory by shifting their names to the left by 1.

    Args:
        folder_path (str): Path to the directory whose filenames need to be shifted.
    """
    for filename in os.listdir(folder_path):
        original_path = os.path.join(folder_path, filename)
        new_filename = shift_filename(filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(original_path, new_path)
        log_json("Shifted Directory File", original_path, new_path)


def shift_single_file(file_path: str):
    """Rename a single file by shifting its name to the left by 1.

    Args:
        file_path (str): The path to the file that needs to be renamed.
    """
    folder_path, filename = os.path.split(file_path)
    new_filename = shift_filename(filename)
    new_path = os.path.join(folder_path, new_filename)
    os.rename(file_path, new_path)
    log_json("Shifted Single File", file_path, new_path)


def main():
    """Main function.

    It sets up the logging, parses CLI arguments, and calls the appropriate function to rename files or directories.
    """
    # Load environment variables from .env file
    load_dotenv()

    parser = argparse.ArgumentParser(description="Shift file or directory names by 1 character to the left.")
    parser.add_argument("-s", "--silent", help="Suppress errors.", action="store_true")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Specify the path of a single file to shift.", type=str)
    group.add_argument("-d", "--dir", help="Specify the directory path to shift all file names.", type=str)

    args = parser.parse_args()

    # Setting verbosity levels and logging after parsing arguments
    verbosity_level = os.getenv("FCLOG_LEVEL", "INFO").upper()
    log_filename = os.getenv("FCLOG_NAME", "file_changer.log").lower()

    setup_logging(verbosity_level, log_filename, max_size=(1024**2)*1)

    try:
        if args.file:
            if os.path.exists(args.file) and os.path.isfile(args.file):
                shift_single_file(args.file)
            else:
                error = f"The file {args.file} does not exist or is not a file."
                logging.error(error)
                if not args.silent:
                    print(error)

        if args.dir:
            if os.path.exists(args.dir) and os.path.isdir(args.dir):
                shift_directory(args.dir)
            else:
                error = f"The directory {args.dir} does not exist or is not a directory."
                logging.error(error)
                if not args.silent:
                    print(error)
    except Exception as e:
        error = f"An unexpected error occurred: {e}"
        logging.critical(error)
        if not args.silent:
            print(error)


if __name__ == "__main__":
    main()
