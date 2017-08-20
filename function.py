import re
sent_length = []
a = raw_input("Enter full path of file: ")
#a = raw_input("Enter full path of file: ")
text = open(a, 'r')
textread = text.read()
#Make lowercase to avoid double count of words
my_txt = textread.lower()
punct = re.split("[.?!]+",my_txt)
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
#Total word count
words = my_txt.split()
total_word_count = len(words)
#Find sentences
periods = my_txt.count(".")
question_mark = my_txt.count("?")
exclamation = my_txt.count("!")
sentences = periods + question_mark + exclamation
#Remove punctuation, count number of unique words w/o punctuation attached
no_punc = my_txt.replace(".","").replace("?","").replace("!","").replace(":","").replace(";","")
uniques = no_punc.split()
unique_words = set(uniques)
total_unique_words = len(unique_words)
#Print results
print "Total number of words: ",total_word_count
print "Number of unqiue words: ",total_unique_words
print "Number of sentences: ", sentences
print "Average sentence length:",avg_sent_length,"words"

from frequency import frequency_finder
