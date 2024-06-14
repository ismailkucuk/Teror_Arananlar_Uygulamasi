#Dosya isimlerinizi türkçe karakterlere uygun hale getirmek için bu kodu çalıştırabilirsiniz
import os

def replace_turkish_characters(directory):
    # Türkçe karakterlerin yerine geçecek İngilizce karakterlerin sözlüğü
    turkish_to_english = {
        'ı': 'i',
        'ğ': 'g',
        'ü': 'u',
        'ş': 's',
        'ö': 'o',
        'ç': 'c',
        'İ': 'I',
        'Ğ': 'G',
        'Ü': 'U',
        'Ş': 'S',
        'Ö': 'O',
        'Ç': 'C'
    }

    # Klasördeki her dosya için işlem yap
    for filename in os.listdir(directory):
        # Dosya adında Türkçe karakter varsa
        if any(char in turkish_to_english.keys() for char in filename):
            # Yeni dosya adını oluştur
            new_filename = ''.join(turkish_to_english.get(char, char) for char in filename)
            # Eski dosyanın adını yeni adla değiştir
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Klasördeki resimlerin bulunduğu dizini belirt
directory = "images/"
# Türkçe karakterleri İngilizce karakterlerle değiştir
replace_turkish_characters(directory)
