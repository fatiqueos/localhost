import os
import webbrowser

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ana_menu():
    while True:
        clear_console()
        print("\nAşağıdaki işlemlerden birini seç:")
        print("1. Adres Sorgu")
        print("2. Aile Sorgu")
        print("3. GSM TC Sorgu")
        print("4. Ad Soyad Sorgu")
        print("5. Sulale Sorgu")
        print("6. TC GSM Sorgu")
        print("7. TC Sorgu")
        print("8. Sms Bomber")
        print("9. Projeye Git")
        print("q. Cikis")
        
        print()
        secim = input("Seciminiz (çıkmak için q): ")

        if secim == 'q':
            print("Çıkılıyor...")
            break
        elif secim == '9':
            webbrowser.open("https://github.com/fatiqueos/localhost")
            clear_console()
            input("Tarayıcınızı kontrol edin. Menüye dönmek için bir tuşa basın...")
        else:
            dosya_dict = {
                '1': "data/adres.py",
                '2': "data/aile.py",
                '3': "data/gsmtc.py",
                '4': "data/sorgu.py",
                '5': "data/sulale.py",
                '6': "data/tcgsm.py",
                '7': "data/tckn.py",
                '8': "data/smsbomber.py"
            }

            if secim in dosya_dict:
                print(f"{dosya_dict[secim]} dosyasını çalıştırıyorsun...")
                os.system(f'python {dosya_dict[secim]}')
                
                input("\nMenüye dönmek için bir tuşa basın...")
            else:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
