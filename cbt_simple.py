question_one = """What is 2 + 2?
a) 3
b) 4
c) 5
d) 6"""

question_two = """What color is the sky on a clear day?
a) Red
b) Blue
c) Green
d) Yellow"""


question_three = """How many legs does a spider have?
a) 6
b) 7
c) 8
d) 9"""

question_four = """What sound does a cow make?
a) Meow
b) Bark
c) Moo
d) Quack"""


question_five = """What is the opposite of 'hot'?
a) Warm
b) Cold
c) Cool
d) Boiling"""

question_bank: list[dict[str, str]] = [
    {
        "question": question_one, 
        "answer": "b"
    },
    {
        "question": question_two, 
        "answer": "b"
    },
    {
        "question": question_three, 
        "answer": "c"
    },
    {
        "question": question_four, 
        "answer": "c"
    },
    {
        "question": question_five, 
        "answer": "b"
    },
]

total_score = 0

for question in question_bank:
    _question = question["question"]
    valid_answer = question["answer"]
    print(_question)
    chosen_answer = input("Choose an option from a to d: ").strip().lower()

    if chosen_answer == valid_answer:
        total_score += 1
    
print(f"At the end of the CBT exam, you scored {total_score} points")