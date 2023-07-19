import csv

# Return filename (CSV) as a list.
def read_csv(filename):
    with open(filename) as csvfile:
        my_reader = csv.reader(csvfile, dialect="excel")
        return list(my_reader)


# Convert filename to basefilename.tex.
def convert(filename):
    # read input file
    output = read_csv(filename)
    
    # denote start of table
    # TODO: uses length of first row as number of columns. Could be imprved.
    # TODO: Also add tags to include LaTeX packages necessary for processing the table.
    output.insert(0, "\\begin{tabular}{" + len(output[0]) * "|c" + "|}")

    # concatenate each row into "&" - separated string
    # TODO: recognise string types and add corresponding LaTex noation?
    for i in range(1, len(output)):
        processed_line = ""
        for j in range(0, len(output[i])):
            processed_line += output[i][j]
            processed_line += " & " if j != len(output[i]) - 1 else ""

        # add trailing double backslash to end of row
        processed_line += " \\\\"
        output[i] = processed_line

    # add "\hline" separators
    # TODO: It seems to me that this could use some love, but I don't know what bc I'm tired
    for i in range(1, 2 * len(output), 2):
        output.insert(i, "\hline")

    # denote end of table
    output.append("\end{tabular}")

    # create new filename 
    filename = filename.split('.')[0] + ".tex"
    # TODO: check if filename exitst to avoid overwrites
    # TODO: only replace last file extension

    # write new file
    # TODO: Optional stdout output?
    file = open(filename, 'w')
    for line in output:
        file.write("".join(line))
        file.write("\n")
    file.close()


# TODO: Reformatting def, implement config.force_decimal_dots_on_output
