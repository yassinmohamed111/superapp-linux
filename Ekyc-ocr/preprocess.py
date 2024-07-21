import cv2 
import numpy as np

    
def thresholding(image,black):
        img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(img_gray,black,255,cv2.THRESH_BINARY_INV)
        
        return thresh
  


def dilation(thresh_img,v1=1,v2=1):
            
        kernel = np.ones((v1,v2), np.uint8)
        #(1,2),iter=2
        dilated = cv2.dilate(thresh_img, kernel, iterations = 2)
        return dilated
    


def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def resize_image(image, width, height):
    # Assuming resize_image is a function that resizes the image
    return cv2.resize(image, (width, height))

def save_threshold(image1, image2, image3, image4, width=None, height=None, image2_width=200, image2_height=400):
    if width or height:
        image1 = resize_image(image1, width, height)
        image3 = resize_image(image3, width, height)
        image4 = resize_image(image4, width, height)
    
    if image2_width or image2_height:
        image2 = resize_image(image2, image2_width, image2_height)
    
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_name.jpg', image1)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_second_name.jpg', image2)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_locationn.jpg', image3)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_manf.jpg', image4)

def save_threshold2(image1, image2, image3, image4):
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_name.jpg', image1)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_second_name.jpg', image2)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_locationn.jpg', image3)
    cv2.imwrite('/home/yassinmohamed/superapp linux/Ekyc-ocr/processed_images/output_manf.jpg', image4)

# Example usage

