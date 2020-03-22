import cv2
import numpy as np
from matplotlib import pyplot as plt

#Difference-of-Gaussian visualisation
def DoG(fn):
    fn_no_ext = fn.split('.')[0]
    outputFile = fn_no_ext + '_DoG.jpg'
    #read the input file
    img = cv2.imread(str(fn))

    #run a 5x5 gaussian blur then a 3x3 gaussian blr
    blur5 = cv2.GaussianBlur(img,(5,5),0)
    blur3 = cv2.GaussianBlur(img,(3,3),0)

    DoGim = blur5 - blur3
    cv2.imwrite(outputFile, DoGim)

#SIFT and Feature Matching visualisation
def siftMatch(image1, image2):
    img1 = cv2.imread(image1)
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(image2)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    img1 = cv2.drawKeypoints(gray1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(image1.split('.')[0] + '_sift_keypoints.jpg',img1)
    
    img2 = cv2.drawKeypoints(gray2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(image2.split('.')[0] + '_sift_keypoints.jpg',img2)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k = 2)
    good = []
    for m, n in matches:
        if m.distance < 0.75*n.distance:
            good.append(m)

    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches[:10], None, flags = 2)
    
    cv2.imwrite(image1.split('.')[0] + '_' + image2[78:86] + '_matches.jpg', img3)
    #plt.imshow(img3),plt.show()

#BEGIN:
for i in range(2, 10):
    img1 = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(390 + i) + '.jpg'
    img2 = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(391 + i) + '.jpg'
    siftMatch(img1, img2)
for i in range(2,11):
    img = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(390 + i) + '.jpg'
    DoG(img)

#siftMatch('C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5392.jpg', 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5393.jpg')


