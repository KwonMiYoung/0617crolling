from collections import Counter
import string
import collections
import re

INPUT_FILE_NAME = 'cleaned_output1.txt'
textfile = open(INPUT_FILE_NAME, 'r')
text = textfile.read()

num = 0

OUTPUT_FILE_NAME = 'keyword1.txt'
write_file = open(OUTPUT_FILE_NAME, 'w')


text=sorted(
        sorted(
            Counter(text.split()).most_common(30),  # most number of words name
            key=lambda pair: pair[0],
            reverse=True
        ),  # sorted2 word name
        key=lambda pair: pair[1],
        reverse=True
    )  # sorted1 number of words

write_file.write(str(text))

textfile.close()
write_file.close()