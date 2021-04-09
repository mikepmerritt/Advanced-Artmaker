from PIL import Image, ImageOps

# "image0.jpg" is the name of the file we want to use
img = Image.open("image0.jpg", 'r')

def main():
    newimg = ImageOps.expand(img, 1000, 0)
    newimg.save("border.png", "PNG")
    print("border added")
    for i in range(0,180):
        newimg = newimg.rotate(i)
        newimg = newimg.rotate(-i)
        print(i+1)
    # default is 1000 for lossless image blurring
    # crop more to get rid of black artifacts
    newimg = ImageOps.crop(newimg, 1010)
    newimg.save("blurred.png", "PNG")
    print("image blurred")


main()