#!/usr/bin/python

import sys, argparse, os, glob

parser = argparse.ArgumentParser(description='Utility to concatenate files')
parser.add_argument('--output',default='./output.tab', help='Specifies the output file.  The default is ./output.tab')
parser.add_argument('--input', default='./', required=True, help='The directory where input files are located. The default is current directory')
parser.add_argument('--extension', default='*', help='Limit the input selection to files with a certain extension')
parser.add_argument('--header', help='Keeps file header only once.',action="store_true")

res = parser.parse_args()

with open(res.output,'w') as f:

    print_header = True

    os.chdir(res.input)

    for file in glob.glob("*." + res.extension):
        print file
        with open(file, 'r') as file_in:
            content = file_in.read().splitlines(True)
        if print_header:
            f.writelines(content)
            if res.header:
                print_header = False
        else:
            f.writelines(content[1:])


#f.write('hello')

f.close()
