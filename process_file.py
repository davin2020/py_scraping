
import re

# "[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?"
# MY_REGEX = "[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})"
MY_REGEX = "^\d\d:\d\d:\d\d\.\d\d\d"


def use_regex(input_text):
    pattern = re.compile(r"[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?", re.IGNORECASE)
    return pattern.match(input_text)

# Using readlines()
# TODO get filenames from a certain folder ie process all the fiels in a given folder
# NEXT try this against Trauma Conf files tha ti cant watch, but can get VTT for 
FILENAME = "HRT_Conf_Day4_Lee Harbour_141751067.vtt"
# FILENAME = "HRT_Conf_Day4_test.txt"
OUTPUT_FILENAME = "Processed_" + FILENAME

file1 = open(FILENAME, 'r')
Lines = file1.readlines()
 
all_text = []
count = 0
# Strips the newline character
# TODO remove the first line - WEBVTT - 
#  also doesnt cope with `..` or ulrs eg `xyz.com` in original transcript
for line in Lines:
	# nothing is being matched here!
	# x = re.findall("MY_REGEX", line)
	# # y = re.match(line)
	# print("found regex...", x)

	count += 1
	# if line is empty
	# if not line.isspace(): 
	if line.strip(): 
		# dont need to add okay text twice!
		# all_text.append(line)
		# o.write(line) 
		# regex for timestamp
		x = re.findall(MY_REGEX, line)
		
		if not x:
			print("found regex...", x)
			all_text.append(line)
	# some issue w indenting
	# x = re.findall(MY_REGEX, line)
	# # y = re.match(line)
	# print("found regex...", x)
	# if not x:
	# 	all_text.append(line)
# print("Line_{}: {}".format(count, line.strip()))

print("ready")
print(all_text)   

cleaned_text = []
for item in all_text:
	cleaned = item.replace("\n", " ")
	cleaned2 = cleaned.replace(".", ".\n")
	cleaned_text.append(cleaned2)


# final_cleaned_text = []
# for item2 in cleaned_text:
# 	cleaned2 = item2.replace(".", ".\r")
# 	final_cleaned_text.append(cleaned2)

# print(final_cleaned_text)
# Output: "Hello,World!"	

# TODO NEXT - 
# add 1 space to end of every line, and remove existing \n - or replace \n with space?
# add carraige  ereturn after full stop 

# # writing to file
file1 = open(OUTPUT_FILENAME, 'w')
file1.writelines(cleaned_text)
file1.close()