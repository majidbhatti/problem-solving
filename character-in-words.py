def findWordsContaining(words, x):
    indices = []
    for w, word in enumerate(words):
        word_half_len = len(word)
        for i in range(word_half_len):
            if word[i] == x:
                indices.append(w)
                break
    return indices


print(findWordsContaining(["ekcpg", "pdknua", "fot", "janppw", "ofomkfvx"], 'g'))
