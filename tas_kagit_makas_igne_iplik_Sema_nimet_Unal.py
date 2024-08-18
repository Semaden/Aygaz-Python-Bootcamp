import random

def oyuna_basla_mi():
    """
    Önce oyuncunun oyuna başlamak isteyip istemediğini kontrol eder.
    Oyuncu oynamak istiyorsa bilgisayarın oyuna başlamak isteyip istemediğini kontrol eder.
    """
    while True:
        oyuncu_baslangic = input("Oyuna başlamak ister misiniz? (evet/hayır): ").lower()
        if oyuncu_baslangic in ["evet", "hayır"]:
            break
        print("Geçersiz yanıt. Lütfen 'evet' veya 'hayır' yazın.")
    
    if oyuncu_baslangic != "evet":
        print("Oyuncu oyuna başlamak istemedi. Oyun başlatılmıyor.")
        return None, None
    
    bilgisayar_baslangic = random.choice(["evet", "hayır"])
    if bilgisayar_baslangic != "evet":
        print("Bilgisayar oyuna başlamak istemedi. Başka bir zaman şansını dene :)")
        return oyuncu_baslangic, bilgisayar_baslangic
    
    return oyuncu_baslangic, bilgisayar_baslangic

def print_kurallar():
    
    #Kuralları satır satır ekrana yazdırır.
    
    print("Kurallar:\n"
          "Taş makası kırar.\n"
          "Taş iğneyi kırar.\n"
          "Makas ipliği keser.\n"
          "Makas kağıdı keser.\n"
          "İplik taşı yener.\n"
          "İplik kağıdı sarar.\n"
          "Kağıt taşı sarar.\n"
          "Kağıt ipliği sarar.\n"
          "İğne kağıdı deler.\n"
          "İğne ipliği yener.")

def tas_kagit_makas_igne_iplik_Sema_Nimet_UNAL():
    print("Taş, Kağıt, Makas, İğne ve İplik Oyununa Hoş Geldiniz!")
    print_kurallar()
    print("İlk iki turu kazanan oyunu kazanır.\n")

    secenekler = ["taş", "kağıt", "makas", "iğne", "iplik"]
    kurallar = {
        "taş": {"makas": True, "iğne": True, "kağıt": False, "iplik": False},
        "kağıt": {"taş": True, "iğne": True, "makas": False, "iplik": False},
        "makas": {"iplik": True, "kağıt": True, "taş": False, "iğne": False},
        "iğne": {"kağıt": True, "iplik": True, "taş": False, "makas": False},
        "iplik": {"kağıt": True, "taş": True, "makas": False, "iğne": False},
    }

    oyuncu_baslangic, bilgisayar_baslangic = oyuna_basla_mi()
    if oyuncu_baslangic is None or bilgisayar_baslangic is None:
        return
    
    print("Oyun başlıyor...\n")

    toplam_oyun = 0
    toplam_tur = 0

    while True:
        toplam_tur_oyun = 0
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas, iğne, iplik, ipucu, exit): ").lower()
            while oyuncu_secimi not in secenekler + ["ipucu", "exit"]:
                oyuncu_secimi = input("Geçersiz seçenek. Lütfen taş, kağıt, makas, iğne, iplik, ipucu veya exit seçin: ").lower()
            
            if oyuncu_secimi == "exit":
                print("Oyundan çıkılıyor. Oyun sona erdi.")
                return
            
            if oyuncu_secimi == "ipucu":
                print_kurallar()
                continue  # ipucu seçildiğinde tur sayısını artırmadan kuralları gösterip devam et

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            else:
                if kurallar[oyuncu_secimi].get(bilgisayar_secimi, False):
                    print("Bu turu siz kazandınız!")
                    oyuncu_galibiyet += 1
                else:
                    print("Bu turu bilgisayar kazandı!")
                    bilgisayar_galibiyet += 1

            toplam_tur_oyun += 1  # Her turda toplam tur sayısını artır
            toplam_tur += 1  # Genel toplam tur sayısını artır

            print(f"Skor: Siz {oyuncu_galibiyet} - {bilgisayar_galibiyet} Bilgisayar")
            print(f"Bu oyunda toplam {toplam_tur_oyun} tur oynandı.")
            print(f"Şu ana kadar toplam {toplam_oyun} oyun tamamlandı ve toplam {toplam_tur} tur oynandı.\n")

        toplam_oyun += 1  # Toplam oyun sayısını artır

        if oyuncu_galibiyet == 2:
            print("Tebrikler! Oyunu sen kazandın.")
        else:
            print("Üzgünüm :( Oyunu bilgisayar kazandı.")

        while True:
            tekrar_oyna = input("Devam etmek ister misiniz? (evet/hayır): ").lower()
            if tekrar_oyna == "evet":
                break
            elif tekrar_oyna == "hayır":
                print("Oyundan çıkılıyor. Bye Bye.")
                return
            else:
                print("Geçersiz yanıt. Lütfen 'evet' veya 'hayır' yazın.")

        bilgisayar_oynama_istegi = random.choice(["evet", "hayır"])
        if bilgisayar_oynama_istegi == "hayır":
            print("Bilgisayar artık oynamak istemiyor. Şansını sonra tekrar dene :)")
            break

    print("Oyun bitti. Tekrar görüşmek üzere!")

# Oyunu başlatmak için fonksiyonu çalıştırın:
tas_kagit_makas_igne_iplik_Sema_Nimet_UNAL()
