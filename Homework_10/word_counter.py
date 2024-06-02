# Exercise 6: Count Words Function
# Write a function that counts the number of words in a sentence.

def word_counter(sentence):
    words = sentence.split()
    return len(words)

print(word_counter("In this sentence five words"))