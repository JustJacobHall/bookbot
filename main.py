def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        return words

def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_file_contents = file_contents.lower()
        
        counts = {}
        for character in lowered_file_contents:
            if character in counts:
                counts[character] += 1
            else:
                counts[character] = 1

        char_list = []
        for char, num in counts.items():
            if char.isalpha():
                char_list.append({"char": char, "num": num})

        return char_list

def sort_on(dict):
    return dict["num"]

def report():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count()} words found in the document")
        print(" ")

        prepared = character_count()
        prepared.sort(reverse=True, key=sort_on)
        
        for dict in prepared:
            print(f"The '{dict["char"]}' character was found {dict["num"]} times") 

        print("--- End report ---")