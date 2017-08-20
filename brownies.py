import re
sent_length = []
text = open("U:/PythonScirpts/Test1.txt",'r')
textread = text.read()
#Split words into sentences by seperating on puntuation
punct = re.split("[.?!]+",textread)
#If the last sentence in the list is blank, remove that sentence from the list
if punct[-1] == "":
    del punct[-1]
else:
    pass
for i in punct:
    sep = i.split()
    lengths = len(sep)
    sent_length.append(lengths)
avg_sent_length = sum(sent_length)/(len(sent_length))
print "Average sentence length:",avg_sent_length,"words"





# #Total word count
# words = my_txt.split()
# total_word_count = len(words)
# #Find sentences
# periods = my_txt.count(".")
# question_mark = my_txt.count("?")
# exclamation = my_txt.count("!")
# sentences = periods + question_mark + exclamation
# #Remove punctuation, count number of unique words w/o punctuation attached
# no_punc = my_txt.replace(".","").replace("?","").replace("!","").replace(":","").replace(";","")
# uniques = no_punc.split()
# unique_words = set(uniques)
# total_unique_words = len(unique_words)
# #Print results
# print "Total number of words: ",total_word_count
# print "Number of unqiue words: ",total_unique_words
# print "Number of sentences: ", sentences
