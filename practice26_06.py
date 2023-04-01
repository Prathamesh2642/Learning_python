i=0

with open("log.txt") as file:
    while True:
        content=file.readline().lower()
        i=i+1
        if 'python' in content:
            print("Yes python is present at line",i)
