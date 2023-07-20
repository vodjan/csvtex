#!/usr/bin/env python3

# import sys

import config
import csv_to_latex
import latex_to_csv

# initialise global variables, parse arguments
config.init()

# TODO: Better exception handling?
if config.filename is None:
    print(config.strings["ERR MSG: no file specified"])
    exit(config.strings["ERR CODE: no file specified"])

if config.filename.split('.')[-1] == "csv":
    csv_to_latex.convert(config.filename)
elif config.filename.split('.')[-1] == "tex":
    latex_to_csv.convert(config.filename)
else:
    # TODO: Better exception handling?
    print(config.strings["ERR MSG: unknown extension"], sys.argv[-1].split('.')[-1])
    exit(config.strings["ERR CODE: unknown extension"])