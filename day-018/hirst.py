import colorgram

rgb_list = []
colour_list = []

def colour_extractor(image_location):
    hirst_colours = colorgram.extract(image_location, 15)

    for colour in hirst_colours:
        rgb_list.append(colour.rgb)

    for colour in rgb_list:
        r = colour.r
        g = colour.g
        b = colour.b
        colour_list.append((r, g, b))

    return colour_list