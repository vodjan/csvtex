#!/usr/bin/env python3

import sys

import config
import csv_to_latex
import latex_to_csv

# TODO: Better exception handling?
if len(sys.argv) < 2:
    print(config.strings["ERR MSG: no file specified"])
    exit(config.strings["ERR CODE: no file specified"])

config.init()

filename = sys.argv[-1]

if sys.argv[-1].split('.')[-1] == "csv":
    csv_to_latex.convert(filename)
elif sys.argv[-1].split('.')[-1] == "tex":
    latex_to_csv.convert(filename)
else:
    # TODO: Better exception handling?
    print(config.strings["ERR MSG: unknown extension"], sys.argv[-1].split('.')[-1])
    exit(config.strings["ERR CODE: unknown extension"])