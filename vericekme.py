#Data.json dosyasından veri çekmek için bu kodu çalıştırabilirsiniz.

import os
import json
import urllib3
import requests


def download_and_save_image(data):
    adi = data["Adi"]
    soyadi = data["Soyadi"]
    t_orgut_adi = data["TOrgutAdi"]
    t_kategori_adi = data["TKategoriAdi"]
    ilk_gorsel_url = "https://www.terorarananlar.pol.tr" + data["IlkGorselURL"]
    urllib3.disable_warnings()
    #Bütün kategorileri çekmek için bu kısımı aktif edin
    #response = requests.get(ilk_gorsel_url, verify=False)

    #Kategorisine göre filtrelemek için bu kısımı aktif edin
    if t_kategori_adi == "kırmızı":
        response = requests.get(ilk_gorsel_url, verify=False)

    # İlk görselin adını oluştur
    dosya_adi = f"{adi} {soyadi}, {t_orgut_adi}, {t_kategori_adi}.jpeg"

    #Terör örgütlerinden isimlerinde bulunan '/' sembolünü hata vermemesi için '_' ile değiştir
    dosya_adi = dosya_adi.replace("/", "_")



    # İndirme başarılıysa
    if response.status_code == 200:
        # Görseli kaydet
        with open(dosya_adi, "wb") as f:
            f.write(response.content)
        print(f"{dosya_adi} başarıyla kaydedildi.")
    else:
        print("Görsel indirilemedi.")


# JSON dosyasını oku
with open("data.json", "r", encoding="utf-8") as f:
    veri = json.load(f)

# Her bir girdi için işlem yap
for item in veri:
    download_and_save_image(item)
