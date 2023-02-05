from AI import AI
from PIL import Image

im = Image.open("Test_Images/vege.jpg")
im = list(im.getdata())
a = AI(im)
print(a.classify())
