import subprocess
import os

def convert_dat_to_mp4(input_file, output_file=None, compression_level='high'):
    # Eğer çıktı dosyası belirtilmemişse, aynı isimle .mp4 uzantılı dosya oluştur
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '_compressed.mp4'
    
    # Sıkıştırma seviyesine göre CRF (Constant Rate Factor) değerini belirle
    # CRF değeri 0-51 arasındadır, daha yüksek değer = daha fazla sıkıştırma
    crf_values = {
        'low': '23',
        'medium': '28',
        'high': '35',
        'extreme': '40'
    }
    crf = crf_values.get(compression_level, '35')
    
    try:
        # ffmpeg komutunu çalıştır
        command = [
            'ffmpeg',
            '-i', input_file,
            '-c:v', 'libx264',  # H.264 codec kullan
            '-crf', crf,        # Sıkıştırma kalitesi
            '-preset', 'slower', # Daha iyi sıkıştırma için yavaş preset
            '-c:a', 'aac',      # Ses codec'i
            '-b:a', '128k',     # Ses bit hızı
            output_file
        ]
        
        print(f"Dönüştürme başladı... Sıkıştırma seviyesi: {compression_level}")
        subprocess.run(command, check=True)
        print(f"Dönüştürme başarılı! Dosya kaydedildi: {output_file}")
        
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    # Kullanıcıdan dosya yolunu al
    input_file = input("Lütfen .dat dosyasının yolunu girin: ")
    
    # Sıkıştırma seviyesini seç
    print("\nSıkıştırma seviyesini seçin:")
    print("1. Düşük sıkıştırma (daha iyi kalite)")
    print("2. Orta sıkıştırma")
    print("3. Yüksek sıkıştırma (önerilen)")
    print("4. Aşırı sıkıştırma (düşük kalite)")
    
    choice = input("Seçiminiz (1-4) [varsayılan: 3]: ").strip()
    
    compression_levels = {
        '1': 'low',
        '2': 'medium',
        '3': 'high',
        '4': 'extreme'
    }
    
    compression_level = compression_levels.get(choice, 'high')
    
    # Dosyanın var olup olmadığını kontrol et
    if not os.path.exists(input_file):
        print("Hata: Belirtilen dosya bulunamadı!")
    else:
        convert_dat_to_mp4(input_file, compression_level=compression_level) 