import os
import sys
import subprocess

def main():
    # check commandline arguments
    if len(sys.argv) != 5:
        print("Usage: main.py [out_dir] [src_dir] [pattern] [num_of_pages_each_combination]")
        exit()
    
    out_dir = sys.argv[1]
    src_dir = sys.argv[2]
    pattern = sys.argv[3]
    num_of_pages_each_combination = int(sys.argv[4])

    # get all filenames with pattern
    all_files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    patterned_files = [src_dir + f for f in all_files if pattern in f]
    print("We have {} file(s) out of {} file(s) to process.".format(len(patterned_files), len(all_files)))

    # check if we can proceed
    if len(patterned_files) <= 0:
        print("No file to be processed, exiting")
        exit()
    if (len(patterned_files) % num_of_pages_each_combination) != 0:
        print("Potential wrong num_of_pages_each_combination, exiting")
        exit()
    result = subprocess.run(["pdfunite -v"], shell=True, capture_output=True, text=True)
    if "version" not in result.stderr:
        print("No pdfunite installation detected, exiting")
        exit()
    
    # combine
    patterned_files.sort()
    num_of_iter = int(len(patterned_files) / num_of_pages_each_combination)
    for i in range(num_of_iter):
        # print("pdfunite {} {}".format(" ".join(patterned_files[i*7:(i+1)*7]), out_dir + pattern + "_" + str(i) + ".pdf"))
        # break
        result = subprocess.run(["pdfunite {} {}".format(" ".join(patterned_files[i*7:(i+1)*7]), out_dir + pattern + "_" + str(i) + ".pdf")], shell=True, capture_output=True, text=True)
        
    print("{} files are generated in {}".format(num_of_iter, out_dir))

if __name__ == "__main__":
    main()
