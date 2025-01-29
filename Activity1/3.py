def wordCount(t):
    """Count words and their line occurrences in a text file."""
    word_dict = {}
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, 1):
            words = line.lower().split()
            for word in words:
                if word not in word_dict:
                    word_dict[word] = [line_num]
                elif line_num not in word_dict[word]:
                    word_dict[word].append(line_num)
    return word_dict