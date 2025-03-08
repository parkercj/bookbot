def get_num_words(path_to_file):
    
    with open(path_to_file) as f:
        book_text = f.read()
    splitbook = book_text.split()
    WC = len(splitbook)
    wcstring = (f"Found {WC} total words")
    return wcstring

def get_num_characters(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()

    frequency_dict = {}
    for char in book_text.lower():
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict


    return [{k:f"{v}"} for k, v in sorted(dict_to_sort.items(), key=lambda x: x[1], reverse=True)]

def sort_list(dict_to_sort):
    results_list = []
    for char, count in sorted(dict_to_sort.items(), key=lambda x: x[1], reverse=True):
        
        char_dict = {char: count}
        results_list.append(char_dict)
    return results_list


    