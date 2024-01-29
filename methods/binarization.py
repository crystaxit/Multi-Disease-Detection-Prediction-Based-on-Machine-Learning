import cv2
import os
def binarization(self,imagepath):
    #im_gray = cv2.imread(imagepath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    im_gray = cv2.cvtColor(cv2.imread(imagepath), cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    path4=''
    cv2.imwrite(os.path.join(path4,'bw_image3.png'), im_bw)
   
    cv2.imshow('gray_image1',im_bw) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()