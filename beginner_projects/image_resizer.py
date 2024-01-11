from PIL import Image

def resize_image(size1, size2):
    image = Image.open('test.jpg')
    print(f"Current size :  {image.size}")
    resized_image = image.resize((size1, size2))
    resized_image.save(f"resizedimage{size1}.jpeg")

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Height: "))
resize_image(size1, size2)