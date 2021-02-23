# PCAP 2.3.1.18 Your own split
# Write your own function,which behaves almost exactly like the original split function

def mysplit(strng):

    split_words = []
    word = ''

    for char in strng:
        if char != ' ':
            word += char
        else:
            if word:
                split_words.append(word)
            word = ''
    split_words.append(word)

    for w in split_words:
        if w == '':
            split_words.remove(w)

    return split_words

print(mysplit("To be or n789,ot to be, that is the question"))