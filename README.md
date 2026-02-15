# Auto File Organizer (Desktop Cleaner) 🧹

Python kullanılarak yazılmış, karmaşık dosya yığınlarını saniyeler içinde düzenleyen basit bir otomasyon aracı. Bu script, belirlediğiniz klasördeki dosyaları uzantılarına göre (png, jpg, pdf, docx vb.) otomatik olarak ayrı klasörlere ayırır.

## 🚀 Nasıl Çalışır?

Script, bulunduğu dizinde `organizer` adında bir klasör arar.
1.  Eğer klasör yoksa oluşturur.
2.  Eğer klasör varsa ve içinde dosyalar bulunuyorsa, bu dosyaları uzantılarına göre (Örn: `organizer/png/resim.png`) alt klasörlere taşır.

## 🛠️ Gereksinimler

Bu proje sadece Python'un standart kütüphanelerini kullanır. Ekstra kurulum gerektirmez.
* **Python 3.x** yüklü olması yeterlidir.

## 💻 Kullanım

1.  **Projeyi İndirin:**
    ```bash
    git clone [https://github.com/Serdarsahinn05/FileOrganizer.git](https://github.com/Serdarsahinn05/FileOrganizer.git)
    cd FileOrganizer
    ```

2.  **Scripti İlk Kez Çalıştırın:**
    ```bash
    python organizer.py
    ```
    *Bu adımda `organizer` klasörü oluşturulacaktır.*

3.  **Dosyaları Yerleştirin:**
    Düzenlemek istediğiniz karmaşık dosyaları oluşan `organizer` klasörünün içine atın.

4.  **Tekrar Çalıştırın:**
    Scripti tekrar çalıştırdığınızda (`python organizer.py`), tüm dosyalarınızın türlerine göre klasörlendiğini göreceksiniz.

## ⚠️ Uyarı
Script dosyalarınızı taşırken (move işlemi) çalışır. Herhangi bir veri kaybı yaşamamak için önemli dosyalarınızın yedeğini aldığınızdan emin olun.

## 📝 Lisans
Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir.

---
**Geliştirici:** [Serdarsahinn05](https://github.com/Serdarsahinn05)
