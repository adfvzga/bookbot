def get_book_text(book_path):
    with open(book_path) as p:
        text = p.read()
        return text


def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count


def count_characters(text):
    character_dict = {}
    text = text.lower()
    for char in text:
        if char in character_dict.keys():
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict


def dict_to_sorted_list(char_dict):
    list_dicts = []
    for char in char_dict.keys():
        if char.isalpha():
            new_dict = {}
            new_dict["char"] = char
            new_dict["num"] = char_dict[char]
            list_dicts.append(new_dict)
    list_dicts.sort(key=lambda d: d["num"], reverse=True)
    return list_dicts

    