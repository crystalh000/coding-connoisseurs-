import os
from PIL import Image

folder = "Test_Images"
sub_folders = ["meat", "vegetables", "fruit", "bread"]
food_colors = {i:[] for i in sub_folders}

for sub in sub_folders:
    for img in os.listdir(f"{folder}/{sub}"):
        im = Image.open(f"{folder}/{sub}/{img}")
        im = im.getdata()
        sum = [0, 0, 0]
        count = len(im)*len(im[0])
        for pixel in im:
            for i in range(3):
                sum[i] += pixel[i]
        sum = [sum[i]/count for i in range(3)]
        hex_color = hex(int(sum[0]))[2:]+hex(int(sum[1]))[2:]+hex(int(sum[2]))[2:]
        food_colors[sub].append(hex_color)

print(food_colors)