# For storing global variables

strings = {
    "ERR MSG: no file specified" : "Error: no file specified",
    "ERR CODE: no file specified" : 100,
    "ERR MSG: unknown extension" : "Error: Unknown file extension: ",
    "ERR CODE: unknown extension" : 101
}

def init():
    global force_decimal_dots_on_output

    force_decimal_dots_on_output = False