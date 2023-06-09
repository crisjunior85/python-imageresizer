#image resizer
#install a library called Pillow
#import Pillow
#open up the image we want to resize
#print the current size of the image
#specify the size we wanna change it to
#save the new resized image
#then change the program to which we ask a user 

from PIL import Image

def resize_image(size1, size2):
    image = Image.open("Beany.jpg")
    print(f"Current size: {image.size}")
    
    resized_image = image.resize((size1, size2))
    
    resized_image.save("crisbeany" + str(size1) + ".jpg")

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image(size1, size2)
