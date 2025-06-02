titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"


def add_book(title, author):
    titles.append(title)
    authors.append(author)
    statuses.append("Unread")
    print("The book is added.")


def mark_as_read(title):
    for i in range(len(titles)):
        if titles[i] == title:
            statuses[i] = "Read"
            print("The book has been read.")
        else:
            print("Error. The book is not found.")


def mark_as_unread(title):
    for i in range(len(titles)):
        if titles[i] == title:
            statuses[i] = "Unread"
            print("The book has not been read.")
        else:
            print("Error. The book is not found.")


def search_book(keyword):
    writer = ""
    wrote = ""
    word = keyword.casefold()
    if word in titles:
        for i in range(len(titles)):
            if titles[i] == word:
                wrote = titles[i]
                writer = authors[i]
                print(f"{writer} - '{wrote}'")
            elif authors[i] == word:
                wrote = titles[i]
                writer = authors[i]
                print(f"{writer} - '{wrote}'")
            else:
                print("No books found.")


def list_books():
    writer = ""
    wrote = ""
    status = ""

    for i in range(len(titles)):
        writer = authors[i]
        wrote = titles[i]
        status = statuses[i]
        print(f"{writer} - '{wrote}' : {status}")


def suggest_book():
    import random

    book_list = []

    for i in range(len(statuses)):
        if statuses[i] == "Unread":
            book_list.append(i)

    if not book_list:
        print("No unread books left.")
    else:
        authors_list = []
        titles_list = []

        for i in book_list:
            for j in range(len(authors)):
                authors_list.append(authors[int(i)])
            for k in range(len(titles)):
                titles_list.append(titles[int(i)])
        matrix_of_books = []

        for i in authors_list:
            for j in titles_list:
                matrix_of_books.append([i, j])

        random_book = random.choice(matrix_of_books)
        some_book = f"'{random_book[0]}' - {random_book[1]}"
        print(some_book)


def delete_book(title):
    if title in titles:
        index = titles.index(title)
        del titles[index]
        del authors[index]
        del statuses[index]
        print("The book has been deleted.")
    else:
        print("Book not found.")


def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()
