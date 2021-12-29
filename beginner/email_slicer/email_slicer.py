import argparse
import sys
# helper.py is located in the beginner folder in this repo
sys.path.append("/path/to/helper.py")
import helper
import os
import re
import csv

if len(sys.argv) < 2:
    print("use -h for help")
    sys.exit(0)

parser = argparse.ArgumentParser()

input_group = parser.add_mutually_exclusive_group()
parser.add_argument('-o','--output_file',help='output to file')
input_group.add_argument('-e','--emails', nargs="+", help='accept emails to slice emails')
input_group.add_argument('-f', '--file_input',
        help='accept a file with emails as input')




args = parser.parse_args()

emails = args.emails
file_input = args.file_input
output_file = args.output_file

outputs = []
wrong_inputs = []

def slicer(email):
    sliced_email = []
    a = re.search("([.a-z1-9]+)@([a-z]+[a-z.]+)", email)
    sliced_email.append(a.group(1))
    sliced_email.append(a.group(2))
    return sliced_email

def slicer_checker(input_list):
    wrong_inputs = []
    outputs = []
    for item in input_list:
        if helper.condition_email(item):
            wrong_inputs.append(item)
            continue
        outputs.append(slicer(item))
    return wrong_inputs, outputs

if emails:
    wrong_inputs, outputs = slicer_checker(emails)

if file_input:
    reader = open(file_input, 'r')
    try:
        inputs = reader.read().splitlines()
        wrong_inputs, outputs = slicer_checker(inputs)
    finally:
        reader.close()


if output_file:
    f = open(output_file, 'w')
    writer = csv.writer(f)
    writer.writerows(outputs)
else:
    for output in outputs:
        print(output[0], output[1])
    
    if len(wrong_inputs):
        print("\n\n\nInvalid Inputs:")
        for wrong_input in wrong_inputs:
            print(wrong_input)


