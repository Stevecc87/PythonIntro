#text file
user_input = raw_input("Enter full path of file: ")
text = open(user_input, 'r')
textread = text.read()
#Make lowercase to avoid double count of words
my_txt = textread.lower()
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
