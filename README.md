# csvtex
A simple Python program for converting CSV spreadsheets into (La)TeX tabular notation and back.

## Warning: probably not very good
This is a sample project that I'm using to learn more about Git and GitHub and to brush up on Python. I am not an expert in neither TeX nor CSV and I'm only planning to implement basic functionality for my personal needs.

# Usage
```
csvtex.py [-h] [-f] [-fdd] [-o [OUTPUT]] filename
```
## Positional arguments:
- `filename`: name of file to be converted

The program will decide what to do based on the file extension of the provided filename:
- `.tex`: Convert from TeX `{tabular}` to CSV,
- `.csv`: Convert from CSV into a basic TeX `{tabular}`.

## Options:
- `-h`, `--help`: show help message and exit
- `-f`, `--force`: force operation (overwrite existing file)
- `-fdd`, `--force-decimal-dots`: force decimal dots on output
- `-o`, `--output`: specify output filename (default: same basename as input file with other extension; will be ignored if `-p` is specified)
- `-p`, `--print`: print output to stdout instead of writing to file

## Notes:
For `.tex` -> `.csv` conversion, all text in the file not encased between `\begin{tabular}` and `\end{tabular}` will be ignored. If the file contains more than one `tabular`, only the first one will be converted.
