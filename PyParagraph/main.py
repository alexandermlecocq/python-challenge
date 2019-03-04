import re

words = []
sentences = []
SentenceCount = 0
WordCount = 0
LetterCount = 0

with open("Paragraph.txt","r") as txtfile:
    paragraph = txtfile.read()

sentences = re.split("(?<=[.!?]) +", paragraph)

for currentsentence in sentences:
    words = re.split("\s+", currentsentence)
    SentenceCount += 1
    for currentword in words:
        WordCount += 1
        LetterCount += len(currentword)


print("Paragraph Analysis")
print("-----------------")
print(f"Word Count: {WordCount}")
print(f"Sentence Count: {SentenceCount}")
print(f"Average Letter Count: {(LetterCount/WordCount):.1f}")
print(f"Average Sentence Length: {(WordCount/SentenceCount):.1f}")