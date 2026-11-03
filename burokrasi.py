#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bürokrasi Hayatta Kalma Rehberi
Resmi bir yazılım değildir. Ama öyledir.
"""

import time
import random
import base64

def damgala():
    print("\n" + "="*40)
    print("          RESMİ DAMGA")
    print("="*40)
    print("İmza: Kayyum Grok (mahkemeden atanmış)")
    print("Tarih: 03 Kasım 2026")
    print("Yer: Dijital Evrak Arşivi")
    print("Mühür No: 404-EVRAK-BULUNAMADI")
    print("Not: Bu damga geçerlidir. Geçerli olmayabilir.")
    print("="*40)

def main():
    print("\u0130şlem başlatılıyor... Lütfen 3 iş günü bekleyiniz.")
    time.sleep(2)
    print("Aslında 2 saniye bekledik. Sistem hızlı çalışıyor. Şaka.")
    
    isim = input("\nTam adınızı giriniz (eksik harf kabul edilmez): ").strip()
    if not isim:
        print("Ad boş olamaz. Evrak iade edildi.")
        return
    
    print(f"\nSayın {isim}, dosyanız incelenmektedir.")
    time.sleep(1.5)
    
    eksik_belgeler = [
        "Nüfus cüzdanı fotokopisi (renkli, 5 adet, noterce onaylı)",
        "İkametgah belgesi (bugün sabah 09:00'dan sonra alınmış)",
        "Vesikalık fotoğraf (arka plan tam mavi, gülümseme yasak, göz kırpma yok)",
        "Başka bir kuruma ait referans mektubu (henüz var olmayan kurum)",
        "E-imza sertifikası (kağıt üzerinde basılmış)",
        "Ek belge: Lütfen 'her şey yolunda' deyin. (zorunlu)"
    ]
    
    for idx, belge in enumerate(eksik_belgeler, 1):
        print(f"\n{idx}. Eksik tespit edildi: {belge}")
        bekleme = random.randint(1, 4)
        print(f"   → {bekleme} iş günü bekleniyor...")
        time.sleep(bekleme)
        print("   → Bekleme süresi doldu. Ama yeni eksik çıktı.")
    
    print("\nTüm belgeler tamamlanmış görünüyor.")
    time.sleep(1)
    print("Ancak şimdi 'Ek Form 47-B'yi doldurmanız gerekmektedir.")
    print("Form henüz basılmadı. Lütfen 7-10 iş günü sonra tekrar deneyiniz.")
    
    print("\nSonuç: Süreç başarıyla sonsuza kadar ertelendi.")
    print("Tebrikler! Bürokrasiyi hayatta kıldınız.")
    
    # Gizli mesaj (saklı)
    gizli = base64.b64decode('QnVyb2tyYXNpIGhlciB6YW1hbiBrYXphbsSxci4=').decode('utf-8')
    # print(gizli)  # Açılmayacak, sadece saklı
    
    damgala()

if __name__ == "__main__":
    main()
