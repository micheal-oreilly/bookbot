with open("books/frankenstein.txt") as f:
    text = f.read()
    words = text.split()

def count_words(words):
    return len(words)

def count_letters(text):
    letters = {}
    for l in text:
        lowercase = l.lower()
        if lowercase in letters:
            letters[lowercase] += 1
        else:
            letters[lowercase] = 1
    return letters

count_words(words)

input_dictionary = count_letters(text)
result_list = list(input_dictionary.items())
#print(result_list)
result_list.sort()
print(result_list)
for item in result_list:
    print(item[0])
    if item[0].isalpha() == False:
        result_list.remove(item)
print(result_list)