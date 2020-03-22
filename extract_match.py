import cv2
from PIL import Image

# Difference-of-Gaussian visualisation
def DoG(fn):
    fn_no_ext = fn.split('.')[0]
    outputFile = fn_no_ext + '_DoG.jpg'
    # read the input file
    img = cv2.imread(str(fn))

    # run a 5x5 gaussian blur then a 3x3 gaussian blr
    blur5 = cv2.GaussianBlur(img, (5, 5), 0)
    blur3 = cv2.GaussianBlur(img, (3, 3), 0)

    DoGim = blur5 - blur3
    cv2.imwrite(outputFile, DoGim)


# SIFT and Feature Matching visualisation
def siftMatch(image1, image2):
    img1 = cv2.imread(image1)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(image2)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    img1 = cv2.drawKeypoints(gray1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(image1.split('.')[0] + '_sift_keypoints.jpg', img1)

    img2 = cv2.drawKeypoints(gray2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(image2.split('.')[0] + '_sift_keypoints.jpg', img2)

    # FLANN_INDEX_KDTREE = 0
    # index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
    # search_params = dict(checks=100)
    #
    # flann = cv2.FlannBasedMatcher(index_params, search_params)
    #
    # matches = flann.knnMatch(descriptors1, descriptors2, k=2)
    #
    # good_matches = []
    # for m, n in matches:
    #     if m.distance < 0.7 * n.distance:
    #         good_matches.append(m)
    #
    # #print(*matches[:6])
    # img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    # #plt.imshow(img3), plt.show()
    # cv2.imwrite(image1.split('.')[0] + '_' + image2[78:86] + '_matches.jpg', img3)

# BEGIN:
# for i in range(2, 10):
#     img1 = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(390 + i) + '.jpg'
#     img2 = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(391 + i) + '.jpg'
#     siftMatch(img1, img2)
# for i in range(2, 11):
#     img = 'C:/Users/Jill Ueng/Documents/MEng Final Year Project/OpenCV SIFT/demo/demoimg/IMG_5' + str(390 + i) + '.jpg'
#     DoG(img)


path = "C:\\Users\\Jill Ueng\\Pictures\\temp"

img1 = path + '\\20190411_162929.jpg'
img2 = path + '\\20190411_162933.jpg'
size = 500, 666

item1 = Image.open(img1)
item2 = Image.open(img2)
item1.load()
item2.load()
item1.thumbnail(size, Image.ANTIALIAS)
item2.thumbnail(size, Image.ANTIALIAS)

item1 = item1.rotate(90, expand=True)
item2 = item2.rotate(90, expand=True)

item1.save(path + '\\_1.jpg', "JPEG", quality=100)
item2.save(path + '\\_2.jpg', "JPEG", quality=100)

siftMatch(path + '\\_1.jpg', path + '\\_2.jpg')

