# This is the solution for First technical round for the role of Computer Vision Engineer at Vectorly
# Solution developed by Ritwik Raha 
#
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# The image has first been converted into grayscale to improve thresolding
# Next is a simple binary thresholding where the levels are set by analysing the image entropy
# the final step is to run a dilation operation on the thresholded image and filtering the noises
#

#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    kernel = np.ones((3,3),np.uint8)
    img2gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(img2gray, 25, 255, cv2.THRESH_BINARY)
    output = cv2.dilate(thresh,kernel,iterations = 2)

    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################