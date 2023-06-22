from PIL import Image

data = []
with open("input.txt", "r") as file:
    data = file.readlines()

width = 300
height = 300
image = Image.new("1", (width, height))
pixels = image.load()
for i in range(height):
    for j in range(width):
        if data[i][j] == "0":
            pixels[i, j] = 255
        else:
            pixels[i, j] = 0


image.save("output.png")
