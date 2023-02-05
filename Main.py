from AI import AI
from PIL import Image

im = Image.open("Test_Images/img.jpg")
im = list(im.getdata())
a = AI(im)
category, diff = a.classify()
print(category, diff*100)
