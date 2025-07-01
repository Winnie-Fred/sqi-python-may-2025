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
        "answer": "b",
        "score": 5,
    },
    {
        "question": question_two, 
        "answer": "b",
        "score": 6,
    },
    {
        "question": question_three, 
        "answer": "c",
        "score": 12,
    },
    {
        "question": question_four, 
        "answer": "c",
        "score": 4,
    },
    {
        "question": question_five, 
        "answer": "b",
        "score": 3,
    },
]

total_score = 0

for idx, question in enumerate(question_bank, start=1):
    while True:
        _question = question["question"]
        valid_answer = question["answer"]
        print(f"\n{idx}. {_question}\n")
        chosen_answer = input("Choose an option from a to d: ").strip().lower()

        if chosen_answer not in "abcd":
            print("You have to chose from a to d")
            continue
        break

    if chosen_answer == valid_answer:
        total_score += question['score']
    
print(f"At the end of the CBT exam, you scored {total_score} points")