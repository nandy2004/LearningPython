def capital_words(text):
    words = text.split()
    result = []
    for word in words:
        if word[0].isupper():
            result.append(word)
    return result

# Example
sentence = "Python is Developed By Guido Van Rossum"
print(capital_words(sentence))
