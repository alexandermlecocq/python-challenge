import re

#Create a list for words and sentences and also counters for words, sentences and letters 
words = []
sentences = []
SentenceCount = 0
WordCount = 0
LetterCount = 0

#Reads a text file into a string called paragraph
with open("Paragraph.txt","r") as txtfile:
    paragraph = txtfile.read()

#Splits paragraph on various punctuation markers into a list of sentences
sentences = re.split("(?<=[.!?]) +", paragraph)

#For each sentence...
for currentsentence in sentences:
    #Split the sentence on spaces into a list of words
    words = re.split("\s+", currentsentence)
    
    #Increment the count of sentences
    SentenceCount += 1

    #For each word in that sentence
    for currentword in words:
        #Increment the word count
        WordCount += 1

        #Add the length of that word to the total number of letters
        LetterCount += len(currentword)

#Print paragraph analysis
print("Paragraph Analysis")
print("-----------------")
print(f"Word Count: {WordCount}")
print(f"Sentence Count: {SentenceCount}")
print(f"Average Letter Count: {(LetterCount/WordCount):.1f}")
print(f"Average Sentence Length: {(WordCount/SentenceCount):.1f}")