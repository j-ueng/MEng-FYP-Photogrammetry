import cv2
import os


path = "C:\\Users\\Jill Ueng\\Documents\\MEng Final Year Project\\Validation3\\Photos2\\filtering\\"
savepath = "C:\\Users\\Jill Ueng\\Documents\\MEng Final Year Project\\Validation3\\Photos2\\filtered\\"
dirs = os.listdir(path)

for item in dirs:
    fullpath = os.path.join(path, item)
    if os.path.isfile(fullpath):
        img = cv2.imread(fullpath)

        for i in range(1, 10, 2):
            blurred = cv2.GaussianBlur(img, (i, i), 0)
            # folder = '\\GaussianBlur\\%dx%d\\' % (i, i)
            # if os.path.isdir(savepath + folder):
            #     cv2.imwrite(savepath + folder + item, blurred)
            # else:
            #     os.makedirs(savepath + folder)
            #     cv2.imwrite(savepath + folder + item, blurred)

            sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
            folder = '\\Sharpened\\%dx%d\\' % (i, i)
            if os.path.isdir(savepath + folder):
                cv2.imwrite(savepath + folder + item, sharpened)
            else:
                os.makedirs(savepath + folder)
                cv2.imwrite(savepath + folder + item, sharpened)

        for i in range(70, 100, 20):
            small = cv2.resize(img, (0, 0), fx=i*0.01, fy=i*0.01)
            folder = '\\Resolution\\%d percent\\' % i
            if os.path.isdir(savepath + folder):
                cv2.imwrite(savepath + folder + item, small)
            else:
                os.makedirs(savepath + folder)
                cv2.imwrite(savepath + folder + item, small)

        for i in range(5, 31, 5):
            folder = '\\Contrast\\limit%d\\' % i
            lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=i*0.1, tileGridSize=(8, 8))
            cl = clahe.apply(l)
            limg = cv2.merge((cl, a, b))
            final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
            if os.path.isdir(savepath + folder):
                cv2.imwrite(savepath + folder + item, final)
            else:
                os.makedirs(savepath + folder)
                cv2.imwrite(savepath + folder + item, final)
