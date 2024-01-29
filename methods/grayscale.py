import cv2
import os

def grayscale(self,imagepath):
    
    image = cv2.imread(os.path.join(imagepath))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    path=''
    cv2.imwrite(os.path.join(path,'gray_image.png'),gray_image)

    cv2.imshow('gray_image',gray_image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
