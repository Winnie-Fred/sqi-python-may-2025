# Data Type         Is ordered?         Is Indexed?     Is Mutable?     Allows Duplicates?
# String                yes                 yes             no                  yes
# List                  yes                 yes             yes                 yes
# Tuple                 yes                 yes             no                  yes
# Dictionary            yes             yes, but with keys  yes         allows duplicate values, not keys
# Set                   no                  no        yes, except frozen sets   no             


# streaming_services = {"Hulu", "Netflix", "Prime Video", "Netflix", "Showmax", "Disney+"}
# print(streaming_services)

# streaming_services = set()

# print(streaming_services)


# text = "Hello"
# print(set(text))

# nums = [23, 67, 567.67, 123, 67, 990]
# print(set(nums))
# print(len(set(nums)))


# streaming_services = {"Hulu", "Netflix", "Prime Video", "Netflix", "Showmax", "Disney+"}
# print(type(streaming_services))

# ==============================================False and 0, True and 1==============================================
# my_set = {1, 4, 8, True}
# print(my_set)

# my_set = {0, 4, False, 8, True}
# print(my_set)

# ==============================================False and 0, True and 1==============================================



# ==============================================.ADD()==============================================
# streaming_services = {"Hulu", "Netflix", "Prime Video", "Netflix", "Showmax", "Disney+"}
# streaming_services.add("HBO Max")
# # streaming_services.add("Hulu")
# print(streaming_services)
# ==============================================.ADD()==============================================


# ==============================================.UPDATE() and .UNION()==============================================
# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = {"Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"}
# phone_brands.update(other_phone_brands)
# print(phone_brands)
# print(other_phone_brands)

# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = {"Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"}
# all_brands = phone_brands.union(other_phone_brands)
# print(all_brands)
# print(phone_brands)
# print(other_phone_brands)

# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = {"Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"}
# even_more_phone_brands = {"Oppo", "LG", "Google Pixel", "Nothing"}

# all_brands = phone_brands.union(other_phone_brands).union(even_more_phone_brands)
# print(all_brands)


# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = ["Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"]
# even_more_phone_brands = ("Oppo", "LG", "Google Pixel", "Nothing")

# all_brands = phone_brands.union(other_phone_brands).union(even_more_phone_brands)
# print(all_brands)

# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = {"Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"}
# even_more_phone_brands = {"Oppo", "LG", "Google Pixel", "Nothing"}

# phone_brands.update(other_phone_brands)
# phone_brands.update(even_more_phone_brands)
# print(phone_brands)

# ==================SHORTHAND METHOD==================
# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = {"Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"}
# even_more_phone_brands = {"Oppo", "LG", "Google Pixel", "Nothing"}

# all_brands = phone_brands | other_phone_brands | even_more_phone_brands
# print(all_brands)


# phone_brands = {"Samsung", "Apple", "Huawei", "Nokia", "Tecno", "Vivo"}
# other_phone_brands = ["Infinix", "iTel", "Redmi", "Motorolla", "Multilinks"]
# even_more_phone_brands = ("Oppo", "LG", "Google Pixel", "Nothing")

# all_brands = phone_brands | other_phone_brands | even_more_phone_brands
# print(all_brands)
# ==================SHORTHAND METHOD==================

# ==============================================.UPDATE() and .UNION()==============================================


# ==============================================.INTERSECTION() AND .INTERSECTION_UPDATE()==============================================
# football_players = {"Yamal", "Osimhen", "Messi", "Ronaldo"}
# more_football_players = {"Ibrahimovic", "Kaka", "Lukaku", "Mbappe"}

# football_players.intersection_update(more_football_players)
# print(football_players)

# football_players = {"Yamal", "Kaka", "Osimhen", "Messi", "Ronaldo"}
# more_football_players = {"Ibrahimovic", "Kaka", "Messi", "Lukaku", "Mbappe"}
# even_more_football_players = {"Oshuala", "Modric", "Kaka", "Moses", "Mikel Obi"}

# intersection = football_players.intersection(more_football_players).intersection(even_more_football_players)
# print(intersection)


# ==================SHORTHAND METHOD==================
# football_players = {"Yamal", "Kaka", "Osimhen", "Messi", "Ronaldo"}
# more_football_players = {"Ibrahimovic", "Kaka", "Messi", "Lukaku", "Mbappe"}
# even_more_football_players = {"Oshuala", "Modric", "Kaka", "Moses", "Mikel Obi"}

# intersection = football_players & more_football_players & even_more_football_players
# print(intersection)

# football_players = ("Yamal", "Kaka", "Osimhen", "Messi", "Ronaldo")
# more_football_players = ["Ibrahimovic", "Kaka", "Messi", "Lukaku", "Mbappe"]
# even_more_football_players = {"Oshuala", "Modric", "Kaka", "Moses", "Mikel Obi"}

# intersection = football_players & more_football_players & even_more_football_players
# print(intersection)
# ==================SHORTHAND METHOD==================

# ==============================================.INTERSECTION() AND .INTERSECTION_UPDATE()==============================================

# ==============================================.DIFFERENCE() AND .DIFFERENCE_UPDATE()==============================================
# body_creams = {"Nivea", "Dove", "Fine", "Dudu Osu", "Caro Tone", "Miss Cherry","Kids and Things", "E45", "Johnsons"}
# more_creams = {"Jergens", "Pearls", "Dudu Osu", "E45", "Baby Face"}
# # some_more_creams = {"Vaseline", "Ori", "Dr. Rachel", "Skin Doctor"}

# body_creams.difference_update(more_creams)  # {"Nivea", "Dove", "Fine", "Caro Tone", "Miss Cherry","Kids and Things", "Johnsons"}
# print(body_creams)

# 5 - 2
# |||||


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)  # {"banana", "cherry"}
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set2.difference(set1)  # {'google', 'microsoft'}
# print(set3)

# ==================SHORTHAND METHOD==================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set2 - set1
# print(set3)
# ==================SHORTHAND METHOD==================

# ==============================================.DIFFERENCE() AND .DIFFERENCE_UPDATE()==============================================


# ==============================================.SYMMETRIC_DIFFERENCE() AND .SYMMETRIC_DIFFERENCE_UPDATE()==============================================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)


# countries = {"Nigeria", "Canada", "USA", "Malta", "Dominican Republic"}
# more_countries = {"Japan", "France", "Peru", "Australia", "Malta", "Finland"}
# even_more_countries = {"Ghana", "Scotland", "Malta", "Iceland", "Morocco", "Qatar"}
# # {"Nigeria", "Canada", "USA", "Dominican Republic", "Japan", "France", "Peru", "Australia", "Finland"}
# # {"Ghana", "Scotland", "Malta", "Iceland", "Morocco", "Qatar"}
# symm_diff = countries.symmetric_difference(more_countries).symmetric_difference(even_more_countries)
# print(symm_diff)

# ==============SHORTHAND=========================
# symm_diff = countries ^ more_countries ^ even_more_countries
# print(symm_diff)
# ==============SHORTHAND=========================

# ==============================================.SYMMETRIC_DIFFERENCE() AND .SYMMETRIC_DIFFERENCE_UPDATE()==============================================


# ==============================================REMOVING FROM A SET==============================================
# countries = {"Nigeria", "Canada", "USA", "Malta", "Dominican Republic"}
# countries.remove("Nigeria")
# countries.discard("Nigeria")
# print(countries)

# countries = {"Nigeria", "Canada", "USA", "Malta", "Dominican Republic"}
# countries.remove("Peru")
# countries.discard("Peru")
# print(countries)

# # countries.clear()
# print(countries)

# countries = {"Nigeria", "Canada", "USA", "Malta", "Dominican Republic"}
# popped_country = countries.pop()
# print(countries)
# print(popped_country)
# ==============================================REMOVING FROM A SET==============================================


# ==============================================.ISDISJOINT()==============================================

# numbers = {9, 4, 8, 1, 6, 34}
# other_numbers = {10, 4, 7, 1, 6}
# print(numbers.isdisjoint(other_numbers))

# numbers = {9, 4, 8, 1, 6, 34}
# other_numbers = {10, 7}
# print(numbers.isdisjoint(other_numbers))


# all_numbers = {2, 5, 8, 10, 45}
# some_numbers = {5, 10}
# # print(some_numbers.issubset(all_numbers))
# # print(all_numbers.issubset(some_numbers))
# print(all_numbers.issubset(all_numbers))



# ==============================================.ISDISJOINT()==============================================


# ==============================================EXERCISES==============================================
# 🛒 1. Grocery Store – Find Common Items in Carts
# Exercise:
# You have two shopping carts. Each contains a list of items. Use sets to find:

cart1 = ["milk", "bread", "eggs", "butter"]
cart2 = ["eggs", "butter", "cheese", "yogurt"]

cart1 = set(cart1)
cart2 = set(cart2)

# Items both people are buying # eggs, butter
# both_are_buying = cart1.intersection(cart2)
# print(both_are_buying)

# cart1.intersection_update(cart2)
# print(cart1)

# Items only one of them is buying   # milk, bread, cheese, yoghurt
# symm_diff = cart1.symmetric_difference(cart2)
# print(symm_diff)

# All items either of them is buying # milk, bread, eggs, butter, cheese, yoghurt
# all_items = cart1.union(cart2)
# print(all_items)


# 🎟️ 2. Movie Club – Count Unique Movies Watched
# Exercise:
# Three friends watched movies over the weekend. Each of them lists the movies they saw. Use sets to find out:

# How many unique movies were watched in total.

# alice = {"Inception", "Titanic", "Joker"}
# bob = {"Joker", "Interstellar", "Inception"}
# carol = {"Avatar", "Titanic", "Joker"}
# Answer: "Inception", "Titanic", "Joker", "Interstellar", "Avatar"

# print(len(alice.union(bob).union(carol)))



# unique = alice|bob|carol
# print(unique)
# print(len(unique))

# 🧑‍🤝‍🧑 3. Party Invite List – Avoid Duplicates
# Exercise:
# You’re creating a guest list. Some names were added twice by mistake. Use a set to fix this.

# guest_list = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"]

# print(list(set(guest_list)))

# guest_list = set(guest_list)
# print(guest_list)

# 🏫 4. Students in Clubs – Who’s in Both?
# Exercise:
# In a school, some students are in the science club, and some are in the music club. Find students who are in both.

# science_club = {"John", "Mia", "Liam", "Olivia"}
# music_club = {"Emma", "Liam", "Noah", "Olivia"}

# students_in_both = science_club & music_club
# print(students_in_both)

# students_in_both = science_club & music_club
# print(students_in_both)
# ==============================================EXERCISES==============================================
