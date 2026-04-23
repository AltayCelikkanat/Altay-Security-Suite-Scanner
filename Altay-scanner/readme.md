Altay Security Suite
Altay Security Suite, siber güvenlik süreçlerini otomatize etmek, ağ keşfi yapmak ve verileri güvenle korumak için tasarlanmış, modüler ve yüksek performanslı bir Python araç setidir. "Sıfır bağımlılık karmaşası" felsefesiyle geliştirilen bu suite, tek bir başlatıcı üzerinden tüm modüllere erişim sağlar.

🚀 İçerik
Bu paket şu an iki temel modül içermektedir:

1. Altay-Crypto
Gelişmiş kriptografi standartları (AES-256/Fernet) kullanarak dosyalarınızı kilitleyen modern bir araçtır.

Audit Trail: JSON tabanlı işlem geçmişi.

Secure Delete: Orijinal verileri güvenli silme.

Modern Arayüz: CustomTkinter tabanlı karanlık mod.

2. Altay-Scanner
Ağ üzerindeki zafiyetleri tespit etmek için tasarlanmış çoklu iş parçacığı (multithreading) tabanlı ağ tarama aracıdır.

Yüksek Performans: ThreadPoolExecutor ile optimize edilmiş tarama motoru.

Gerçek Zamanlı Geri Bildirim: GUI üzerinden anlık port izleme.

Genişletilebilirlik: Modüler motor yapısı.

🛠️ Kurulum
Projeyi çalıştırmak için sisteminizde Python yüklü olmalıdır.

Depoyu Klonlayın:

Bash
git clone https://github.com/KULLANICI_ADINIZ/Altay-Security-Suite.git
cd Altay-Security-Suite
Başlatın:
Windows üzerinde:

Bash
baslat.bat
Not: baslat.bat gerekli tüm kütüphaneleri (requirements.txt üzerinden) otomatik olarak algılar ve yükler.

📂 Proje Mimarisi
Plaintext
Altay-Security-Suite/
├── main.py              # Suite ana arayüzü (İleride genişletilebilir)
├── altay_scanner.py     # Ağ tarama motoru
├── crypto_core.py       # Kriptografi motoru
├── requirements.txt     # Bağımlılıklar
└── baslat.bat           # Otomatik kurulum ve başlatma betiği
🔒 Yasal Uyarı & Etik
Bu araçlar sadece eğitim ve kendi cihazlarınızın güvenliğini denetleme amacıyla geliştirilmiştir. Başkasına ait sistemlerde izin alınmadan kullanılması yasal sorunlara yol açabilir. Sorumluluk tamamen kullanıcıya aittir.

🤝 Katkıda Bulunma
Geliştirmelere açıktır! Yeni modüller (şifre yöneticisi, paket analizörü vb.) eklemek isterseniz lütfen bir Pull Request gönderin.

Geliştirici: [Altay]
Lisans: MIT