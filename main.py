from curses.ascii import isalpha
import sys
from stats import get_num_words, get_char_count, format_char_dict


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    words_count = get_num_words(text)
    chars_count_dict = get_char_count(text)
    formated_chars_dict = format_char_dict(chars_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("-------- Character Count --------")
    for dict in formated_chars_dict:
        key = list(dict.keys())[0]
        if isalpha(key):
            print(f"{key}: {dict[key]}")
    print("============= END ===============")


main()