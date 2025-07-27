def length_of_last_word(sentence):
    words = sentence.strip().split()
    if words:
        return len(words[-1])
    else:
        return 0

# Example usage
print(length_of_last_word("Find the length of the last word")) 

