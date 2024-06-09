def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"========Book report on {book_path}========")
    num_words = get_num_words(text)
    print(f"There are {num_words} found in the document\n")

    chars_dict = get_num_chars(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)

    for item in sorted_list:
        if not item["name"].isalpha():
            continue
        
        print(f"The '{item["name"]}' character was found {item["num"]} times")
    
    print("========End of Report========")

# returns the text in the book as a string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

# returns the total number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)

# returns a dict with the number of times each character appears in the text
def get_num_chars(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    
    return chars_dict

def sort_on(dict):
    return dict["num"]

# turns the dict into a list to be sorted
def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"name": char, "num": chars_dict[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()