import cv2
import numpy as np

#Difference-of-Gaussian visualisation
def DoG(fn):
    fn_no_ext = fn.split('.')[0]
    outputFile = fn_no_ext + '_DoG.jpg'
    #read the input file
    img = cv2.imread(str(fn))

    #run a 5x5 gaussian blur then a 3x3 gaussian blr
    blur5 = cv2.GaussianBlur(img,(5,5),0)
    blur3 = cv2.GaussianBlur(img,(3,3),0)

    #write the results of the previous step to new files
    cv2.imwrite(fn_no_ext + '_3x3.jpg', blur3)
    cv2.imwrite(fn_no_ext + '_5x5.jpg', blur5)

    DoGim = blur5 - blur3
    cv2.imwrite(outputFile, DoGim)

#SIFT visualisation
def siftVisual(inImg):
    img = cv2.imread(inImg)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(gray,None)

    img=cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(inImg + '_sift_keypoints.jpg',img)

#Feature matching visualisation
def featureMatch ():
    pass

#BEGIN:
#path = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/'
DoG('C:/Users/Jill Ueng/Pictures/Saved Pictures/cats.jpg')


