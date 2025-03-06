import sys
from stats import get_num_words, count_chars, sortdict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        num_words = get_num_words(content)
        print(f'{num_words} words found in the document')
        chars_dict = count_chars(content)
        sorted_dict = sortdict(chars_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f'Found {num_words} total words')
        print("--------- Character Count -------")
        for i in sorted_dict:
            if i["key"].isalpha():
                print(f'{i["key"]}: {i["val"]}')

                
        print("============= END ===============")


main()

