def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        max = 0
        for word in words:
            if len(word) > max:
                max = len(word)
                words_max = []
                words_max.append(word)
            elif len(word) == max:
                words_max.append(word)
        return words_max

print(longest_word('test.txt'))

