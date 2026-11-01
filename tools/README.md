# YÖKDİL Koçu – güncelleme notu

- `index.html` şifreli yükleyicidir; uygulamanın kendisi AES-GCM ile şifrelidir (anahtar: PBKDF2-SHA256, 310.000 tur).
- Şifre ve tuz (salt) bu depoda yoktur. Aynı tuz kullanılırsa telefonda "hatırla" ile kaydedilen anahtar güncellemeden sonra da çalışır.
- Kaynak: claude.ai'deki "YÖKDİL Koçu" artifact'ı. Güncellemek için: artifact'tan HTML'i al → `pwa.py` ile PWA başlıklarını ekle → `lock.py düz.html index.html şifre.txt tuz.txt` ile şifrele → buraya yükle.
- Tuz değeri: index.html içindeki `var S="..."` satırında (gizli değildir).
