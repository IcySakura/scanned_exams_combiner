# scanned_exams_combiner
A simple script for combining scanned exams (pdf)

# Setup
You need to have pdfunite installed.
Your scanned exams should be single-page pdf files with sortable filenames.

# Usage
```
main.py [out_dir] [src_dir] [pattern] [num_of_pages_each_combination]
```

# Example
Suppose you have 3 students with 2-page exams, where files are "xxx_001.pdf", "xxx_002.pdf", "xxx_003.pdf", "xxx_004.pdf", "xxx_005.pdf", "xxx_006.pdf".

Run ```mkdir ./exam_out``` to mkae [out_dir] first.

Run ```main.py ./exam_out/ [src_dir]/ "xxx" 2``` will output "xxx_0.pdf", "xxx_1.pdf", "xxx_2.pdf" in "./exam_out" folder.
