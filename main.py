<<<<<<< HEAD
from stats import word_count, char_count, func3

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    print(f"{num_words} words found in the document")
    print(char_dict)
    result = func3(char_dict)
    print(result)
=======
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = countem(text)
    print(f"{num_words} words found in the document")
>>>>>>> origin

def get_book_text(path):
    with open(path) as f:
        return f.read()

<<<<<<< HEAD
=======
def countem(text):
    words = text.split()
    return len(words)

>>>>>>> origin
main()



<<<<<<< HEAD
=======

>>>>>>> origin
