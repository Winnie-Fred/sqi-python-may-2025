book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
components = book_info.split(" ; ")
author, book_title, year_published, isbn, no_of_pages, cost = components
author = author.title()
book_title = book_title.strip().title()
isbn = isbn.replace("ISN", "ISBN")
# cost = "{0:.2f}".format(cost)
cost = "₦{0:.2f}".format(float(cost))

print(f"""The book {book_title} was written by {author} and published in {year_published}.
It has {no_of_pages} pages and {isbn} and costs {cost}.""")

print("""The book {} was written by {} and published in {}.
It has {} pages and {} and costs {}.""".format(book_title, author, year_published, no_of_pages, isbn, cost))


# age = 5
# is_student = True
# name = "Awwal"
# height = 4.65
# print("I am {2}. It is {0} that I am a student. I am {1} years old, my height is {3}m".format(is_student, age, name, height))


# radius = "45.2345"
# print("{0:.2f}".format(radius))
# print("{1:.2f}".format(radius, 32.789))
# print("{0:.2f}".format(radius, 32.789))
# print(type("{0:.2f}".format(radius, 32.789)))


# radius = 45.2762
# print(round(radius))
# print(type(round(radius)))

