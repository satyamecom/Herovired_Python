import pathlib
import os
import shutil
import time

def copy_backup(source, dest):
    sfile = pathlib.Path(source)
    dfile = pathlib.Path(dest)

    # Check if source directory exists
    if not sfile.exists() or not sfile.is_dir():
        print("Error: Source directory does not exist or is not a directory.")
        return

    # Check if destination directory exists
    if not dfile.exists() or not dfile.is_dir():
        print("Error: Destination directory does not exist.")
        return

    slistfile = os.listdir(source)
    dlistfile = os.listdir(dest)

    print("\nSource Directory Files:", slistfile)
    print("Destination Directory Files:", dlistfile, "\n")

    for file in slistfile:
        src_path = sfile / file  # Full path to source file
        dest_path = dfile / file  # Full path to destination file

        if src_path.is_file():  # Ensure it's a file before copying
            if file in dlistfile:
                print(f"File '{file}' already exists. Creating a unique backup...")
                timestamp = time.strftime("%Y%m%d%H%M%S")
                new_dest_path = dfile / f"{file}_{timestamp}"  # Append timestamp
                shutil.copy2(src_path, new_dest_path)  # Copy with new name
                print(f"Copied '{file}' as '{new_dest_path.name}'.")
            else:
                print(f"Copying '{file}' to destination...")
                shutil.copy2(src_path, dest_path)  # Normal copy
        else:
            print(f"Skipping '{file}' as it is not a file.")

    print("\nBackup process completed successfully.")

# Get user input for directories
sfile = input("Enter the source directory path: ")
dfile = input("Enter the destination directory path: ")
copy_backup(sfile, dfile)
