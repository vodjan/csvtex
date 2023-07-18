#!/usr/bin/env python3

import sys

import config
import csv_to_latex
import latex_to_csv

# TODO: Better exception handling?
if len(sys.argv) < 2:
    print("Error: no file specified")
    exit(100)

config.init()

filename = sys.argv[-1]

if sys.argv[-1].split('.')[-1] == "csv":
    csv_to_latex.convert(filename)
else:
    latex_to_csv.convert(filename)