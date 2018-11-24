import sys
from nltk import tokenize
import os

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print("File path {} does not exist. Exiting...".format(input_file))
    sys.exit()
count = 0

sentences = []
# chap_count = 0
with open(input_file, 'rb') as fp:
    for line in fp:
        line = line.decode("ISO-8859-1")
        if line not in ['\n', '\r\n']:
            # count += 1
            # for sent in tokenize.sent_tokenize(line):
                # print(sent)
            sentences.extend(tokenize.sent_tokenize(line))

# for i in range(len(sentences)):
#     if ("CHAPTER" in sentences[i]):
#         print(i)
#         del sentences[i]
# for i in sentences:
#     if ("CHAPTER " in i) or ("Harry Potter and the Sorcerer's Stone" == i):
#         sentences.remove(i)

output_file = sys.argv[2]
cars=["Audi\n","Bentely\n","Toyota\n"]
of=open(output_file,mode="w", encoding='utf-8')
for sent in sentences:
    of.write(sent + "\n")
