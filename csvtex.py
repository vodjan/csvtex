#!/usr/bin/env python3

# import sys

import os

import config
import csv_to_latex
import latex_to_csv

# initialise global variables, parse arguments
config.init()

# TODO: Better exception handling?
if config.filename is None:
    print(config.strings["ERR MSG: no file specified"])
    exit(config.strings["ERR CODE: no file specified"])

# Convert
# Always expect convert functions to return array of '\n'-terminated lines (strings)
if config.filename.split('.')[-1] == "csv":
    output = csv_to_latex.convert(config.filename)

    if config.out_filename is None:
        # TODO: only replace last file extension
        config.out_filename = config.filename.split(".")[0] + ".tex"

elif config.filename.split('.')[-1] == "tex":
    output = latex_to_csv.convert(config.filename)

    if config.out_filename is None:
        # TODO: only replace last file extension
        config.out_filename = config.filename.split(".")[0] + ".csv"
else:
    # TODO: Better exception handling?
    print(config.strings["ERR MSG: unknown extension"], config.filename.split('.')[-1])
    exit(config.strings["ERR CODE: unknown extension"])

# check if filename exitst to avoid overwrites
if not config.force and not config.print_to_stdout and os.path.isfile(config.out_filename):
    print(config.strings["ERR MSG: file exists"], config.out_filename)
    exit(config.strings["ERR CODE: file exists"])

# print output
if config.print_to_stdout:
    for line in output:
        print(line, end='')
# save output to file
else:
    file = open(config.out_filename, 'w')
    for line in output:
        file.write(line)
    file.close()
