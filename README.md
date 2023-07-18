# csvtex
A simple Python script for converting CSV spreadsheets into (La)TeX tabular notation and back.

## Warning: probably not very good
This is a sample project that I'm using to learn more about Git and GitHub and brush up on Python. I am not an expert in neither TeX nor CSV and I'm only planning to implement basic functionality for my personal needs.

# Usage
```
csvtex.py <filename>
```

The script will decide what to do based on the file extension of the provided filename:
- `.tex`: Convert from TeX `{tabular}` to CSV,
- `.csv`: Convert from CSV into a basic TeX `{tabular}`.

The output file will be named the same basename as the input with the other extension.

**WARNING**: The script currently does not check for existing files and will overwrite any file in the folder that may have the same filename.
