import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def tach_bien_anh(duong_dan_anh):
    anh = cv2.imread(duong_dan_anh)

    anh_gray = cv2.cvtColor(anh, cv2.COLOR_BGR2GRAY)

    anh_blur = cv2.GaussianBlur(anh_gray, (5, 5), 0)

    canny_edges = cv2.Canny(anh_blur, 50, 150)

    cv2_imshow(anh)
    print("Anh Goc")

    cv2_imshow(canny_edges)
    print("Bien Anh")

tach_bien_anh("/content/tải xuống.jpg")
