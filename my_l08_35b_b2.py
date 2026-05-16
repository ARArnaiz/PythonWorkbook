CONST_BOOKS = [
    {"rank": 1, "author": "Gabriel García Márquez", "title": "Cien años de soledad",
     "en": "One Hundred Years of Solitude", "year": 1967, "country": "CO", "price": 17},
    {"rank": 2, "author": "Julio Cortázar", "title": "Rayuela", "en": "Hopscotch", "year": 1963, "country": "AR",
     "price": 18},
    {"rank": 3, "author": "Mario Vargas Llosa", "title": "La ciudad y los perros", "en": "The Time of the Hero",
     "year": 1963, "country": "PE", "price": 15},
    {"rank": 4, "author": "Carlos Fuentes", "title": "La muerte de Artemio Cruz", "en": "The Death of Artemio Cruz",
     "year": 1962, "country": "MX", "price": 16},
    {"rank": 5, "author": "Juan Rulfo", "title": "Pedro Páramo", "en": "Pedro Páramo", "year": 1955, "country": "MX",
     "price": 16},
    {"rank": 6, "author": "Mario Vargas Llosa", "title": "Conversación en La Catedral",
     "en": "Conversation in the Cathedral", "year": 1969, "country": "PE", "price": 18},
    {"rank": 7, "author": "Gabriel García Márquez", "title": "El coronel no tiene quien le escriba",
     "en": "No One Writes to the Colonel", "year": 1961, "country": "CO", "price": 14},
    {"rank": 8, "author": "José Donoso", "title": "El obsceno pájaro de la noche", "en": "The Obscene Bird of Night",
     "year": 1970, "country": "AR", "price": 19},
    {"rank": 9, "author": "Guillermo Cabrera Infante", "title": "Tres tristes tigres", "en": "Three Trapped Tigers",
     "year": 1967, "country": "CU", "price": 17},
    {"rank": 10, "author": "Alejo Carpentier", "title": "Los pasos perdidos", "en": "The Lost Steps", "year": 1953,
     "country": "CU", "price": 16},
    {"rank": 11, "author": "Carlos Fuentes", "title": "La región más transparente", "en": "Where the Air Is Clear",
     "year": 1958, "country": "MX", "price": 15},
    {"rank": 12, "author": "Mario Vargas Llosa", "title": "La casa verde", "en": "The Green House", "year": 1966,
     "country": "PE", "price": 16},
    {"rank": 13, "author": "Julio Cortázar", "title": "Bestiario", "en": "Bestiary (stories)", "year": 1951,
     "country": "AR", "price": 14},
    {"rank": 14, "author": "Gabriel García Márquez", "title": "El otoño del patriarca",
     "en": "The Autumn of the Patriarch", "year": 1975, "country": "CO", "price": 16},
    {"rank": 15, "author": "Augusto Roa Bastos", "title": "Yo el Supremo", "en": "I, the Supreme", "year": 1974,
     "country": "PA", "price": 20},
    {"rank": 16, "author": "Miguel-Ángel Asturias", "title": "El Señor Presidente", "en": "Mister President",
     "year": 1946, "country": "GU", "price": 15},
    {"rank": 17, "author": "Manuel Puig", "title": "El beso de la mujer araña", "en": "Kiss of the Spider Woman",
     "year": 1976, "country": "AR", "price": 15},
    {"rank": 18, "author": "José Lezama Lima", "title": "Paradiso", "en": "Paradiso", "year": 1966, "country": "CU",
     "price": 22},
    {"rank": 19, "author": "Alejo Carpentier", "title": "El siglo de las luces", "en": "Explosion in a Cathedral",
     "year": 1962, "country": "CU", "price": 17},
    {"rank": 20, "author": "Ernesto Sábato", "title": "Sobre héroes y tumbas", "en": "On Heroes and Tombs",
     "year": 1961, "country": "AR", "price": 18},
]

def authors_lst_to_tuple(lst: list[dict[str, str | int]]) -> list[tuple]:
    return [ (item['author'], item['title'], item['price']) for item in lst ]

mytuple = (authors_lst_to_tuple(CONST_BOOKS))
# print(mytuple)

def tuple_to_dict(lst: list[tuple]) -> dict[str, dict]:
    return { title : {"author first name" : author.split(maxsplit=1)[0],
                      "author last name" : author.split(maxsplit=1)[1],
                      "price" : price}
             for author, title, price in lst }

# print(tuple_to_dict(mytuple))

def make_book_dict(books):

    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price}
            for name, title, price in books}

# print(make_book_dict(mytuple))
