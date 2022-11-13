def unique_sort(sentence):
    words = []
    sentence = sentence.split(" ")
    for word in sentence:
        if word.lower() not in words:
            words.append(word.lower())
    
    words.sort()

    new_sentence = " ".join(words)

    return new_sentence

