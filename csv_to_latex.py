import csv
import config

# Return filename (CSV) as a 2D list of elements per row.
def read_csv(filename):
    with open(filename) as csvfile:
        my_reader = csv.reader(csvfile, dialect="excel")
        return list(my_reader)


# Input: 2D list of strings
# Output: 2D list of strings formatted for TeX tabular
def format_elements_for_tex(input):
    # Format each element:
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):

            # Replace all commas by points
            # TODO: Detect only decimal commas
            if config.force_decimal_dots_on_output:
                input[i][j] = input[i][j].replace(",", ".")

            # surround all commas by {} for correct spacing in Tex
            # TODO: only do this for decimal commas
            # TODO: add an option for this
            else:
                input[i][j] = input[i][j].replace(",", "{,}")
    return input


# Input: 2D list of strings
# Output: 1D list of lines for TeX tabular
def create_tabular(input):

    # denote start of table
    # TODO: uses length of first row as number of columns. Could be imprved.
    # TODO: Also add tags to include LaTeX packages necessary for processing the table.
    input.insert(0, "\\begin{tabular}{" + len(input[0]) * "|c" + "|}")

    # concatenate each row into "&" - separated string and add trailing double backslash to end of row
    for i in range(1, len(input)):
        input[i] = " & ".join(input[i]) + " \\\\"

    # add "\hline" separators
    # TODO: It seems to me that this could use some love, but I don't know what bc I'm tired
    for i in range(1, 2 * len(input), 2):
        input.insert(i, "\\hline")

    # denote end of table
    input.append("\end{tabular}")

    return input


# Return list of lines ('\n'-terminated strings)
def convert(filename):
    output = create_tabular(
        format_elements_for_tex(
            read_csv(filename)))

    # terminate lines
    for i in range(0, len(output)):
        output[i] = output[i] + '\n'

    return output
