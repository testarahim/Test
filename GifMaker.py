from PIL import Image

im = Image.open("coffee.png")

def rotation(img, degree):
    newLoc = im.rotate(degree)
    return newLoc
images = list()
for i in range(0,360,30):
    images.append(rotation(im,i))

images[0].save("degisik.gif", save_all=True, append_images = images[1:], optimize = False, duration = 100, loop = 0)
