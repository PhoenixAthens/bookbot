import sys
from stats import word_counter, character_counter, sort_dict_of_char_count

def get_book_text(path:str):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = word_counter(get_book_text(book_path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_of_chars = character_counter(get_book_text(book_path))
    list_from_dict_of_chars = sort_dict_of_char_count(dict_of_chars)
    for i in list_from_dict_of_chars:
        if(i['char'].isalpha()):
            print(f"{i['char']}: {i['num']}")

    # print(dict_of_chars)


    # for c in dict_of_chars:
    #     print(f"'{c}': '{dict_of_chars[c]}'")


main()
