# convert_dat_to_mp4 - .dat Dosyasını .mp4 Formatına Dönüştürme Aracı

Bu Python programı, `.dat` dosyalarını `.mp4` formatına dönüştürmek ve sıkıştırma seviyesini ayarlamak için `ffmpeg` aracını kullanır. Kullanıcı, dönüşüm için dosya yolunu ve sıkıştırma seviyesini seçebilir. Bu program, çıktı dosyasını istediğiniz kalitede sıkıştırarak mp4 formatında kaydeder.

## Gereksinimler

- Python 3.x
- `ffmpeg` yüklü olmalıdır. `ffmpeg` yüklemek için aşağıdaki komutu kullanabilirsiniz:
  - **Windows:** [FFmpeg İndirme ve Kurulum](https://ffmpeg.org/download.html)
  - **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
  - **MacOS (Homebrew ile):**
    ```bash
    brew install ffmpeg
    ```

## Kullanım

1. **Dosya Yolu Seçimi:**
   Program başladığında, `.dat` formatındaki dosyanızın yolunu girmeniz istenecektir.

2. **Sıkıştırma Seviyesi Seçimi:**
   Program, dönüşüm sırasında uygulamak istediğiniz sıkıştırma seviyesini seçmenizi ister. Mevcut seçenekler şunlardır:
   
   - **1:** Düşük sıkıştırma (daha iyi kalite)
   - **2:** Orta sıkıştırma
   - **3:** Yüksek sıkıştırma (önerilen seçenek)
   - **4:** Aşırı sıkıştırma (daha düşük kalite)
   
   Varsayılan seçenek `3` (Yüksek sıkıştırma) olarak ayarlanmıştır.

3. **Dönüştürme Başlangıcı:**
   Seçimlerinizi yaptıktan sonra, program `ffmpeg` komutunu çalıştırarak dönüştürme işlemine başlar. İşlem tamamlandığında, dönüştürülmüş `.mp4` dosyanız belirtilen isimle kaydedilecektir.

## Fonksiyonlar

### `convert_dat_to_mp4(input_file, output_file=None, compression_level='high')`

- **input_file**: Dönüştürülecek `.dat` dosyasının yolu.
- **output_file**: Çıktı dosyasının adı (isteğe bağlı). Belirtilmezse, giriş dosyasının ismiyle aynı olacak şekilde `_compressed.mp4` eklenir.
- **compression_level**: Sıkıştırma seviyesi. Seçenekler:
  - `'low'`: Düşük sıkıştırma, yüksek kalite
  - `'medium'`: Orta sıkıştırma
  - `'high'`: Yüksek sıkıştırma, önerilen seçenek
  - `'extreme'`: Aşırı sıkıştırma, düşük kalite

### Çalışma Prensibi

1. Kullanıcı, giriş dosyasının yolunu ve sıkıştırma seviyesini seçer.
2. `ffmpeg` komut satırı aracı, belirtilen sıkıştırma seviyesine göre `.dat` dosyasını `.mp4` formatına dönüştürür.
3. Program, dönüşüm tamamlandığında başarı mesajı verir ve çıktı dosyasını kaydeder.

## Örnek Kullanım

```bash
python convert_dat_to_mp4.py
