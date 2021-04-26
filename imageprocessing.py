from PIL import Image, ImageOps
import  numpy as np
from knnmodel import MLmodel

class Imageprocessing:
    def cleanImage():
        img = Image.open('data_images/image.png')                   # read image
        image = img.crop((10, 60, 500, 450))                        # croping image
        # image.show()
        inv_image = ImageOps.invert(image)                        # inverting the image
        # inv_image.show()
        inv_image = inv_image.resize((8,8), Image.ANTIALIAS)      # resizing the image into 8x8x3 pixels
        data = inv_image.getdata()                                # converting the image into numpy array
        array = np.array(data)
        temp = []
        for elem in array:
            temp.append(((elem[0]+elem[1]+elem[2])/3))            # converting the 2-D array into 1-D array
        ML_data = np.array(temp)
        ML_data = ML_data.reshape(1,-1)                           # Final array
        return ML_data
