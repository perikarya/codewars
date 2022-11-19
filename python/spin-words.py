def spin_words(sentence):
    for word in sentence.split():
        if len(word) >= 5:
            sentence = sentence.replace(word, word[::-1])
    return sentence
