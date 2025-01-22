def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        letters = count_characters(file_contents)
        
        sorted_characters = []
        for l in letters:
            sorted_characters.append({"char": l, "num": letters[l]})
        sorted_characters.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} found in document")
        for letter in sorted_characters:
            if letter["char"].isalpha():
                print(f"The '{letter["char"]}'character was found {letter["num"]} times")
        #print(f"The {" "} was found {letters["e"]} times")

    

def sort_on(dict):
    return dict["num"]

def count_characters(book):
    text = book.lower()
    characters = {}
    for t in text:
        if t in characters:
            characters[t] += 1
        else:
            characters[t] = 1
    #print(characters)
    return characters

if __name__ == "__main__":
    main()