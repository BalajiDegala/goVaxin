#!/usr/bin/env python3

import argparse
import shutil

parser = argparse.ArgumentParser(description="Delete a Vaccine virus in Maya Ascii file")

# Add an argument for the input file
parser.add_argument("-i","--input_file", help="The input file to process")

# Parse the arguments
args = parser.parse_args()

backup_file =  args.input_file.replace('.ma', '.ma_bak')
shutil.copy(args.input_file, backup_file)
# Open the file
with open(args.input_file, "r") as f:
    # Read the file line by line
    lines = f.readlines()

# Convert the list of lines into an iterator
lines = iter(lines)

# Open the file in write mode
with open(args.input_file, "w") as f:
    # Iterate over the lines
    for line in lines:
        # If the line contains the word "vaccine", skip it and the next 10 lines
        if "vaccine" in line:
            print("got affected with Vaccine Virus")
            for i in range(12):
                next(lines, None)
        # Write the line to the file
        else:
            print("This file is safe from Vaccine Virus")
            f.write(line)
