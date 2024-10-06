import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ana_menu():
    clear_console()
    while True:
        print("\nAşağıdaki işlemlerden birini seç:")
        print("1. Adres Sorgu")
        print("2. Aile Sorgu")
        print("3. GSM TC Sorgu")
        print("4. Ad Soyad Sorgu")
        print("5. Sulale Sorgu")
        print("6. TC GSM Sorgu")
        print("7. TC Sorgu")
        print("q. Cikis")
        
        print()
        secim = input("Seciminiz (cikmak için q): ")

        if secim == 'q':
            print("Cikiliyor...")
            break
        else:
            dosya_dict = {
                '1': "data/adres.py",
                '2': "data/aile.py",
                '3': "data/gsmtc.py",
                '4': "data/sorgu.py",
                '5': "data/sulale.py",
                '6': "data/tcgsm.py",
                '7': "data/tckn.py"
            }

            if secim in dosya_dict:
                print(f"{dosya_dict[secim]} dosyasini calistiriyorsun...")
                os.system(f'python {dosya_dict[secim]}')
                
                input("\nMenüye donmek için bir tuşa basın...")
                clear_console()
            else:
                print("Gecersiz secim! Lutfen tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
