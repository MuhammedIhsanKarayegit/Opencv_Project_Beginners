import cv2 as cv
import easyocr as eocr
import matplotlib.pyplot as plt

# Aşağıda resimlerdeki yazıları tespit etmesi için gerekli fonksiyon yazıldı.
def text_detection(img_path):
    img = cv.imread(img_path) # Resim okuma
    reader = eocr.Reader(['en'], gpu=False) # easyocr kütüphanesi ile ocr nesnesi oluşturuldu. Şimdilik sadece ingilizce algılanıyor. Gpu kullanımı kapatıldı.
    text_ = reader.readtext(img) # Resimlerdeki yazıların tespit edilmesi bu kısımda gerçekleştiriliyor.
    
    # text_ içindeki her bir yazı t değişkeni içine alınıp bu yazı için bir dikdörtgen oluşturuluyor ve bu dikdörtgenin üzerine resimdeki yazı yazdırılıyor.
    for t in text_:
        print(t)
        bbox, text, score = t
        cv.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv.putText(img, text, bbox[0], cv.FONT_HERSHEY_COMPLEX, 0.65, (0,0,0), 1)

    # Resmideki yazılar algılanmış bir şekilde ekrana çıktı verir.
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGBA))
    plt.show()

img_path = input('Resim yolunu giriniz.')
text_detection(img_path)