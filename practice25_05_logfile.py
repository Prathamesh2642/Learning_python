with open("log.txt") as file:
    content=file.read().lower()
if 'python' in content:
    print("Yes, python is present")