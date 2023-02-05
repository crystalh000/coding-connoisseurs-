from AI import AI
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open("img2.jpg")
im = list(im.getdata())
a = AI(im)
category, error = a.classify()
print(category, error)

with open("weekly.txt", "a") as f:
    f.write(category)
    f.write("\n")

def analyze_week():
    with open("weekly.txt", "r") as f:
        indexes = {'meat':0, 'vegetable':1, 'bread':2, 'fruit':3}
        counts = [0 for _ in range(len(indexes))]
        for line in f:
            counts[indexes[line[:-1]]] += 1
        plt.pie(counts, labels=list(indexes.keys()))
        plt.savefig("pie_chart.png")
analyze_week()

def move_weekly():
    with open("archive.txt", "a") as archive:
        with open("weekly.txt", "r") as weekly:
            for line in weekly:
                archive.write(line)
    with open("weekly.txt", "w"):
        pass

# move_weekly()