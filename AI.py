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
        flat = [0, 0, 0]
        count = len(self.img)*len(self.img[0])
        for pixel in self.img:
            for i in range(3):
                flat[i] += pixel[i]
        flat = [flat[i]/count for i in range(3)]
        # print(flat)
        # print(hex(int(flat[0]))[2:]+hex(int(flat[1]))[2:]+hex(int(flat[2]))[2:])

        # Use the pixel as an input for the AI

        # old values
        # colors = ["#342a1d", "#3d4138", "#1d140e", "#413725", "#46403d", "201a17", "221417", "311719", "242511", "383426", "1e2824", "3d342b", "3f372e"]
        # categories = ["fruit", "vegetable", "meat", "bread", "meat", "meat", "fruit", "fruit", "vegetable", "vegetable", "vegetable", "bread", "bread"]
        # errors = []
        # for k in colors:
        #     rgb = hex_to_list(k)
        #     total = 0
        #     for i in range(3):
        #         total += (flat[i]-rgb[i])**2
        #     errors.append(total)
        #     print(categories[colors.index(k)], errors[-1])
        # minimum = min(errors)
        # index = errors.index(minimum)
        # original = 0
        # for i in hex_to_list(colors[index]):
        #     original += i**2
        # return categories[index], 1 - minimum**.5/original**.5

        food_colors = {'meat': ['393128', '2b1b15', '302923', '301c14', '2015d', '2c211b', '453f3c', '201a17', '201710', '35302d'], 'vegetables': ['211d13', '34361b', '222419', '262512', '312e23', '3d4138', '242511', '383426', '1e2824', '2a20f'], 'fruit': ['342a1d', '221417', '311719', '4223d', '382b1c', '292219', '271d14', '2a251c', '382519', '322318'], 'bread': ['3d362b', '443428', '251e15', '413725', '3d342b', '3f372e', '3a2b1f', '332d29', '332a1b', '2a201c']}
        food_errors = {'meat':[], 'vegetables':[], 'fruit':[], 'bread':[]}
        food_avgs = {'meat':0, 'vegetables':0, 'fruit':0, 'bread':0}
        minimum_category = 'meat'
        minimum_error = (None, 2**31)
        for k, v in food_colors.items():
            for hex in v:
                rgb = hex_to_list(hex)
                error = 0
                for i in range(3):
                    error += (flat[i]-rgb[i])**2
                minimum_error = (k, error) if error < minimum_error[1] else minimum_error
                food_errors[k].append(error)
            food_avgs[k] = sum(food_errors[k])/len(food_errors[k])
            if food_avgs[k] < food_avgs[minimum_category]:
                minimum_category = k
        print(food_errors)
        print(food_avgs)
        return minimum_category, food_avgs[minimum_category]
        # return minimum_error