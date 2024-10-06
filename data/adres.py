import mysql.connector
import requests
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def query_db(tc):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='secmen2015'
    )
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM secmen2015 WHERE TC = %s", (tc,))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def format_user_info(data, tc):
    return f"""
TC: {tc}
ADI: {data['ADI']}
SOYADI: {data['SOYADI']}
DOGUM TARIHI: {data['DOGUMTARIHI']}
IL: {data['ADRESIL']}
ILCE: {data['ADRESILCE']}
MAHALLE: {data['MAHALLE']}
CADDE: {data['CADDE']}
KAPINO: {data['KAPINO']}
DAIRENO: {data['DAIRENO']}
"""

def get_google_maps_link(data):
    address = f"{data['ADRESIL']} {data['ADRESILCE']} {data['MAHALLE']} {data['CADDE']} {data['KAPINO']} {data['DAIRENO']}"
    encoded_address = requests.utils.quote(address)
    return f"https://www.google.com/maps/search/?api=1&query={encoded_address}"

def main():
    clear_screen()
    tc_kimlik = input("TC Kimlik Numarasini girin: ")
    
    print("Sorgulanıyor, lutfen bekleyin...")
    time.sleep(2)

    try:
        result = query_db(tc_kimlik)

        if not result:
            print(f"Kisinin adres bilgisi bulunamadi.")
            return

        user_info = format_user_info(result[0], tc_kimlik)
        google_maps_link = get_google_maps_link(result[0])

        print(user_info)
        print(f"Google Maps Linki: {google_maps_link}")

    except Exception as e:
        print("Veritabanı sorgusu sırasında bir hata oluştu:", e)

if __name__ == "__main__":
    main()
