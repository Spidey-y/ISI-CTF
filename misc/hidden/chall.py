from PIL import Image

image = Image.open("frame.png")
if image.mode != "RGB":
    image = image.convert("RGB")
width, height = image.size
pixels = image.load()
res = []
for y in range(height):
    res.append([])
    for x in range(width):
        r, g, b = pixels[x, y]
        if r == g == b == 255 or r == g == b == 234:
            res[-1].append("E")
        else:
            res[-1].append("T")
f = open("file.txt", "w")
for i in res:
    f.write("".join(i) + "BREAK")
