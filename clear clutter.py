import os


files = os.listdir("./DSA in Python/")

for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"")