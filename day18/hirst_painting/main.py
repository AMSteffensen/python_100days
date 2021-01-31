from turtle import Turtle, Screen
import random
color_list = [(125, 36, 24), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190), (37, 73, 84), (45, 74, 63), (48, 66, 80)]

TURTLE_SIZE = 50

t = Turtle(shape="turtle", visible=False)
s = Screen()
s.colormode(255)
t.pensize(20)
t.penup()
t.goto(TURTLE_SIZE/2 - s.window_width()/2, s.window_height()/2 - TURTLE_SIZE/2)
t.pendown()

def random_color():
    random_number = random.randint(0, len(color_list))
    random_color = color_list[random_number -1]
    return random_color

def draw(space, x):
    for i in range(x):
        for j in range(x):
            t.color(random_color())
            t.dot()  
            #distance for another dot
            t.forward(space)
        t.backward(space*x)

        t.right(90)
        t.forward(space)
        t.left(90)
t.penup()
draw(100,10)
screen = Screen()
screen.exitonclick()












#mport colorgram

#colors = colorgram.extract('./image.jpg', 30)

#rgb_colors = []
#for color in colors:
 #   r = color.rgb.r
 #   g = color.rgb.g
 #   b = color.rgb.b
 #   new_color = (r, g, b)
 #   rgb_colors.append(new_color)
#print(rgb_colors)



#10 by 10 pattern, 100 dots



#r = []
#g = []
#b = []
#for i in range(0, len(colors)):
#    r.append((colors[i].rgb.r))
#    g.append((colors[i].rgb.g))
#    b.append((colors[i].rgb.b))

#first_color = (r[0], g[0],b[0])
#second_color = (r[1], g[1],b[1])
#third_color = (r[2], g[2],b[2])
#fourth_color = (r[3], g[3],b[3])
#fifth_color = (r[4], g[4],b[4])
#sixth_color = (r[5], g[5],b[5])
#print(f"{first_color}, {second_color}, {third_color}, {fourth_color}, {fifth_color}, {sixth_color}")
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
