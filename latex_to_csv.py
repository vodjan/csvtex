import csv
from io import StringIO  # used to return formatted CSV as array of strings (lines)

import config

# Return a text file as array of strings (lines).
def read_tex(filename):
    file = open(filename, "r")
    output = file.readlines()
    file.close()
    return output


# Return True if string contains at least one substring from list stubstrings.
def includes_substrings(substrings, string):
    for element in substrings:
        for i in range(0, len(string) - 1):
            if element == string[i : i + len(element)]:
                return True
    return False


# Return only the part of the file (as array of lines) which is a LaTeX tabe, excluding the lines "\begin{tabular}" and "\end{tabular}".
# TODO: Currently only supports one table per file (will convert first table in document). Consider adding support for multiple tables per file.
# TODO: There are probably table starters / enders about which I do not currently know. Consider implementing them.
def table_only(input):
    table_starters = ["\\begin{tabular}"]
    table_enders = ["\\end{tabular}"]

    output = []
    is_table = False

    for line in input:
        
        # Check for end of table (do not include this line)
        if is_table and includes_substrings(table_enders, line):
            is_table = False
            break

        if is_table:
            output.append(line)

        # Check for start of table (start including next line)
        if not is_table and includes_substrings(table_starters, line):
            is_table = True

    return output


# Delete lines that are LaTeX line separators from table (line array)
# TODO: There may be more possible LaTeX line separators in different packages, consider adding them
def remove_line_separators(input):
    line_separators = ["\\hline", "\\hhline"]

    # Pop lines that include line separators. Iterate from end to avoid changing indeces in progress.
    for i in range(len(input) - 1, -1, -1):
        if includes_substrings(line_separators, input[i]):
            input.pop(i)
    
    return input


# INPUT: 1D string array (array of lines)
# OUTPUT: 2D string of elements
def separate_latex_table_elements(input):
    # separate by '&'
    for i in range(0, len(input)):
        input[i] = input[i].split('&')

    return input


# Reformat all elements of input to be usable in csvfile (input: 2D string)
# TODO: More formatting exceptions wouldn't hurt. What about decimal dots? What about an option to keep some formatting?
def reformat_latex_elements_to_csv(input):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            # must use alloaction because of Python array shenanigans
            # remove dollar signs and curly brackets (sometimes used in Tex for decimal comma spacing)
            # TODO: only remove curly brackets when used for decimal comma spacing
            input[i][j] = input[i][j].replace('$', '').replace('{', '').replace('}', '')
            # remove leading and trailing spaces (also removes '\n')
            input[i][j] = input[i][j].strip()
            # remove double backslashes
            input[i][j] = input[i][j].strip("\\\\")
            # remove any remaining spaces in between backslashes and the value
            input[i][j] = input[i][j].strip()

            # Change any commas in any element into dots
            # TODO: add option into arg parser
            # TODO: only change decimal commas into dots
            if config.force_decimal_dots_on_output:
                input[i][j] = input[i][j].replace(',', '.')

    return input


# Convert TeX tabular into CSV and return as array of '\n'-terminated lines (strings)
def convert(filename):
    output = reformat_latex_elements_to_csv(
        separate_latex_table_elements(
            remove_line_separators(
                table_only(
                    read_tex(filename)))))

    # add CSV formatting and return as array of lines (strings)
    data = StringIO()

    my_writer = csv.writer(data)
    my_writer.writerows(output)

    return data.getvalue()

# TODO: convert multiple tables into multiple CSV files