from stats import get_num_words,sort_characters_by_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    # bookdata = get_book_text('/home/puneeth/python_projects/bookbot/books/frankenstein.txt')
    bookdata = get_book_text(book_path)

    num_words = get_num_words(bookdata)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")

    char_count = {}
    for char in bookdata.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    sorted_chars = sort_characters_by_count(char_count)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()


