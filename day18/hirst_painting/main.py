import colorgram

colors = colorgram.extract('./image.jpg', 30)
r = []
g = []
b = []
for i in range(0, len(colors)):
    r.append((colors[i].rgb.r))
    g.append((colors[i].rgb.g))
    b.append((colors[i].rgb.b))

first_color = (r[0], g[0],b[0])
second_color = (r[1], g[1],b[1])
third_color = (r[2], g[2],b[2])
fourth_color = (r[3], g[3],b[3])
fifth_color = (r[4], g[4],b[4])
sixth_color = (r[5], g[5],b[5])
print(f"{first_color}, {second_color}, {third_color}, {fourth_color}, {fifth_color}, {sixth_color}")
#first_color = colors[0]
#rgb = first_color.rgb # e.g. (255, 151, 210)
#hsl = first_color.hsl # e.g. (230, 255, 203)
#proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
#red = rgb[0]
#red = rgb.r
#saturation = hsl[1]
#saturation = hsl.s
