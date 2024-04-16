# Python script to process .vtt transcript files from videos, remove any blank lines and timestamps,
# then add carraige returns after full stops of each sentence, so transcript is easier to read.

import re
import os

# Best to compile regex only once, ouside of any loops, then can use it multiple times inside loops
# Finds timestamps in vtt file in the format - 00:00:19.850 - ie under 1 hr in duration
# TODO what would 1 hr+ video timestamp look like?
TIMESTAMP_REGEX = re.compile("^\d\d:\d\d:\d\d\.\d\d\d")
# carat ^ mean beginning of line

# remove sequential number from vtt file, in format from 1 to 9999
NUMBER_REGEX = re.compile("^[0-9]{1,4}$")

# adjust name of folder as needed - TODO could pass in folder name as param to script
FOLDER = "files_to_process"

def proces_vtt(my_filename):
	INPUT_FILENAME = FOLDER + "/" + my_filename
	(just_filename, extention) = os.path.splitext(my_filename)

	# changed processed filename to .txt - 
	# caveat - any existing files with same name will be overwritten
	OUTPUT_FILENAME = FOLDER + "/" +  "Processed_" + just_filename + ".txt"

	input_file = open(INPUT_FILENAME, 'r')
	input_lines = input_file.readlines()
	 
	all_text = []

	# process each line of input file, saving wanted text to a list all_text[]
	for line in input_lines:
		# strip removes newline char (but print adds them back)
		if line.strip(): 
			# regex for matching against numbers, or timestamp 
			line_with_number = NUMBER_REGEX.match(line)
			# print("NUMBER_REGEX line_with_number: ", line_with_number)
			line_with_timestamp = TIMESTAMP_REGEX.match(line)      
			# print("line_with_timestamp: ", line_with_timestamp)

			if not line_with_timestamp:
				# some vtt also hvae sequential numbers eg 15 
				if not line_with_number:
					if "WEBVTT" not in line:
						all_text.append(line)

	# formatting text by adding newline after each sentence, so its not all one large paragraph
	formatted_text = []
	for item in all_text:
		line_with_space = item.replace("\n", " ")
		# need to match on full stop then space, otherwise elipses like .. get replaced new with newline
		sentence_with_newline = line_with_space.replace(". ", ". \n")
		formatted_text.append(sentence_with_newline)

	# write formtated text to file
	output_file = open(OUTPUT_FILENAME, 'w')
	output_file.writelines(formatted_text)

	# output_file.writelines(input_lines)
	print("\nProcessed .vtt file and saved output to .txt file")
	print("Output filename: ", OUTPUT_FILENAME)
	input_file.close()
	output_file.close()


def main():
	for filename in os.listdir(FOLDER):
		if filename.endswith(".vtt"):
			proces_vtt(filename)


if __name__ == '__main__':
	main()
    