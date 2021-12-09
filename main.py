from PIL import Image, ImageDraw
import math

def grad_to_rad(grad):
    return grad/360*math.pi*2

n = 2
degree = 10*(n+1)

file = open('DS2.txt')
image = Image.new("RGBA", (960,960), (0,0,0,0))
draw = ImageDraw.Draw(image)
for row in file:
    temp = row.split(" ")
    #Проти часової стрілки
    x = round(math.cos(grad_to_rad(degree + (360-2*degree))) * (int(temp[0]) - 480) - math.sin(grad_to_rad(degree + (360-2*degree))) * (int(temp[1]) - 480) + 480)
    y = round(math.sin(grad_to_rad(degree + (360-2*degree))) * (int(temp[0]) - 480) + math.cos(grad_to_rad(degree + (360-2*degree))) * (int(temp[1]) - 480) + 480)
    draw.point((x, y), "blue")
    #По часовій стрілці
    '''
    x1 = round(math.cos(grad_to_rad(degree)) * (int(temp[0]) - 480) - math.sin(grad_to_rad(degree)) * (int(temp[1]) - 480) + 480)
    y1 = round(math.sin(grad_to_rad(degree)) * (int(temp[0]) - 480) + math.cos(grad_to_rad(degree)) * (int(temp[1]) - 480) + 480)
    draw.point((x1,y1),"red")
    '''
    #Початковий датасет
    '''
    draw.point((int(temp[0]),int(temp[1])),"black")
    '''
del draw
image.save("result.png", "PNG")
file.close()