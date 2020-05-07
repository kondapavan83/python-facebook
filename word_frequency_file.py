filename=input("Please provide filename: ")
with open(f"{filename}","r") as file:
    lines=file.readlines()

words=[]
for line in lines:
    words.extend(line.split())

unique_words=set(words)
word_freq={}
for word in unique_words:
    word_freq[word]=words.count(word)

highest_freq=max(word_freq.values())

for k,v in word_freq.items():
    if v==highest_freq:
        print(k,v)
