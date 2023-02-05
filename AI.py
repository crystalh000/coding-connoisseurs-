def hex_to_list(hex):
    if hex[0] == "#":
        hex = hex[1:]
    return [int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16)]

class AI:

    def __init__(self, image_array):
        "Initialize the input"
        self.img = image_array
    
    def classify(self):
        "Ask the AI to determine the classification from the input"

        # Flatten the image into 1 pixel
        sum = [0, 0, 0]
        count = len(self.img)*len(self.img[0])
        for pixel in self.img:
            for i in range(3):
                sum[i] += pixel[i]
        sum = [sum[i]/count for i in range(3)]
        print(sum)
        # Use the pixel as an input for the AI
        colors = ["#342a1d", "#3d4138", "#453f3c", "#413725"]
        categories = ["fruit", "vegetable", "meat", "bread"]
        errors = []
        for k in colors:
            rgb = hex_to_list(k)
            total = 0
            for i in range(3):
                total += (sum[i]-rgb[i])**2
            errors.append(total)
        return categories[errors.index(min(errors))]