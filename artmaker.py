from PIL import Image, ImageOps

def openImage():
    filename = input("Enter the name of the image file you would like to use (example: image.png): ")
    return Image.open(filename, 'r')

def addBorder(img):
    border_img = ImageOps.expand(img, 1000, 0)
    border_img.save("border.png")
    print("border added")
    return border_img

def blur(img):
    for i in range(0,180):
        img = img.rotate(i)
        img = img.rotate(-i)
        print(i+1)
    return img

def cropEdges(img, pixels_cropped):
    img = ImageOps.crop(img, pixels_cropped)
    img.save("blurred.png")
    print("image blurred")

def main():
    original_img = openImage()
    border_img = addBorder(original_img)
    blurred_img = blur(border_img)
    cropEdges(blurred_img, 1010)

main()