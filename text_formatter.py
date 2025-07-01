# text = " HELLO world "
# text = "good day to you   "
text =  "Trimming spaces at the beginning"

text = text.strip()
text = text.capitalize()
text = text + "."
print(text)  # Good day to you.


text = "good day to you   "
text = text.strip().capitalize() + "."
print(text)  # Good day to you.