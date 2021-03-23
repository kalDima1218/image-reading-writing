from PIL import Image, ImageDraw
pix=[]
with open('token.txt', 'r') as f:
	wh = f.readline()[:-1].split(" ")
	w = int(wh[0])
	h = int(wh[1])
	for _ in range(w):
		pix.append([])
		for _ in range(h):
			ln=f.readline()[:-1].split(" ")
			pix[-1].append([int(ln[0]), int(ln[1]), int(ln[2])])
img = Image.new("RGB", (w, h))
draw = ImageDraw.Draw(img)
for i in range(w):
	for l in range(h):
		draw.point((i, l), (pix[i][l][0], pix[i][l][1], pix[i][l][2]))
img.save("token.jpg")