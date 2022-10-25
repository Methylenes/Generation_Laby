from PIL import Image, ImageDraw


def rectangle(output_path, lab, endingPath, printPath):
    imageSize = len(lab) * 2
    rectSize = int(len(lab) / 2)

    image = Image.new("RGB", (imageSize, imageSize), "#F5F5DC")
    draw = ImageDraw.Draw(image)

    for i in range(len(lab)):
        for j in range(len(lab)):
            if i == j == 0:
                draw.rectangle([(0, 0), (rectSize, rectSize)], fill="black")
            elif lab[i][j] == '#':
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="black")
            elif (i, j) in endingPath and (i, j):
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="blue")
            elif (i, j) in printPath and (i, j) not in endingPath:
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="purple")
            else:
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="white")

    image.save(output_path)
    image.show()

####################################

