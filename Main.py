import os
from AI import AI
from PIL import Image

im = Image.open("carb.jpg")
im = list(im.getdata())
a = AI(im)
print(a.classify())