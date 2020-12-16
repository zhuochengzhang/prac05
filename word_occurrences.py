word_occurrences_dict = {}
text_words = input("Text: ")
text_word_list = text_words.split(" ")
for item in text_word_list:
    if item in word_occurrences_dict:
        word_occurrences_dict[item] = (word_occurrences_dict[item] + 1)
    else:
        word_occurrences_dict[item] = 1
max_len = 0
for item in word_occurrences_dict.keys():
    if max_len < len(item):
        max_len = len(item)
for item in sorted(word_occurrences_dict.keys()):
    print('{:{}} = {}'.format(item, max_len,word_occurrences_dict[item]))

