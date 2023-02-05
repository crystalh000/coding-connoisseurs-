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
        print(hex(int(sum[0]))[2:]+hex(int(sum[1]))[2:]+hex(int(sum[2]))[2:])
        # Use the pixel as an input for the AI
        colors = ["#342a1d", "#3d4138", "#1d140e", "#413725", "#46403d", "201a17", "221417", "311719", "242511", "383426", "1e2824", "3d342b", "3f372e"]
        categories = ["fruit", "vegetable", "meat", "bread", "meat", "meat", "fruit", "fruit", "vegetable", "vegetable", "vegetable", "bread", "bread"]
        errors = []
        for k in colors:
            rgb = hex_to_list(k)
            total = 0
            for i in range(3):
                total += (sum[i]-rgb[i])**2
            errors.append(total)
            print(categories[colors.index(k)], errors[-1])
        minimum = min(errors)
        index = errors.index(minimum)
        original = 0
        for i in hex_to_list(colors[index]):
            original += i**2
        return categories[index], 1 - minimum**.5/original**.5