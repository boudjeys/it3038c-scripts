from PIL import Image, ImageFilter


#import and save jpg as a png
image1 = Image.open(r'C:\it3038c-scripts\python\Lab7Images\bear.jpg', "r")
image1.save(r"C:\it3038c-scripts\python\Lab7Images\bear.png")

#import an image and rotate it 90 degrees, then save
image2 = Image.open(r'C:\it3038c-scripts\python\Lab7Images\fish.jpg', "r")
image2.rotate(90).save(r"C:\it3038c-scripts\python\Lab7Images\fishrotated.jpg")

#import an image and apply a gaussian blur, then save
image3 = Image.open(r'C:\it3038c-scripts\python\Lab7Images\squirrel.jpg', "r")
image3.filter(ImageFilter.GaussianBlur(15)).save(r'C:\it3038c-scripts\python\Lab7Images\squirrelblurred.jpg')