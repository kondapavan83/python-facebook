def goat(sentence):
    changed_words=[]
    final_words=[]
    words=sentence.split()
    print(words)
    for word in words:
        if word[0].lower() in ('a','e','i','o','u'):
            changed_words.append((word+"ma").lower())
        else:
            fl=word[0]
            word=word.lstrip(fl)
            changed_words.append((word+fl+"ma").lower())

    print(changed_words)
    for index,word in enumerate(changed_words):
        final_words.append(word+'a'*(index+1))

    return(" ".join(final_words))

print(goat(input()))
