
a = raw_input("Enter full path of file: ")
#a = raw_input("Enter full path of file: ")
text = open(a, 'r')
textread = text.read()
#Make lowercase to avoid double count of words
my_txt = textread.lower()
#Total word count
no_punc =my_txt.replace(".","").replace("?","").replace("!","").replace(":","").replace(";","")
words = no_punc.split()
print words
word_dic = {}
for i in words:
    word_dic[i] = word_dic.get(i,0) + 1
sorted_dic = sorted(word_dic.items(),key=lambda x: x[1],reverse=True)
print sorted_dic
for j in sorted_dic:

    print j

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
