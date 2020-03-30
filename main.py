
simple_number = 10
print('Int variable: ', simple_number)

best_language = 'Python'
print('String variable: ', best_language)

if type(simple_number) != type(best_language):
    print('Compare variables with different types')

number_as_string = str(simple_number)
print('Convert number to string ', number_as_string)

numbers_list = [10, 2, 23, 4, 15, 61, 27, 8, 92, 10]
print('Create list: ', numbers_list)

numbers_list.append(100)
print('Add 100 at the end of the list: ', numbers_list)

numbers_list.insert(2, 500)
print('Add 500 to third position of the list: ', numbers_list)

numbers_list.pop(0)
print('Remove first element of the list: ', numbers_list)

numbers_list.pop(1)
print('Remove second element of the list: ', numbers_list)

numbers_list.reverse()
print('Reverse list: ', numbers_list)

elements_count = len(numbers_list)
print('Count elements in the list: ', elements_count)

list_copy = numbers_list.copy()
print('Copy list: ', list_copy)


def bubble_sort(list):
    copy = list.copy()
    length = len(copy)
    for i in range(length):
        for j in range(length - 1):
            if copy[i] < copy[j]:
                copy[i] = copy[i] + copy[j]
                copy[j] = copy[i] - copy[j]
                copy[i] = copy[i] - copy[j]
    return copy


print('Sort list with bubble sort: ', bubble_sort(numbers_list))

print('Sort list with sorted function: ', sorted(numbers_list))

print('Sort list with .sort() function: ', numbers_list.sort())

test_string = 'This is a test string for Internship Onix for python'
words = list(test_string.split(' '))
print('Words from test string: ', words)

unique_words = list(set(words))
print('Unique words from test string: ', unique_words)

unique_words_sorted = sorted(unique_words, reverse=True)
print('Unique words sorted in reverse: ', unique_words_sorted)

dictionary = {
    'id': 1,
    'task': 2,
    'description': 'Python homework'
}
print('Dictionary created: ', dictionary)

dictionary['destination'] = 'Onix'
print('Destination key added: ', dictionary)

print('Get description value from dict: ', dictionary['description'])

dictionary.pop('description')
print('Delete description from dict: ', dictionary)

print('Dictionary keys: ', dictionary.keys())

print('Dictionary values: ', dictionary.values())

sorted_by_keys = {}
for key in sorted(dictionary.keys()):
    sorted_by_keys[key] = dictionary[key]

print('Dictionary sorted by keys: ', sorted_by_keys)

sorted_ba_values = {}
for key, value in sorted(sorted_by_keys.items(), key=lambda item: str(item[1])):
    sorted_ba_values[key] = value

print('Dictionary sorted by values: ', sorted_ba_values)
