from AI import AI
from PIL import Image

im = Image.open("img.jpg")
im = list(im.getdata())
a = AI(im)
category, error = a.classify()
print(category)

with open("weekly.txt", "a") as f:
    f.write(category)
    f.write("\n")

def move_weekly():
    with open("archive.txt", "a") as archive:
        with open("weekly.txt", "r") as weekly:
            for line in weekly:
                archive.write(line)
    with open("weekly.txt", "w"):
        pass

move_weekly()