def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


print(longest_word("Write a program to find the longest word")) 