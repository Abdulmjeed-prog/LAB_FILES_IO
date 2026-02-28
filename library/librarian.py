import json
import os

library = {
    
}


def add_book(library,title, author, isbn):
    if isbn not in library:
        library[isbn] = {
        "title": title,
        "author": author,
        "available": True
        }
        print("Added")
    else:
        print("Book is already in the library")
    
        

def remove_book(library,isbn:str):
    
    if isbn in library:
        del library[isbn]
        print("Done")
    else:
        print("the book is not available")

def check_out_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = False
        print("Done")
    else:
        print("not available")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        print("Done")
    else:
        print("not available")

def display_books(library):
    for num, isbn in enumerate(library, start=1):
        book = library[isbn]
        if book["available"] == True:
            msg = "Yes"
        else:
            msg = "No"
        print(f"{num}- {book['title']} | Author: {book['author']} | ISBN: {isbn} | Available Online: {msg}")


def save_library(library):
    """Save to JSON file."""
    with open('library.json', 'w', encoding='utf-8') as f:
        json.dump(library, f, indent=2)
    

def load_library(library):
    """Load from JSON file."""
    if os.path.exists('library.json'):
        try:
            with open('library.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                library.clear()
                library.update(data)
            
        except:
            pass 


load_library(library)
