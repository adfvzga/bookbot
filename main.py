from stats import get_book_text, count_words, count_characters, dict_to_sorted_list
import sys


def main():
    if len(sys.argv) == 2:
        # Get data and calculate
        book_path = sys.argv[1]
        num_words = count_words(get_book_text(book_path))
        char_dict = count_characters(get_book_text(book_path))
        sorted_list = dict_to_sorted_list(char_dict)
        # Print report 
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dictionary in sorted_list:
            print(f"{dictionary["char"]}: {dictionary["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()