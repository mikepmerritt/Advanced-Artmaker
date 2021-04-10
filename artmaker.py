from PIL import Image, ImageOps

# loads in the file the user types into the console
# TODO: handle error for nonexistent file
def openImage():
    filename = input("Enter the name of the image file you would like to use (example: image.png): ")
    return Image.open(filename, 'r')

# adds a border around the image before blurring, making the resulting blurred image a square
# if this is not called, the resulting image will be circular
def addBorder(img):
    border_img = ImageOps.expand(img, 1000, 0)
    border_img.save("border.png")
    print("border added")
    return border_img

# blurs the image
def blur(img):
    for i in range(0,180):
        img = img.rotate(i)
        img = img.rotate(-i)
        print(i+1)
    return img

# crops off the edges of the image
# pixels_cropped values to use: 
# - 1000 to get rid of border, has fuzzy edges
# - 1010 to get rid of border and fuzzy edges
# - 0 if no border was used
def cropEdges(img, pixels_cropped):
    img = ImageOps.crop(img, pixels_cropped)
    img.save("blurred.png")
    print("image blurred")

# main method
def main():
    original_img = openImage()
    border_img = addBorder(original_img)
    blurred_img = blur(border_img)
    cropEdges(blurred_img, 1010)


main()