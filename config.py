# For storing global variables

import argparse

# For things that don't change during runtime
strings = {
    "ERR MSG: no file specified" : "Error: No file specified",
    "ERR CODE: no file specified" : 100,
    "ERR MSG: unknown extension" : "Error: Unknown file extension: ",
    "ERR CODE: unknown extension" : 101,
    "ERR MSG: file exists" : "Error: File already exists (use -o to specify a different name or -f to overwrite): ",
    "ERR CODE: file exists" : 102
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
    parser.add_argument("-f", "--force", action="store_true", dest="force",
                        help = "force operation (overwrite existing file)")
    parser.add_argument("-fdd", "--force-decimal-dots", action="store_true", dest="fdd",
                        help="force decimal dots on output")
    parser.add_argument("-o", "--output", type=str, nargs='?', dest="output",
                        help="specify output filename")

    # TODO: add options for:
    # - custom output filename
    # - optional stdout output
    # - more optional formatting

    return parser.parse_args()


# For things that change during runtime
def init():
    global debug
    global filename  # the INPUT filename
    global force  # overwrite existing file
    global out_filename  # the OUTPUT filename
    global force_decimal_dots_on_output

    # Default values
    debug = False
    filename = None
    force = False
    out_filename = None  # csvtex.py expects None if no filename specified by options
    force_decimal_dots_on_output = False

    # Parse arguments
    args = parse_args()

    # Assign arguments to global vars
    if args.filename is not None: filename = args.filename
    force = args.force
    if args.output is not None: out_filename = args.output
    force_decimal_dots_on_output = args.fdd
