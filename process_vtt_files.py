#  PY script to process vtt files, remove any blank lines and timestamps,
# then add carragie returns after full stops - so transcript is easier to read

import re
import os

# finds timestamps in the format - 00:00:19.850
TIMESTAMP_REGEX = "^\d\d:\d\d:\d\d\.\d\d\d"
# REGEX_2 = "^.*$"
NUMBER_REGEX = "^[0-9]{1,4}$"
# ^[0-9]{1,3}$


# def use_regex(input_text):
#     pattern = re.compile(r"[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?", re.IGNORECASE)
#     return pattern.match(input_text)

# Using readlines()
# TODO get filenames from a certain folder ie process all the fiels in a given folder
# NEXT try this against Trauma Conf files tha ti cant watch, but can get VTT for 
FOLDER = "misc_test"

ext = ('.vtt', '.txt')

# FILENAME = "C:\wamp64\www\python\py_scraping\to_process\short_HRT_day1_melissa_ramos.vtt"

# FILENAME = "short_HRT_day1_melissa_ramos.vtt"
# FILENAME = "short_HRT_day1_michelle_sands.vtt"



def proces_vtt(filename):

	INPUT_FILENAME = FOLDER + "/" + filename
	# TODO change processed filename to .txt 
	OUTPUT_FILENAME = FOLDER + "/" +  "Processed_" + filename
	print("\n")
	print("filename INPUT_FILENAME ",  INPUT_FILENAME)
	print("filename OUTPUT_FILENAME ",  OUTPUT_FILENAME)

	input_file = open(INPUT_FILENAME, 'r')
	input_lines = input_file.readlines()
	 
	# with open(INPUT_FILENAME) as file:
	#   print(file.readlines())
	#   # output_file.writelines(input_lines)

	# print("...............")
	all_text = []
	# count = 0

	# TODO - only process files w .vtt extension 

	# Strips the newline character
	# TODO remove the first line - WEBVTT - 
	#  also doesnt cope with `..` or ulrs eg `xyz.com` in original transcript  - maybe serach for `x. ` ie extra space at end?
	for line in input_lines:
		# count += 1
		
		# if not line.isspace(): # if line is space
		# if line is empty

		if line.strip(): 
			# if "WEBVTT" not in line:
			# 	all_text.append(line)
			# regex for timestamp
			line_with_number = re.findall(NUMBER_REGEX, line)
			# print("NUMBER_REGEX line_with_number: ", line_with_number)

			line_with_timestamp = re.findall(TIMESTAMP_REGEX, line)
			# print("line_with_timestamp: ", line_with_timestamp)

			if not line_with_timestamp:
				# print("didnt find regex...", x)
				# some vtt also hvae sequential numbers eg 15 
				if not line_with_number:
					if "WEBVTT" not in line:
						all_text.append(line)
			# print("...", line)

	# ?? the end of the file is not being processed? - DONT compare long input file w short output file!

	# print("\ndone adding lines to all_text[] ")
	# print(all_text)   

	cleaned_text = []
	for item in all_text:
		line_with_space = item.replace("\n", " ")
		# need to match on full stop then space, otherwise elipses like .. get replaced
		sentence_with_newline = line_with_space.replace(". ", ". \n")
		cleaned_text.append(sentence_with_newline)

	print("done updating cleaned_text[]] ")
	# print(cleaned_text)  


	# print(cleaned_text)

	# TODO NEXT - 
	# add 1 space to end of every line, and remove existing \n - or replace \n with space?
	# add carraige  ereturn after full stop 

	# # writing to file
	output_file = open(OUTPUT_FILENAME, 'w')
	output_file.writelines(cleaned_text)

	# output_file.writelines(input_lines)
	print("processed vtt file and saved output to txt file")
	input_file.close()
	output_file.close()


# proccess just one named file as a test
# filename = "short_HRT_day1_pete_williams.vtt"
# proces_vtt(filename)

# for filename in os.scandir(FOLDER):
for filename in os.listdir(FOLDER):
	# nd filename.extension == ".vtt":
	# TODO - how to exclude "Procssed" files?
	if filename.endswith(ext):
		proces_vtt(filename)
		print("processed file: ", filename)
    # if filename.is_file():
    #     print(filename.path)
    #     print(filename.extension)
