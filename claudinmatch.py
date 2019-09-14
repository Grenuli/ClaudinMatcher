#!/usr/bin/python
# This has been coded by Grenuli (GitHub.com/Grenuli, Bsc. Ing. Lena Stohwasser) and is thus her intellectual work and possession.
# You may use it and distribute it under further notice and indication of her name and work.
import re

#Prompt user for input file. Please also state type of file. txt is preferred
cl_file = open(input("Please enter the full name of the file with the prepared claudin sequences.\n"
                     "Note that for files in fasta format you have to put \"file.fasta.txt\": "),"r",1)


#Prompt user for Claudinsequences to search for and validate
cl_charge = input("Please indicate claudin sequence pattern you want to find."
                 "Type in belonging keyword:\n"
                    "all: just claudins\n"
                    "all-channels: all channel forming claudins\n"
                    "an-ion: an-ion-channels with single or double pos charge (pospos, posneu)\n"
                    "kat-ion: kat-ion-channels with single or double negative charge (negneg, negneu, neuneg)\n"
                    "kat-an-ion: kat-ion channels with low an-ion permability (posneg)\n"
                    "all-kat-ion: all kat-ion channels\n")

#Depending on Claudins to filter, the pattern and restriction level can be choosen from keywords
keywords = ["all", "all-channels", "an-ion", "kat-ion", "kat-an-ion", "all-kat-ion"]
while not(keywords.__contains__(cl_charge)):
    print("Keyword is not defined. Please choose one of the predefined keywords as listed below: ")
    cl_charge = input("all: just claudins\n"
                    "all-channels: all channel forming claudins\n"
                    "an-ion: an-ion-channels with single or double pos charge (pospos, posneu)\n"
                    "kat-ion: kat-ion-channels with single or double negative charge (negneg, negneu, neuneg)\n"
                    "kat-an-ion: kat-ion channels with low an-ion permability (posneg)\n"
                    "all-kat-ion: all kat-ion channels\n")

user_restriction = input("Please indicate level of filter:\n"
                         "low: all proteins matching the charged channel after the second C are found\n"
                         "high: only claudins with the correct structure in the first apical ring are chosen\n")
restriction = ["low", "high"]
while not (restriction.__contains__(user_restriction)):
    print("Please indicate level of filter:\n")
    user_restriction = input("low: all proteins matching the charged channel after the second C are found\n"
                             "high: only claudins with the correct structure in the first apical ring are chosen\n")

if user_restriction == "high":
    start_of_pattern = ".*W.+"
    end_of_pattern = ".+R.+"
elif user_restriction == "low":
    start_of_pattern = ".*"
    end_of_pattern = ".+"
if cl_charge == "all":
    cl_pattern = start_of_pattern+"[GSN][IL]W..[C].+[C]"+end_of_pattern
elif cl_charge == "all-channels":
    cl_pattern = start_of_pattern+"[GSN][LI]W..[C].{1,20}[C](([RHK]{1,2}[^DE])|([DE]{2})|(.[DE])|([DE][^RHK]))"+end_of_pattern
elif cl_charge == "an-ion":
    cl_pattern = start_of_pattern+"[GSN][IL]W..[C].{1,20}[C][RHK]{1,2}[^DE]"+end_of_pattern
elif cl_charge == "kat-ion":
    cl_pattern = start_of_pattern+"[GSN][IL]W..[C].{1,20}[C](([DE]{2})|([^RHK][DE])|([DE][^RHK]))"+end_of_pattern
elif cl_charge == "kat-an-ion":
    cl_pattern = start_of_pattern+"[GSN][IL]W..[C].{1,20}[C][RHK][DE]"+end_of_pattern
elif cl_charge == "all-kat-ion":
    cl_pattern = start_of_pattern+"[GSN][IL]W..[C].{1,20}[C](([DE]{2})|(.[DE])|([DE][^RHK]))"+end_of_pattern

#Write results into new file at directory of users choice
result_target = input("Please indicate where you want your results to be saved: \n")
target = open(result_target, "a", 1)

#Seperate names and sequences in input file before further processing
line = cl_file.read()
line1 = re.sub("\n", "", line)
output_prep = line1.split(">")
for val in output_prep:
    output_prep1 = val.split("]")
    output_name = output_prep1[0]
    output_seq = []
#Manipulate sequences into one line, to enable pattern matching
    for i in range(1, output_prep1.__len__()):
        output_seq.append(output_prep1[i])
    output_seq1 = re.sub("\d", "", str(output_seq))
    output_seq2 = re.sub(']', "", output_seq1)
    output_seq3 = re.sub('\[', "", output_seq2)
    output_seq4 = re.sub("\'", "", output_seq3)
    output_seq5 = re.sub(" ", "", output_seq4)
#Do pattern matching to find required sequences
    output_fin = re.search(cl_pattern, output_seq5, re.S | re.I | re.X)
#Write results to user-specified output file and console and then close it
    if output_fin:
        printable_name = ">" + output_name + "]" + "\n"
        printable_result = output_fin.group()+"\n"
        print(printable_name, printable_result)
        target.write(printable_name)
        target.write(printable_result)
target.close()
cl_file.close()