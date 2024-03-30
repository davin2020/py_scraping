#  PY script to process vtt files, remove any blank lines and timestamps,
# then add carragie returns after full stops - so transcript is easier to read

import re
import os

# finds timestamps in vtt file in the format - 00:00:19.850
TIMESTAMP_REGEX = "^\d\d:\d\d:\d\d\.\d\d\d"
# remove number from vtt file, in format from 1 to 9999
NUMBER_REGEX = "^[0-9]{1,4}$"


# NEXT try this against Trauma Conf files tha ti cant watch, but can get VTT for 
FOLDER = "test_process"

def proces_vtt(my_filename):
	print("my_filename :: ", my_filename)
	INPUT_FILENAME = FOLDER + "/" + my_filename

	# TODO change processed filename to .txt 
	(just_filename, ext) = os.path.splitext(my_filename)
	print("filename without ext : ", just_filename)

	OUTPUT_FILENAME = FOLDER + "/" +  "Processed_" + just_filename + ".txt"
	print("\n")
	print("filename INPUT_FILENAME ",  INPUT_FILENAME)
	print("filename OUTPUT_FILENAME ",  OUTPUT_FILENAME)

	input_file = open(INPUT_FILENAME, 'r')
	input_lines = input_file.readlines()
	 
	#  try diff WITH syntax?
	# with open(INPUT_FILENAME) as file:
	#   print(file.readlines())
	#   # output_file.writelines(input_lines)

	# print("...............")
	all_text = []

	#  check if copes with URLs  eg `xyz.com` in original transcript  - maybe serach for `x. ` ie extra space at end?
	# Strips the newline character
	for line in input_lines:

		if line.strip(): 
			# regex for timestamp
			line_with_number = re.findall(NUMBER_REGEX, line)
			# print("NUMBER_REGEX line_with_number: ", line_with_number)

			line_with_timestamp = re.findall(TIMESTAMP_REGEX, line)
			# print("line_with_timestamp: ", line_with_timestamp)

			if not line_with_timestamp:
				# some vtt also hvae sequential numbers eg 15 
				if not line_with_number:
					if "WEBVTT" not in line:
						all_text.append(line)


	# print("\ndone adding lines to all_text[] ")
	# print(all_text)   

	cleaned_text = []
	for item in all_text:
		line_with_space = item.replace("\n", " ")
		# need to match on full stop then space, otherwise elipses like .. get replaced
		sentence_with_newline = line_with_space.replace(". ", ". \n")
		cleaned_text.append(sentence_with_newline)

	print("done updating cleaned_text[]] ")

	# TODO NEXT - 
	# add 1 space to end of every line, and remove existing \n - or replace \n with space?
	# add carraige  ereturn after full stop 

	# # writing to file
	output_file = open(OUTPUT_FILENAME, 'w')
	output_file.writelines(cleaned_text)

	# output_file.writelines(input_lines)
	print("processed vtt file and saved output to txt file")
	print("output filename: ", OUTPUT_FILENAME)
	input_file.close()
	output_file.close()


#  add main here

# for filename in os.scandir(FOLDER):
for filename in os.listdir(FOLDER):
	if filename.endswith(".vtt"):
		proces_vtt(filename)
