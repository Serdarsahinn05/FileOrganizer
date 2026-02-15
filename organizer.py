import os
import shutil

# Şu anki dosya yolunu al
current_dir = os.path.dirname(os.path.realpath(__file__))

# Şu anki dosya yolunda cleaner dosyasını bul. Aslında cleaner uygun değil ama olsun
cleaner_dir = os.path.join(current_dir, "organizer")

# Eğer 'cleaner' klasörü yoksa hata vermesin, oluştursun
if not os.path.exists(cleaner_dir):
    os.makedirs(cleaner_dir)
    print("Organizer klasörü oluşturuldu. Lütfen içine düzenlenecek dosyaları atın.")
    exit()


files = os.listdir(cleaner_dir)
print(f"Düzenlenecek dosyalar: {files}")

for item in files:
    # Tam dosya yolunu oluştur
    source_path = os.path.join(cleaner_dir, item)

    # KONTROL 1: Bu bir dosya mı? (Klasörleri elleme)
    if os.path.isfile(source_path):

        # Dosya uzantısını al (noktadan sonrasını, küçük harfe çevir)
        # .jpg, .JPG, .png karışıklığını önlemek için .lower() ekledim
        extension = item.split(".")[-1].lower()

        # Eğer dosyanın uzantısı yoksa (örn: "README") 'Diger' diye klasör yapalım
        if "." not in item:
            extension = "Diger"

        # Hedef klasör yolu (Örn: cleaner/png)
        target_folder = os.path.join(cleaner_dir, extension)

        # KONTROL 2: Böyle bir klasör var mı? Yoksa oluştur.
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)

        # Hedef dosya yolu
        destination_path = os.path.join(target_folder, item)

        # TAŞIMA İŞLEMİ (Move)
        try:
            shutil.move(source_path, destination_path)
            print(f"Taşındı: {item} -> {extension}/")
        except Exception as e:
            print(f"Hata oluştu ({item}): {e}")

print("✅ Temizlik Tamamlandı!")

