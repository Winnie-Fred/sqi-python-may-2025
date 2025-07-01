question_bank: list[dict[str, str | dict[str, int]]] = [
    {
        "question": "What is Photosynthesis?", 
        "keywords": {"Photosynthesis":2, "Light energy":1, "Chemical energy":1, "Chloroplasts":2, "Chlorophyll":1, "Carbon dioxide":1, "Water":1, "Glucose":1, "Oxygen":1, "ATP":1}
    },
    {
        "question": "What is the concept of Supply and Demand?", 
        "keywords": {"Supply":2, "Demand":2, "Equilibrium price":1, "Shortage":1, "Surplus":1, "Market forces":1, "Price elasticity":1, "Consumers":1, "Producers":1}
    },
    {
        "question": "Explain Newton's Second Law of Motion.", 
        "keywords": {"Newton's Second Law":2, "Force":2, "Mass":1, "Acceleration":1, "F=ma":2, "Motion":1, "Inertia":1, "Dynamics":1, "Momentum":1}
    },
    {
        "question": "What is Object-Oriented Programming (OOP)?", 
        "keywords": {"Object-Oriented Programming":2, "Class":2, "Object":2, "Inheritance":1, "Encapsulation":1, "Polymorphism":1, "Abstraction":1, "Methods":1, "Attributes":1}
    },
    {
        "question": "Explain Plate Tectonics Theory.", 
        "keywords": {"Plate Tectonics":2, "Lithosphere":1, "Asthenosphere":1, "Convergent boundary":1, "Divergent boundary":1, "Transform boundary":1, "Earthquakes":1, "Volcanoes":1, "Continental drift":1, "Subduction":1}
    }
]


total_score = 0
total_weight = 0

for question in question_bank:
    _question = question["question"]
    keywords = question["keywords"].items()
    response = input(f"{_question}: ").strip().lower()
    for keyword, weight in keywords:
        if keyword.lower() in response:
            print(f"found keyword: {keyword.lower()}")
            total_score += weight
        total_weight += weight

print(f"Total Score: {total_score} out of {total_weight} points.")