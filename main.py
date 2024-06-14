import cv2
from simple_facerec import SimpleFacerec




#Dosyalardan yüz encode
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Kameradan yüz tespiti için bu kısmı aktif edin
#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#Videodan yüz tespiti için bu kısmı aktif edin
cap = cv2.VideoCapture("video1.mp4")


while True:
    ret, frame = cap.read()

    #Yüz tespiti
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        if "," in name:
            # İsim metnini virgülle böl
            name_parts = name.split(',')
            isim = name_parts[0]
            isim = isim.split(' ')

            #Aranması var ise çerçeveyi kırmızı yap
            color = (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (color), 4)

            cv2.rectangle(frame, (15, y1-20), (350 , y1+80), (0, 0, 0), cv2.FILLED)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (color), cv2.FILLED)
            cv2.putText(frame, "Aranan", (x1 + 6, y2 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, "Adi Soyadi: " + name_parts[0], (20, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1)
            cv2.putText(frame, "Orgut: " + name_parts[1], (20, y1+35), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1)
            cv2.putText(frame, "Aranma Kodu: ", (20, y1+70), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1)
            cv2.putText(frame,  name_parts[2], (190, y1+70), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 1)

            # Tespit edilen kişinin resmini göster
            img_path = "images/" + name + ".jpeg"
            img = cv2.imread(img_path)
            if img is not None:
                # Resmi kare boyutuna getir
                img = cv2.resize(img, (70, 100))

                # Resmi kameradan gelen görüntüye7 yerleştir
                frame[y1+105:y1+105+img.shape[0], 20:20+img.shape[1]] = img

        else:
            # Çerçeve ve rengi
            color = (0, 200, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (color), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()