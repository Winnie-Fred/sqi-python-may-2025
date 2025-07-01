def read_data(file_path: str):
    with open(file_path, "r") as f:
        lines = f.readlines()
        processed_data = []
        for line in lines:
            name, age = line.split(",")
            age = int(age)
            processed_data.append((name, age))
        return processed_data