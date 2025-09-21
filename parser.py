import json
from csv import DictReader

from files import CSV_FILE_PATH, JSON_FILE_PATH

fields_books = ["Title", "Author", "Pages", "Genre"]
fields_users = ["name", "gender", "address", "age"]

def get_books():
    books = []
    with open(CSV_FILE_PATH, newline='', encoding='utf-8') as f:
        reader = DictReader(f)
        for row in reader:
            book = {key: row[key] for key in fields_books}
            books.append(book)
    return books

def get_users():
    names = []
    with open(JSON_FILE_PATH, encoding="utf-8") as f:
        users = json.load(f)
        for row in users:
            user_card = {key: row[key] for key in fields_users}
            user_card["books"] = []
            names.append(user_card)
    return names

def distribute_books(books,names):
    user_count = len(names)
    for i, book in enumerate(books):
        user = names[i % user_count]
        user["books"].append(book)
    return names

def save_results(names):
    data_to_save = names
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4)

def main():
    books = get_books()
    users = get_users()
    distribute_books(books, users)
    save_results(users)


if __name__ == "__main__":
    main()
