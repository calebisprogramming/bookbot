def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = get_num_words(text)
    letters = get_sorted_list(count_letters(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the doucment\n")
    for letter in letters:
        print(f"The '{letter['char']}' character was found {letter['count']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["count"]

def get_sorted_list(counted_chars):
    char_list = []

    for char in counted_chars:
        char_list.append({ "char": char, "count": counted_chars[char] })
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def count_letters(text):
    words = text.lower().split()
    counted = {}

    for word in words:
        for i in range(0, len(word)):
            if word[i].isalpha():
                if word[i] in counted:
                    counted[word[i]] += 1 
                else:
                    counted[word[i]] = 1

    return counted

def get_num_words(text):
    words = text.split()
    return len(words)

def open_book(book_file):
    with open(book_file) as f:
        return f.read()

main()
