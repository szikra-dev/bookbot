def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    result = {}
    for char in text:
        c = char.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def format_char_dict(char_dict):
    dict_list = []
    for item in char_dict:
        dict_list.append({item: char_dict[item]})

    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def sort_on(dict):
    key = list(dict.keys())[0]
    return dict[key]