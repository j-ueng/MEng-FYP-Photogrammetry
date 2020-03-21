import cv2
import os


def sift_detector(new_image, image_template):

    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template

    sift = cv2.xfeatures2d.SIFT_create()

    keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
    search_params = dict(checks=100)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    return len(good_matches), keypoints1


path = "C:\\Users\\Jill Ueng\\Documents\\MEng Final Year Project\\Feature Tracking\\Demo"
cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 360)
count = 0
init = 0
saved = 0.0
check = 0

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    top_left_x = int(width / 3)
    top_left_y = int((height / 2) + (height / 4))
    bottom_right_x = int((width / 3) * 2)
    bottom_right_y = int((height / 2) - (height / 4))
    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x,bottom_right_y), (170, 170, 255), 3)
    cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]
    cv2.imshow('Object Detector using SIFT', frame)

    if init == 0:  # re/INITIALISE
        if cv2.waitKey(1) == 9:  # KEY: ENTER
            img_path = path + "\\img%d.jpg" % count
            cv2.imwrite(img_path, cropped)
            image_template = cv2.imread(img_path)

            if os.path.isfile(img_path):
                print('Image %d captured.' % count)
                count = count + 1

            init = 1
            check = 0

        elif cv2.waitKey(1) == 27:  # KEY: ESC
            print('Exiting (1) ~~!!!')
            for file in os.listdir(path):
                os.unlink(os.path.join(path, file))
            break

    elif init == 1:
        features = sift_detector(cropped, image_template)
        matches = features[0]
        kp = features[1]

        cv2.putText(frame, "MATCHES: %d" % matches, (157, 325), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (170, 170, 255), 1)
        cv2.drawKeypoints(cv2.flip(cropped, 1), kp, frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x],
                          flags=cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)

        if check == 0:
            saved = float(matches)  # 100% of matched points
            check = 1

        if not saved == 0:
            cv2.putText(frame, "%.2f %%" % ((matches/saved)*100), (375, 325), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (170, 170, 255), 1)
            if 0.3*saved <= matches <= 0.5*saved:
                cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (170, 255, 170), 3)
                cv2.putText(frame, 'PRESS ENTER', (145, 60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (170, 255, 170), 1)

        cv2.imshow('Object Detector using SIFT', frame)
        if cv2.waitKey(1) == 9:
            init = 0
        elif cv2.waitKey(1) == 27:  # KEY: ESC
            # for file in os.listdir(path):
            #     os.unlink(os.path.join(path, file))
            print("Exiting (2) ~~!!!")
            break

cap.release()
cv2.destroyAllWindows()
