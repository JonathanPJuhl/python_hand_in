import csv as c
from os import walk

class ex2:
    def print_file_content(file):
        with open(file) as csv:
            lines = csv.readlines()
        header = lines[:1]
        rows = lines[1:]
        print(header)
        print(rows)

    def write_list_to_file(output_file, list2):
        of = open(output_file, 'w')
        for line in list2:
            of.write(line + '\n')
        of.close()

    def read_csv(csv):
        with open(csv, newline='') as csv:
            lines = csv.readlines()
        header = lines[:1]
        rows = lines[1:]
        new_list = []
        new_list.append(header)
        for r in rows:
            new_list.append(r)
            
        print(new_list)

    def get_file_names(folderpath, output):
        files = []
        for (dirpath, dirnames, filenames) in walk(folderpath):
            files.extend(filenames)
        
        of = open(output, 'w')
        for f in files:
            of.write(f + '\n')
        of.close()
        
    def get_all_file_names(folderpath, output):
        files = []
        for (dirpath, dirnames, filenames) in walk(folderpath):
            files.extend(filenames)
        
        of = open(output, 'w')
        for f in files:
            of.write(f + '\n')
        of.close()
