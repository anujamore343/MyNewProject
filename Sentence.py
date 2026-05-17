#write a function take sentence as an input & check word count in it
def word_count(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
count = word_count(sentence)
print("Number of words in the sentence is:", count)