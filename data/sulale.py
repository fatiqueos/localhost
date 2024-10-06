import requests
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sulale_sorgula(tc):
    url = f"http://localhost/sulaleapi.php?tc={tc}"

    print("Sorgulanıyor, lutfen bekleyin...")
    time.sleep(2)

    try:
        response = requests.get(url)
        response.raise_for_status()

        try:
            veri = response.json()
        except ValueError:
            print("Kisinin sulale bilgisi bulunamadi.")
            return

        if 'data' not in veri or not veri['data']:
            print("Kisinin sulale bilgisi bulunamadi.")
            return

        duzenlenmis_veri = ""
        for person in veri['data']:
            duzenlenmis_veri += "\n".join([f"{key}: {value}" for key, value in person.items()]) + "\n\n"

        print(duzenlenmis_veri)

    except requests.exceptions.RequestException as e:
        print("Sulale sorgulanirken hata olustu:", e)

if __name__ == "__main__":
    clear_screen()
    tc_kimlik = input("TC Kimlik Numarasini girin: ")
    sulale_sorgula(tc_kimlik)
