def word_counter(text:str):
    words = text.split()
    return len(words)

def character_counter(text:str):
    dict_of_characters = {}
    for i in text:
        i = i.lower()
        if i in dict_of_characters:
            dict_of_characters[i] +=1
        else:
            dict_of_characters[i] = 1
    return dict_of_characters

def sort_order(dict):
    return dict['num']

def sort_dict_of_char_count(dict):
    list_of_dicts = []
    for i in dict:
        list_of_dicts.append({'char':i,'num':dict[i]})
    list_of_dicts.sort(reverse=True,key=sort_order)
    return list_of_dicts;
