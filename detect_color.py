import numpy as np
import cv2
user_input=input("Enter the name of image with path")

#reads the image
image = cv2.imread(user_input)
image1=cv2.imread('white.jpg')

#defining the list of boundries
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

#load the images in the given boundries
for (lower,upper) in boundaries:
    lower=np.array(lower,dtype='uint8')
    upper=np.array(upper,dtype='uint8')
    mask=cv2.inRange(image,lower,upper)
    output = cv2.bitwise_and(image, image1, mask = mask)
    #shows the processed image one by one
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
