import os, re
from PIL import ImageColor
from PIL import Image, ImageDraw, ImageFont

os.chdir("C:\\Python\\Udemy\\Assignment\\Invitation Images")

Read = open("List.txt")
List = Read.readlines()

names = []

for name in List:
    names.append(re.sub("\n","",name))

flower = Image.open("flower1.jpg")
flower_resize = flower.resize((240,240))


Background = flower_resize.copy()


for name in names:
    im = Image.new('RGBA', (288, 360), 'pink')
    im.paste(Background,(25,60))
    
    body = "Dear %s,\nPlease join us at the Wedding"%name
    draw = ImageDraw.Draw(im)
    draw.text((65, 150), body , fill='purple')

    im.save('%s.png'%name)

print("Invitations with Images Ready!!")
    
    
    
    
