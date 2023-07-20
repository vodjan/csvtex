# csvtex
A simple Python program for converting CSV spreadsheets into (La)TeX tabular notation and back.

## Warning: probably not very good
This is a sample project that I'm using to learn more about Git and GitHub and to brush up on Python. I am not an expert in neither TeX nor CSV and I'm only planning to implement basic functionality for my personal needs.

# Usage
```
csvtex.py [-h] [-fdd] <filename>
```
## Positional arguments:
- `filename`: name of file to be converted

The program will decide what to do based on the file extension of the provided filename:
- `.tex`: Convert from TeX `{tabular}` to CSV,
- `.csv`: Convert from CSV into a basic TeX `{tabular}`.
The output file will be named the same basename as the input with the other extension.

## Options:
- `-h`, `--help`: show help message and exit
- `-fdd`, `--force-decimal-dots`: force decimal dots on output

## Notes:
For `.tex` -> `.csv` conversion, all text in the file not encased between `\begin{tabular}` and `\end{tabular}` will be ignored. If the file contains more than one `tabular`, only the first one will be converted.

**WARNING**: The script currently does not check for existing files and will overwrite any file in the folder that may have the same filename.
