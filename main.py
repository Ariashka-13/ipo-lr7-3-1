books = {
    1 : {"title": "Горе от ума", "author": "А. Грибоедов", "year": "1825"},
    2 : {"title": "Ревизор", "author": "Н. Гоголь", "year": "1836"},
    3 : {"title": "Капитанская дочка", "author": "А. Пушкин", "year": "1836"},
    4 : {"title": "Вишневый сад", "author": "А. Чехов", "year": "1904"},
    5 : {"title": "Яма", "author": "Ф. Куприн", "year": "1916"},
}

for i, book in books.items():
    print(f"Книга {i}".center(30, '-')) 
    print(f"Название: {book['title']}, Автор: {book['author']},") 
    print(f"{book['year']}".center(30, '-'))
