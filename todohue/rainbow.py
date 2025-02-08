import random

def rainbow(text):
    arr = []
    for i in text:
        arr.append(f"\x1b[1;4;{random.randint(31,37)}m{i}\x1b[0m")
    return "".join(arr)

