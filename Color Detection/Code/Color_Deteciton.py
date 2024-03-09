import cv2
import numpy as np

def find_color(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Görüntüyü HSV renk uzayına dönüştür
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Renk sınırlarını belirle
    # Kırmızı renk
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Yeşil renk
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Sarı renk
    lower_yellow = np.array([20, 50, 50])
    upper_yellow = np.array([40, 255, 255])

    # Belirlenen renk aralıklarına uyan pikselleri tespit et
    mask_red = cv2.inRange(hsv_image, lower_red1, upper_red1) + cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Eğer belirli bir renk varsa, renk adını döndür; yoksa None döndür
    if np.any(mask_red > 0):
        color_name = "Kırmızı"
    elif np.any(mask_green > 0):
        color_name = "Yeşil"
    elif np.any(mask_yellow > 0):
        color_name = "Sarı"
    else:
        color_name = "Belirli bir renk bulunamadı"

    # Resmi ekrana yazdır
    cv2.imshow('Girilen Resim', image)

    # Renk adını ve resmi altına ekleyerek yeni bir pencere içinde yazdır
    cv2.namedWindow("Renk Tespiti", cv2.WINDOW_NORMAL)
    cv2.putText(image, "Renk: " + color_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Renk Tespiti", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Kullanıcıdan bir resim yolu al
image_path = input("Lütfen bir resim yolunu girin: ")

# find_color fonksiyonunu çağır
find_color(image_path)
