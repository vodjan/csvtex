# For storing global variables

import argparse

# For things that don't change during runtime
strings = {
    "ERR MSG: no file specified" : "Error: no file specified",
    "ERR CODE: no file specified" : 100,
    "ERR MSG: unknown extension" : "Error: Unknown file extension: ",
    "ERR CODE: unknown extension" : 101
}


# Parse arguments
def parse_args():
    # Parse arguments
    parser = argparse.ArgumentParser(
        prog = "csvtex",
        description = "Convert CSV tables into TeX notation and back.",
        epilog = "")
    
    parser.add_argument("filename", type=str,
                        help="name of file to be converted")
    parser.add_argument("-fdd", "--force-decimal-dots", action="store_true", dest="fdd",
                        help="force decimal dots on output")

    # TODO: add options for:
    # - custom output filename
    # - optional stdout output
    # - more optional formatting

    return parser.parse_args()


# For things that change during runtime
def init():
    global debug
    global filename
    global out_filename
    global force_decimal_dots_on_output

    # Default values
    filename = None
    out_filename = None  # csvtex.py expects None if no filename specified by options
    force_decimal_dots_on_output = False

    # Parse arguments
    args = parse_args()

    # Assign arguments to global vars
    filename = args.filename
    force_decimal_dots_on_output = args.fdd


