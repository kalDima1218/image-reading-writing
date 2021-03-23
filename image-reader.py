from PIL import Image
image = Image.open('PXL.jpg')
width = image.size[0]
height = image.size[1]
pix = image.load()
f = open('token.txt', 'w')
f.write(str(width) + " " + str(height) + "\n")
for x in range(width):
    for y in range(height):
       f.write(str(pix[x, y][0]) + " " + str(pix[x, y][1]) + " " + str(pix[x, y][2]) + "\n")
f.close()