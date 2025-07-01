def say_hi(time_of_day, name):
    return f"Hi 👋. Good {time_of_day}, {name}."


def add_nums(a, b):
    return a + b



def main():
    print(say_hi("afternoon", "Awwal"))
    print(add_nums(4, 8))

if __name__ == "__main__":
    print("This code is running from module1.py")
    main()
