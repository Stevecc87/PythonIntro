import re
sent_length = []
text = open("U:/PythonScirpts/Test1.txt",'r')
textread = text.read()
print textread
# #Split words into sentences by seperating on puntuation
# punct = re.split("[.?!]+",textread)
# #If the last sentence in the list is blank, remove that sentence from the list
# if punct[-1] == "":
#     del punct[-1]
# else:
#     pass
# for i in punct:
#     sep = i.split()
#     lengths = len(sep)
#     sent_length.append(lengths)
# avg_sent_length = sum(sent_length)/(len(sent_length))
# print "Average sentence length:",avg_sent_length,"words"
