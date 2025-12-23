import cv2
import numpy as np

cao = cv2.VideoCapture(r"C:\Users\soban\Downloads\Tom_and_jerry_funny_video_😂😂_ll_when_your_friend_running_in_school__#memes_#tom_#funny_#funnyvideo(480p).mp4")

r, f = cao.read()
x, y ,w, h = [3, 328, 232, 300]

t = (x, y, w, h)
roi = f[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
tr = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    r, f = cao.read()
    if r == True:
        hsv_f = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
        d = cv2.calcBackProject([hsv_f], [0], roi_hist, [0, 180], 1)
        r, tp = cv2.CamShift(d, t, tr)
        x, y, w, h = tp
        final = cv2.rectangle(f, (x,y), (x+w, y+h), (0,0,255), 4)

        cv2.imshow('TRACKING', final)

        if cv2.waitKey(20) & 0xFF == ord('p'):
            break
    else:
        break

cao.release()
cv2.destroyAllWindows()
