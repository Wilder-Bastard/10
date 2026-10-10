from PIL import Image
img = Image.open("C:/adamovahuinya/1. study/proga/Default/otkr.jpg")
print(img.size)
chopped = img.crop((100,100,img.width,img.height))
chopped.save("chopped.jpg")